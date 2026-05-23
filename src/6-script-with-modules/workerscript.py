from calculator.models import AddInput, AddOutput
from lilota.worker import LilotaWorker
import calculator.core as calc_service


worker = LilotaWorker(
    db_url="postgresql+psycopg://postgres:postgres@localhost:5432/lilota_sample"
)


@worker.task
def add(data: AddInput) -> AddOutput:
    sum = calc_service.add(data.a, data.b)
    return AddOutput(sum=sum)


def main():
    worker.start()


if __name__ == "__main__":
    main()
