from lilota.core import Lilota
from lilota.scheduler import LilotaScheduler
from lilota.models import Task
from pathlib import Path
import time


scheduler: LilotaScheduler = Lilota.scheduler(
  db_url="postgresql+psycopg://postgres:postgres@localhost:5432/lilota_sample"
)

workers = Lilota.workers(
  db_url="postgresql+psycopg://postgres:postgres@localhost:5432/lilota_sample",
  script_path=str(Path(__file__).resolve().parent / "workerscript.py"),
  number_of_workers=1
)


def main():
  scheduler.start()
  workers.start()
  task_id = scheduler.schedule("hello-world")
  time.sleep(3) # Wait that worker picks up the task (normally not needed)
  task: Task = scheduler.get_task_by_id(task_id)
  print(task)


if __name__ == "__main__":
  try:
    main()
  finally:
    scheduler.stop()
    workers.stop()