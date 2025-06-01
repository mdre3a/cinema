from typing import Optional, List
from fastapi import Depends, Query, status, Body, Path
from fastapi import APIRouter
from sqlalchemy.orm.session import Session
from app.api.deps import require_admin
from app import crud
from app.api import deps
from app.schemas.schedule import Schedule, ScheduleCreate, ScheduleUpdate

router = APIRouter(prefix="/schedule", tags=["Schedule"])


@router.get("/",
            summary="read schedule list",
            description="this method returns the list of schedules",
            response_model=List[Schedule])
def list_schedule(
        room_id: Optional[int] = Query(None, description="Optional room id to filter schedules"),
        schedule_id: Optional[int] = Query(None, description="Optional schedule id to filter schedules"),
        db: Session = Depends(deps.get_db),
):
    filters = None
    if room_id is not None:
        filters = [crud.schedule.model.room_id == room_id]
    if schedule_id is not None:
        filters = [crud.schedule.model.id == schedule_id]
    schedules = crud.schedule.get_multi_filter(db=db, filters=filters)
    return list(schedules)


@router.post("/",
             summary="create a schedule",
             description="this method creates a new schedule",
             response_model=Schedule)
def create_schedule(
        db: Session = Depends(deps.get_db),
        schedule: ScheduleCreate = Body(description="schedule data"),
        user=Depends(require_admin)
):
    schedule = crud.schedule.create(db=db, obj_in=schedule)
    return schedule


@router.put("/{schedule_id}",
            summary="update a schedule",
            description="this method updates a schedule",
            status_code=status.HTTP_200_OK)
def update_schedule(
        db: Session = Depends(deps.get_db),
        schedule_id: int = Path(gt=0, description="schedule id to update"),
        schedule: ScheduleUpdate = Body(description="schedule data"),
        user=Depends(require_admin)
):
    crud.schedule.update_by_id(db=db, id=schedule_id, obj_in=schedule)
    crud.schedule.update_schedule(db=db, schedule_id=schedule_id, schedule=schedule)
    return {"message": "Schedule successfully updated."}


@router.delete("/{schedule_id}",
               summary="delete a schedule",
               description="this method deletes a schedule",
               status_code=status.HTTP_200_OK)
def delete_schedule(
        db: Session = Depends(deps.get_db),
        schedule_id: int = Path(gt=0, description="schedule id to delete"),
        user=Depends(require_admin)
):
    crud.schedule.remove(db=db, id=schedule_id)
    return {"message": "Schedule successfully deleted."}
