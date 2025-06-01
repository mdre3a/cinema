# Import all the models, so that Base has them before being
# imported by Alembic
from app.db.base_class import Base  # noqa
from app.models.user import User  # noqa
from app.models.movie import Movie  # noqa
from app.models.room import Room  # noqa
from app.models.schedule import Schedule  # noqa
