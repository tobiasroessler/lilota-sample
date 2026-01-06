from lilota.core import Lilota
from lilota.models import Task
import os
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base


# A simple db with one table for testing
Base = declarative_base()
DB_FILE = os.path.join(os.path.dirname(__file__), "test-4.db")
DB_URL = f"sqlite:///{DB_FILE}"

class TestTable(Base):
  __tablename__ = "test_table"
  id = Column(Integer, primary_key=True)
  value = Column(String)


lilota = Lilota(db_url="postgresql+psycopg://postgres:postgres@localhost:5432/lilota_sample")

@lilota.register("safe_db_task", input_model=dict[str, str], output_model=dict[str, int])
def safe_db_task(params: dict[str, str]) -> dict[str, int]:
  """
  Create engine & session inside the task.
  Insert a value into the table and return row count.
  """
  engine = create_engine(DB_URL, echo=False)
  Session = sessionmaker(bind=engine)
  session = Session()

  try:
    # Create table (in-memory, per process)
    Base.metadata.create_all(engine)

    # Insert a row
    row = TestTable(value=params["value"])
    session.add(row)
    session.commit()

    # Count rows
    count = session.query(TestTable).count()
    return {
      "count": count
    }
  finally:
    session.close()
    engine.dispose()


def main():
  lilota.start()
  task_id = lilota.schedule("safe_db_task", { "value": "123" })
  lilota.stop()
  task: Task = lilota.get_task_by_id(task_id)
  print(task.output)


if __name__ == "__main__":
  main()