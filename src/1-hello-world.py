from lilota.core import Lilota
from lilota.models import Task
import time


lilota = Lilota(db_url="postgresql+psycopg://postgres:postgres@localhost:5432/lilota_sample")

@lilota.register("hello-world")
def hello_world() -> None:
  print("Hello World")


def main():
  lilota.start()
  task_id = lilota.schedule("hello-world")
  time.sleep(1) # Wait that worker picks up the task (normally not needed)
  task: Task = lilota.get_task_by_id(task_id)
  print(task)


if __name__ == "__main__":
  main()