from calculator.models import AddInput, AddOutput
from lilota.core import Lilota
from lilota.models import Task
from pathlib import Path
import time


lilota = Lilota(
    db_url="postgresql+psycopg://postgres:postgres@localhost:5432/lilota_sample",
    script_path=str(Path(__file__).resolve().parent / "workerscript.py"),
)


def main():
    number1 = 2
    number2 = 3
    lilota.start()
    task_id = lilota.schedule("add", AddInput(a=number1, b=number2))
    time.sleep(5)  # Wait that worker picks up the task (normally not needed)
    task: Task = lilota.get_task_by_id(task_id)
    add_output = AddOutput(**task.output)
    print(f"{number1} + {number2} = {add_output.sum} ")  # 2 + 3 = 5


# if __name__ == "__main__":
try:
    main()
finally:
    lilota.stop()
