from lilota.core import Lilota
from lilota.models import Task


lilota = Lilota(name="Default", db_url="postgresql+psycopg://postgres:postgres@localhost:5432/lilota_sample")


@lilota.register("hello-world")
def hello_world() -> None:
  print("Hello World")


def main():
  lilota.start()
  task_id = lilota.schedule("hello-world")
  lilota.stop()
  task: Task = lilota.get_task_by_id(task_id)
  print(task)


if __name__ == "__main__":
  main()