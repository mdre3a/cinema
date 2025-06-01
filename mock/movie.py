from sqlalchemy.orm.session import Session
from app.models.movie import Movie


def update(db: Session):
    _id = 0
    movies = [
        Movie(id=(_id := _id + 1), name="The Shawshank Redemption", poster="5ffd0b34-6189-4a80-adf9-c1c3b38c6910.jpg"),
        Movie(id=(_id := _id + 1), name="The Godfather", poster="e7f03d97-c284-4c09-92eb-c2521ce8c13b.jpg"),
        Movie(id=(_id := _id + 1), name="The Dark Knight", poster="e5c4206a-0636-4466-85da-b9267383e606.jpg"),
        Movie(id=(_id := _id + 1), name="12 Angry Men", poster="e7869e53-4ea9-4450-889a-cfbb69302d6f.jpg"),
        Movie(id=(_id := _id + 1), name="The Lord of the Rings: The Return of the King", poster="783a46cd-94c7-430f-93e4-e49f53a52dbb.jpg"),
        Movie(id=(_id := _id + 1), name="Schindler's List", poster="3b06dad0-e975-48eb-844f-f96c043eba3d.jpg"),
        Movie(id=(_id := _id + 1), name="Pulp Fiction", poster="1c94ccf8-0b72-4c6c-9bb3-226593c9d6db.jpg")
    ]
    db.bulk_save_objects(movies)
