from lilota.core import Lilota
from lilota.models import Task
import os
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
import time


# A simple db with one table for testing
Base = declarative_base()
DB_FILE = os.path.join(os.path.dirname(__file__), "test-4.db")
DB_URL = f"sqlite:///{DB_FILE}"

class TestTable(Base):
  __tablename__ = "test_table"
  id = Column(Integer, primary_key=True)
  value = Column(String)


lilota = Lilota(
  db_url="postgresql+psycopg://postgres:postgres@localhost:5432/lilota_sample",
  script_path="src/4-using-db-inside-task/4-worker-script.py"
)


def main():
  lilota.start()
  task_id = lilota.schedule("safe_db_task", { "value": "123" })
  time.sleep(3) # Wait that worker picks up the task (normally not needed)
  task: Task = lilota.get_task_by_id(task_id)
  print(task.output)


if __name__ == "__main__":
  main()