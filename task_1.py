""" Homework """

import time
from threading import Thread


def create_file_with_delay(filename):
    """создаем тхт файлы"""
    time.sleep(1)
    with open(filename, 'w') as f:
        f.write("")


def run_without_multithreading():
    """запускаем код без многопоточности"""
    start_time = time.time()
    for i in range(100):
        create_file_with_delay(f"file_{i}.txt")
    end_time = time.time()
    print("Время выполнения без многопоточности:", end_time - start_time)


def run_with_multithreading():
    """запускаем с многопоточностью"""
    start_time = time.time()
    threads = []
    for i in range(100):
        thread = Thread(target=create_file_with_delay, args=(f"file_{i}.txt",))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()
    print("Время выполнения с многопоточностью:", end_time - start_time)


if __name__ == "__main__":
    run_without_multithreading()
    run_with_multithreading()
