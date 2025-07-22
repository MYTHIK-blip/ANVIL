import time
from ..celery_worker import celery_app

@celery_app.task
def run_forge_simulation():
    """A placeholder for a long-running Forge simulation."""
    print("Starting a complex simulation...")
    time.sleep(60)  # Simulate a 1-minute task
    print("Simulation finished.")
    return {"result": "Simulation completed successfully."}
