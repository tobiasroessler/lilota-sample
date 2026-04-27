from lilota.worker import LilotaWorker


worker = LilotaWorker(db_url="postgresql+psycopg://postgres:postgres@localhost:5432/lilota_sample")


@worker.register("hello-world")
def hello_world() -> None:
  print("Hello World")


def main():
  worker.start()


if __name__ == "__main__":
  main()