# import json
# import threading
#
#
# def read_file(file_name):
#     with open(file_name, 'r') as file:
#         new_file = json.load(file)
#         print(f"{file_name}: {new_file}")
#
#
# first = threading.Thread(target=read_file("file1.json"))
# second = threading.Thread(target=read_file(file_name="file2.json"))
# third = threading.Thread(target=read_file(file_name="file3.json"))
#
# first.start()
# second.start()
# third.start()
#
# first.join()
# second.join()
# third.join()


# Exercise N2

import queue
import threading
import time


def process_queue(q, thread_name):
    while not q.empty():
        number = q.get()
        if number % 2 == 0:
            is_even = True
        else:
            is_even = False
        print(f"{thread_name} : {number} : {is_even}")
        q.task_done()


def main():
    q = queue.Queue()

    threads = []
    for i in range(3):
        thread = threading.Thread(target=process_queue, args=(q, f"Thread-{i + 1}"))
        threads.append(thread)
        thread.start()

    for num in range(10):
        q.put(num)

    for thread in threads:
        thread.join()

    print("All Done")


if __name__ == "__main__":
    main()
