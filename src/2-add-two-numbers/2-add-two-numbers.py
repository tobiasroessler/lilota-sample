from dataclasses import dataclass
from lilota.core import Lilota
from lilota.models import Task
import time


@dataclass
class AddInput():
    a: int
    b: int


@dataclass
class AddOutput():
  sum: int


lilota = Lilota(
  db_url="postgresql+psycopg://postgres:postgres@localhost:5432/lilota_sample",
  script_path="src/2-add-two-numbers/2-worker-script.py"
)


def main():
  number1 = 2
  number2 = 3
  lilota.start()
  task_id = lilota.schedule("add", AddInput(a=number1, b=number2))
  time.sleep(3) # Wait that worker picks up the task (normally not needed)
  task: Task = lilota.get_task_by_id(task_id)
  add_output = AddOutput(**task.output)
  print(f"{number1} + {number2} = {add_output.sum} ") # 2 + 3 = 5


if __name__ == "__main__":
  try:
    main()
  finally:
    lilota.stop()