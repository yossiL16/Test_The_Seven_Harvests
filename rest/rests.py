from fastapi import FastAPI, HTTPException
from uvicorn import *
from control_system.queries import get_db_for_order

app = FastAPI()

@app.get('/on_hold')
def get_num_on_hold():
    received, on_hold = get_db_for_order()
    return {'len of on_hold':len(on_hold)}

@app.get('/received')
def get_num_of_received():
    received, on_hold = get_db_for_order()
    return {'len of received':len(received)}


