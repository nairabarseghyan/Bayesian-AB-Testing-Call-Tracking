from fastapi import FastAPI
from typing import Union

app = FastAPI()

test_user_id = 0

@app.get("/arm")
async def get_arm(id: int):
    return {"id": id, "type": "type", "budget": "budget"}

@app.post("/arm")
async def add_arm(id: int, type: str, budget: Union[float, None]):
    return {"id": id, "type": type, "budget": budget}

@app.put("/arm")
async def mod_arm(id: int, type: Union[str, None], budget: Union[float, None]):
    return {"id": id, "type": type, "budget": budget}

