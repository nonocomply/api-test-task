import os


def pytest_configure(config):
    # Устанавливаем текущую директорию на корень проекта (это позволит прописывать относительные пути к файлам)
    os.chdir(os.path.dirname(os.path.abspath(__file__)))


if __name__ == "__main__":
    pass
