from pydantic import BaseModel
from typing import Any
from lilota.core import Lilota
from lilota.models import Task


class AddInput(BaseModel):
  a: int
  b: int

  def as_dict(self) -> dict[str, Any]:
    return {
      "a": self.a,
      "b": self.b,
    }


class AddOutput(BaseModel):
  sum: int

  def as_dict(self) -> dict[str, Any]:
    return {
      "sum": self.sum
    }


lilota = Lilota(db_url="postgresql+psycopg://postgres:postgres@localhost:5432/lilota_sample")

@lilota.register("add", input_model=AddInput, output_model=AddOutput)
def add(data: AddInput) -> AddOutput:
  return AddOutput(sum=data.a + data.b)


def main():
  number1 = 2
  number2 = 3
  lilota.start()
  task_id = lilota.schedule("add", AddInput(a=number1, b=number2))
  lilota.stop()
  task: Task = lilota.get_task_by_id(task_id)
  add_output = AddOutput(**task.output)
  print(f"{number1} + {number2} = {add_output.sum} ") # 2 + 3 = 5


if __name__ == "__main__":
  main()