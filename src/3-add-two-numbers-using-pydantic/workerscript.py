from pydantic import BaseModel
from typing import Any
from lilota.worker import LilotaWorker


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
        return {"sum": self.sum}


worker = LilotaWorker(
    db_url="postgresql+psycopg://postgres:postgres@localhost:5432/lilota_sample"
)


@worker.register("add", input_model=AddInput, output_model=AddOutput)
def add(data: AddInput) -> AddOutput:
    return AddOutput(sum=data.a + data.b)


def main():
    worker.start()


if __name__ == "__main__":
    main()
