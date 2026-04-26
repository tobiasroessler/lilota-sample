from dataclasses import dataclass
from lilota.worker import LilotaWorker


@dataclass
class AddInput():
    a: int
    b: int


@dataclass
class AddOutput():
  sum: int


worker = LilotaWorker(db_url="postgresql+psycopg://postgres:postgres@localhost:5432/lilota_sample")


@worker.register("add", input_model=AddInput, output_model=AddOutput)
def add(data: AddInput) -> AddOutput:
  return AddOutput(sum=data.a + data.b)


def main():
  worker.start()


if __name__ == "__main__":
  main()