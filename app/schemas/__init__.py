from .movie import Movie, MovieShowtime
from .user import User
from .seat import Seat
from .schedule import Schedule, ScheduleInDB, ScheduleRoom
from .room import Room

ScheduleInDB.update_forward_refs(Movie=Movie)
Schedule.update_forward_refs(Movie=Movie)

MovieShowtime.update_forward_refs(ScheduleRoom=ScheduleRoom)
