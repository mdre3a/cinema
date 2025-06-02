from typing import Any, Optional, List
from fastapi import Depends, Query, Body, HTTPException, status
from fastapi import APIRouter
from sqlalchemy.orm.session import Session
from app.api.deps import get_current_user, require_user
from app import crud
from app.api import deps
from app.schemas.seat import Seat, SeatBase, SeatCreate
from app.schemas.user import UserToken

router = APIRouter(prefix="/seat", tags=["Seat"])


@router.get("/",
            summary="read reserved seat list",
            description="this method returns the list of reserved seats",
            response_model=List[Seat])
def list_seat(
        room_id: Optional[int] = Query(None, gt=0, description="Optional room id to filter seats"),
        movie_id: Optional[int] = Query(None, gt=0, description="Optional movie id to filter seats"),
        schedule_id: Optional[int] = Query(None, gt=0, description="Optional schedule id to filter seats"),
        user_id: Optional[int] = Query(None, gt=0, description="Optional user id to filter seats"),
        db: Session = Depends(deps.get_db),
        user=Depends(get_current_user)
):
    current_user = None
    if user is not None:
        current_user = UserToken(**user)
        if user_id is not None:
            if user_id != current_user.id and not current_user.role == "admin":  # a typical user wants to see other user reservations::forbidden
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                )
    seats = crud.seat.get_reserved_seats(db=db, room_id=room_id, schedule_id=schedule_id, movie_id=movie_id, user_id=user_id)

    if current_user is None or ((current_user.role != "admin") and (user_id is None or current_user.id != user_id)):
        current_user_id = current_user.id if current_user is not None else None
        for seat in seats:
            if seat.user_id != current_user_id:
                seat.user_id = None
    return list(seats)


@router.post("/reserve",
             summary="reserve a seat",
             description="this method reserves a seat for a user",
             status_code=status.HTTP_201_CREATED,
             )
def reserver_seat(
        schedule_id: int = Query(gt=0, description="schedule id to reserve"),
        seats: List[SeatBase] = Body(description="seats to reserve"),
        db: Session = Depends(deps.get_db),
        user=Depends(require_user)
):
    new_seats = []
    room = crud.room.get_by_schedule_id(db=db, id=schedule_id)
    if room is None:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="No room found")

    for seat in seats:
        if not (0 < seat.row <= room.max_rows):
            raise HTTPException(status_code=400, detail=f"Row must be between 0 and {room.max_rows}")
        if not (0 < seat.seat <= room.max_seats):
            raise HTTPException(status_code=400, detail=f"Seat must be between 0 and {room.max_seats}")
        new_seat = SeatCreate(schedule_id=schedule_id, row=seat.row, seat=seat.seat, user_id=user.id)
        new_seats.append(new_seat)
    crud.seat.create_multi(db=db, objs_in=new_seats)
    return {"message": "Seat(s) reserved successfully"}
