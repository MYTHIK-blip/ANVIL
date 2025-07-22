from fastapi import APIRouter, BackgroundTasks
from ..tasks import simulation_tasks

router = APIRouter()

@router.post("/simulations/start")
async def start_simulation(background_tasks: BackgroundTasks):
    # This endpoint immediately returns a task ID
    # The actual simulation runs in the background via Celery
    task = simulation_tasks.run_forge_simulation.delay()
    return {"message": "Forge simulation started.", "task_id": task.id}
