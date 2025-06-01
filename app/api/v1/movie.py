from typing import Optional, List
from fastapi import Depends, HTTPException, status, Query, Body, Path, File, UploadFile
from fastapi import APIRouter
from sqlalchemy.orm.session import Session
from app.api.deps import require_admin
from app import crud
from app.api import deps
from app.core.config import settings
from app.schemas.movie import MovieShowtime, Movie, MovieCreate, MovieUpdate, MoviePosterUpdate
import uuid

router = APIRouter(prefix="/movie", tags=["Movie"])


@router.get("/",
            summary="read movie list",
            description="this method returns the list of movies",
            response_model=List[MovieShowtime])
def list_movie(
        db: Session = Depends(deps.get_db),
        room_id: Optional[int] = Query(None, gt=0, description="Optional room id to filter movies"),
        movie_id: Optional[int] = Query(None, gt=0, description="Optional movie id to filter movies"),
):
    movies = crud.movie.get_movies(db=db, room_id=room_id, movie_id=movie_id)
    return list(movies)


@router.post("/",
             summary="create a movie",
             description="this method creates a new movie",
             response_model=Movie)
def create_movie(
        db: Session = Depends(deps.get_db),
        movie: MovieCreate = Body(description="movie data"),
        user=Depends(require_admin)
):
    movie = crud.movie.create(db=db, obj_in=movie)
    return movie


@router.put("/{movie_id}",
            summary="update a movie",
            description="this method updates a movie",
            status_code=status.HTTP_200_OK)
def update_movie(
        db: Session = Depends(deps.get_db),
        movie_id: int = Path(gt=0, description="movie id to update"),
        movie: MovieUpdate = Body(description="movie data"),
        user=Depends(require_admin)
):
    crud.movie.update_by_id(db=db, id=movie_id, obj_in=movie)
    return {"message": "Movie successfully updated"}


@router.delete("/{movie_id}",
               summary="delete a movie",
               description="this method deletes a movie",
               status_code=status.HTTP_200_OK)
def delete_movie(
        db: Session = Depends(deps.get_db),
        movie_id: int = Path(gt=0, description="movie id to delete"),
        user=Depends(require_admin)
):
    crud.movie.remove(db=db, id=movie_id)
    return {"message": "Movie successfully deleted."}


@router.post("/poster/{movie_id}",
             summary="change poster of movie",
             description="this method replaces the poster of a movie",
             )
async def update_poster(
        db: Session = Depends(deps.get_db),
        movie_id: int = Path(gt=0, description="movie id to update poster for"),
        poster: Optional[UploadFile] = File(None),
        user=Depends(require_admin)
):
    movie = MoviePosterUpdate()
    if poster:
        if not poster.content_type.startswith("image/"):
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="File must be an image")
        ext = poster.filename.split('.')[-1]
        file_name = f"{uuid.uuid4()}.{ext}"
        file_path = f"{settings.STATIC_STORAGE_DIR}/posters/{file_name}"
        with open(file_path, "wb") as dest_file:
            content = await poster.read()
            dest_file.write(content)
        movie.poster = file_name
    else:
        movie.poster = None
    crud.movie.update_by_id(db=db, id=movie_id, obj_in=movie)
    return {"message": "Poster successfully updated"}
