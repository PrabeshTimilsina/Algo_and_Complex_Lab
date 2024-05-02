import random
import time
import matplotlib.pyplot as plt
from selection import selection_sort
from insertion import insertion_sort

def rand_num(n):
    return [random.randint(0, n) for _ in range(n)]

def sorted_num(n):
    return sorted(rand_num(n))

def rev_sorted_num(n):
    return sorted(rand_num(n), reverse=True)

def total_time(algorithm, size):
    time_taken = []
    for size in size:
        data = rev_sorted_num(size)
        start_time = time.time()
        algorithm(data)
        end_time = time.time()
        sorting_time = end_time - start_time
        time_taken.append(sorting_time)
    return time_taken

def plot_graph(size, selection, insertion):
    plt.plot(size, selection, marker='o', linestyle='-', label='Selection Sort')
    plt.plot(size, insertion, marker='o', linestyle='-', label='Insertion Sort')
    plt.title('Sorting Algorithms Comparison: reverse sorted elements')
    plt.xlabel('Number of Data')
    plt.ylabel('Time in Seconds')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    size = [1000, 2500, 5000, 7500, 10000, 12500, 15000, 17500, 20000, 22500, 25000, 27500, 30000]
    
    selection = total_time(selection_sort, size)
    insertion = total_time(insertion_sort, size)
    
    plot_graph(size, selection, insertion)
