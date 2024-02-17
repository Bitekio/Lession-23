""" Homework """

import time
import random
from threading import Thread


def create_file_with_random_number(filename):
    """создаем файлы"""
    time.sleep(1)
    random_number = random.randint(1, 100)
    with open(filename, 'w') as f:
        f.write(str(random_number))


def run_without_multithreading():
    """запускаем без многопоточности"""
    start_time = time.time()
    for i in range(100):
        create_file_with_random_number(f"file_{i}.txt")
    end_time = time.time()
    print("Время выполнения без многопоточности:", end_time - start_time)


def run_with_multithreading():
    """запускаем с многопоточностью"""
    start_time = time.time()
    threads = []
    for i in range(100):
        thread = Thread(target=create_file_with_random_number, args=(f"file_{i}_from_task2.txt",))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()
    print("Время выполнения с многопоточностью:", end_time - start_time)


if __name__ == "__main__":
    run_without_multithreading()
    run_with_multithreading()
