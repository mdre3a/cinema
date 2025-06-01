from typing import Optional, List
from fastapi import Depends, status, Body, Path, Query
from fastapi import APIRouter
from sqlalchemy.orm.session import Session
from app.api.deps import require_admin
from app import crud
from app.api import deps
from app.schemas.room import Room, RoomCreate, RoomUpdate

router = APIRouter(prefix="/room", tags=["Room"])


@router.get("/",
            summary="read room list",
            description="this method returns the list of rooms",
            response_model=List[Room])
def list_room(
        db: Session = Depends(deps.get_db),
        room_id: Optional[int] = Query(None, gt=0, description="Optional room id to filter rooms"),
        movie_id: Optional[int] = Query(None, gt=0, description="Optional movie id to filter rooms"),
):
    rooms = crud.room.get_rooms(db=db, room_id=room_id, movie_id=movie_id)
    return list(rooms)


@router.post("/",
             summary="create a room",
             description="this method creates a new room",
             response_model=Room)
def create_room(
        db: Session = Depends(deps.get_db),
        room: RoomCreate = Body(description="room data"),
        user=Depends(require_admin)
):
    room = crud.room.create(db=db, obj_in=room)
    return room


@router.put("/{room_id}",
            summary="update a room",
            description="this method update room",
            status_code=status.HTTP_200_OK)
def update_room(
        db: Session = Depends(deps.get_db),
        room_id: int = Path(gt=0, description="room id to update"),
        room: RoomUpdate = Body(description="room data"),
        user=Depends(require_admin)
):
    crud.room.update_by_id(db=db, id=room_id, obj_in=room)
    return {"message": "Room successfully updated."}


@router.delete("/{room_id}",
               summary="delete a room",
               description="this method deletes room",
               status_code=status.HTTP_200_OK)
def delete_room(
        db: Session = Depends(deps.get_db),
        room_id: int = Path(gt=0, description="room id to delete"),
        user=Depends(require_admin)
):
    crud.room.remove(db=db, id=room_id)
    return {"message": "Room successfully deleted."}
