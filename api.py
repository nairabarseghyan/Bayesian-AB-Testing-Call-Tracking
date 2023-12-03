from fastapi import FastAPI
from typing import Union
import AB_Testing
import pandas as pd

app = FastAPI()

test_user_id = 0

def verify_client(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        return await func(*args, **kwargs)

    return wrapper

@app.get("/arm")
async def get_arm(id: int = -1):
    with AB_Testing.data_preperation.SqlHandler("CallTracking", "DimAdvertisement") as call_results:
        res = call_results.from_sql_to_pandas(0, 64).to_dict()
        print("Results ", res)
        return {k:{id:v[id]} if id < len(v) and id >= 0 else v for k, v in res.items()} if id is not None else res

@app.post("/arm")
async def add_arm(id: int, type: str):
    with AB_Testing.data_preperation.SqlHandler("CallTracking", "DimAdvertisement") as call_results:
        call_results.insert_many(pd.DataFrame({
            "advertisementid": [id],
            "advertisementtype": [type]
        }))
    return {"AdvertisementId": id, "AdvertisementType": type}

@app.put("/arm")
async def mod_arm(id: int, type: Union[str, None], c, t):
    
    # with AB_Testing.data_preperation.SqlHandler("CallTracking", "DimAdvertisement") as call_results:
    return {"id": id, "type": type}

@app.put("/arm")
async def toggle_arm(id):
    """Turns an arm on/off"""
    pass



@app.get("/sample")
async def sample_arm():
    pass



@app.put("/sample")
async def log_result():
    pass


@app.get("/stats")
async def stats():
    pass


@app.post("/client")
async def add_client():
    pass