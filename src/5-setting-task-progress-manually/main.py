from lilota.core import Lilota
from lilota.models import Task
from pathlib import Path
import time


lilota = Lilota(
    db_url="postgresql+psycopg://postgres:postgres@localhost:5432/lilota_sample",
    script_path=str(Path(__file__).resolve().parent / "workerscript.py"),
)


def main():
    lilota.start()
    task_id = lilota.schedule("do_something")
    time.sleep(3)  # Wait that worker picks up the task (normally not needed)
    task: Task = lilota.get_task_by_id(task_id)
    print(task.progress_percentage)  # Should be 100


if __name__ == "__main__":
    try:
        main()
    finally:
        lilota.stop()
