from lilota.worker import LilotaWorker
from lilota.models import TaskContext


worker = LilotaWorker(
    db_url="postgresql+psycopg://postgres:postgres@localhost:5432/lilota_sample"
)


@worker.task
def do_something(task_context: TaskContext) -> None:
    for i in range(1, 101):  # Start at 1 and ends with 100
        task_context.progress.set(i)


def main():
    worker.start()


if __name__ == "__main__":
    main()
