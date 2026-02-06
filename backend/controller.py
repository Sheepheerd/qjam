import uuid
from uuid import UUID

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Room(BaseModel):
    session_id: UUID
    queue: list[str]
    queue_index: int


rooms: list[Room] = []


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "FastAPI is up and running!"}


@app.post("/new")
def create_room() -> Room:
    room: Room = Room(session_id=uuid.uuid4().hex, queue=[], queue_index=-1)
    rooms.append(room)
    return room


@app.post("/{session_id}")
def delete_room(session_id: UUID) -> None:
    for room in rooms:
        if room.session_id == session_id:
            rooms.remove(room)
            return
    raise HTTPException(status_code=404, detail="Item not found")


@app.get("/test/{get_num}")
def read_item(item_id: int, q: str = None):
    return {"get_num": item_id, "q": q}
