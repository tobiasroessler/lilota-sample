from lilota.core import Lilota
from lilota.models import Task, TaskProgress


lilota = Lilota(
  db_url="postgresql+psycopg://postgres:postgres@localhost:5432/lilota_sample",
  set_progress_manually=True
)

@lilota.register("do_something", task_progress=TaskProgress)
def do_something(task_progress: TaskProgress) -> None:
  for i in range(1, 101): # Start at 1 and ends with 100
    task_progress.set(i)


def main():
  lilota.start()
  task_id = lilota.schedule("do_something")
  lilota.stop()
  task: Task = lilota.get_task_by_id(task_id)
  print(task.progress_percentage) # Should be 100


if __name__ == "__main__":
  main()