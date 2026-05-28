from fastapi import FastAPI
from worker import celery
from tasks import add_task


app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "AI Backend Running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/add/{a}/{b}")
def run_task(a: int, b: int):

    task = add_task.delay(a, b)

    return {
        "task_id": task.id,
        "message": "Task Submitted"
    }


@app.get("/result/{task_id}")
def get_result(task_id: str):

    task = celery.AsyncResult(task_id)

    response = {
        "task_id": task_id,
        "status": task.status
    }

    if task.successful():
        response["result"] = task.result
    else:
        response["result"] = None

    return response