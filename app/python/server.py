#!/usr/bin/env python3
from datetime import datetime
from logging import Logger, getLogger
from modules.heavy_task import HeavyTask
from fastapi import FastAPI, BackgroundTasks
from starlette.middleware.cors import CORSMiddleware

""" execute commands
[debug]
$ uvicorn server:app --host 0.0.0.0 --port 3000 --reload
"""

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

@app.get("/api/hello")
def index():
    return {"message": "Hello World"}

task:HeavyTask = HeavyTask(10)

@app.get("/api/background-task")
def fetch_background_task():
    print(f'{datetime.now()} get status -> {task.get_status()}')
    return {"status": task.get_status()}

@app.post("/api/background-task")
def execute_background_task(background_tasks: BackgroundTasks):
    try:
        print(f'{datetime.now()} execute background task.')
        background_tasks.add_task(task)
    except Exception as e:
        print(e)
        return {"message": f"error occured. reason: {e}"}
    return {"message": "ok"}

