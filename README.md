# 🎬 Cinema Booking Backend

A backend system for managing movie scheduling and seat booking in multiple cinema rooms. Built with FastAPI, SQLAlchemy, and SQLite — this project was developed as part of a backend developer interview task.

---

## 🚀 Features

- 🔴 **Rooms Management** — Room layout defined by number of rows and seats per row.
- 🎥 **Movie Scheduling** — Movies scheduled per room with a specific showtime.
- 💺 **Seat Booking** — Users can reserve seats for scheduled movies; unavailable seats are reflected live.
- 👥 **User Authentication** — With role-based access (admin / user).
- 🛠️ **Admin Features** — Manage rooms, movies, schedules, and view all reservations.

---

## 🧠 System Design Overview

### 🏛️ Entities & Relationships

#### 🏠 Rooms

- Each room has a seating layout:
    - `max_row`: Number of rows (e.g., 10)
    - `max_seat`: Number of seats per row (e.g., 8)

#### 🎬 Movies

- Each movie has:
    - `name`
    - `poster`: URL or image path

#### 🗓️ Schedules

- Connects a `movie` and a `room` at a specific `showtime`.
- Foreign keys:
    - `room_id → Room.id`
    - `movie_id → Movie.id`
- **Constraint**: `(room_id, showtime)` is **unique**, ensuring no double-booking of a room at the same time.

#### 👤 Users

- Identified by a **unique email** (used as username).
- Each user has a `role`: either `admin` or `user`.

#### 💺 Seat Reservations

- Represents a booking of a specific seat in a room for a particular schedule by a user.
- Attributes:
    - `row_number`, `seat_number`
    - `schedule_id → Schedule.id`
    - `user_id → User.id`

This structure allows:

- Checking what seat a user booked, and for which movie and schedule.
- Displaying seat maps with real-time reservation status.

---

### 🔐 Access Control

| Role      | Capabilities                                                                                                          |
|-----------|-----------------------------------------------------------------------------------------------------------------------|
| **User**  | View rooms, movies, schedules. Book seats. See which seats are taken, but not who booked them.                        |
| **Admin** | Full control over all resources. Can manage rooms, movies, schedules, and view reservations **with user identities**. |

...

## 🔐 Default Users (Demo Accounts)

You can use the following preloaded accounts for testing and demonstration:

| Role  | Email                 | Password |
|-------|-----------------------|----------|
| Admin | `admin@localdemo.com` | `123`    |
| User  | `user@localdemo.com`  | `123`    |

> These demo users are pre-created in the database for easy access to admin and user functionality.

---

## 📌 Notes

---

## 🧰 Tech Stack

| Tool       | Purpose                                  |
|------------|------------------------------------------|
| FastAPI    | Web API framework                        |
| SQLAlchemy | ORM and database interaction             |
| SQLite     | Lightweight development database         |
| Alembic    | Database migrations                      |
| Poetry     | Dependency and environment manager       |
| Security   | Token-based authentication(OAuth2 + JWT) |

---

## ⚙️ How to Run & Migrate the Project

Follow these steps to set up and run the project:

### 📥 1. Clone the Repository

```bash
git clone https://github.com/mdre3a/cinema.git
cd cinema
```

### 📦 2. Install Dependencies

```bash
poetry install
```

### 🛠️ 3. Generate and Apply Migrations

```bash
poetry run alembic revision --autogenerate -m "initial migration"
poetry run alembic upgrade head
```

### 🧪 4. Import Mock Data

```bash
poetry run import_mock_data
```

### 🚀 5. Run the Application

```bash
poetry run app
```

Now open your browser at http://localhost:8000/docs to interact with the API using Swagger UI.
