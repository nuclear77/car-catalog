import multiprocessing
import time
from base import data


def search_x(start, end, result_queue):
    global data
    start_time = time.time()
    result = [char for char in data[start:end] if char == 'x']
    end_time = time.time()
    result_queue.put((len(result), end_time - start_time))


def main():
    result_queue = multiprocessing.Queue()
    processes = []

    chunk_size = len(data) // 4
    for i in range(4):
        start = i * chunk_size
        end = start + chunk_size if i < 3 else len(data)
        process = multiprocessing.Process(target=search_x, args=(start, end, result_queue))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    total_x_count = 0
    total_time = 0

    while not result_queue.empty():
        result = result_queue.get()
        total_x_count += result[0]
        total_time += result[1]

    print(f"Multiprocessing found {total_x_count} occurrences of 'x' in {total_time:.4f} seconds.")

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print(f"Total time: {end_time - start_time:.4f} seconds.")
