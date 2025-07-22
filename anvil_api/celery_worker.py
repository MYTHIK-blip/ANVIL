from celery import Celery

# Configure Celery to use Redis as the broker
celery_app = Celery(
    "anvil_tasks",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0",
    include=["anvil_api.tasks.simulation_tasks"]
)

celery_app.conf.update(
    task_track_started=True,
)
