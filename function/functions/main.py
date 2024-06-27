from firebase_functions import scheduler_fn
from firebase_admin import initialize_app
import requests

initialize_app()


@scheduler_fn.on_schedule(schedule="0 14 * * *")
def job_application(event: scheduler_fn.ScheduledEvent) -> None:
    print("Job application started")

    requests.get("https://flask-job-apply-oqfwxo66fa-uc.a.run.app")

    print("Job application finished")
