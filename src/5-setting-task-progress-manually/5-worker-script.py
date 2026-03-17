from lilota.worker import LilotaWorker
from lilota.models import TaskProgress


worker = LilotaWorker(
  db_url="postgresql+psycopg://postgres:postgres@localhost:5432/lilota_sample",
  set_progress_manually=True
)


@worker.register("do_something", task_progress=TaskProgress)
def do_something(task_progress: TaskProgress) -> None:
  for i in range(1, 101): # Start at 1 and ends with 100
    task_progress.set(i)


def main():
  worker.start()


if __name__ == "__main__":
  main()