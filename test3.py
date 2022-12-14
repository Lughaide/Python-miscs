from multiprocessing import Pool, Array, cpu_count
from random import randrange

arr = Array('i', range(10))
max_cores = cpu_count()

def dev_info():
    print(f"Max number of cores: {max_cores}")
    print(f"Initial array: {arr[:]}")
    print(f"Indexes: {[i for i in range(len(arr))]}")

dev_info()

def shuffle():
    indexes_list = []

    with Pool() as worker_pool:
        worker_pool.starmap(swap_elements, indexes_list)
    
def swap_elements(x, y):
    global arr
    arr[x], arr[y] = arr[y], arr[x]

def get_indexes():
    for x in range(len(arr) - 1, 0, -1):
        y = randrange(x + 1)
        yield (x, y)

def knux_shuffle():
    global arr
    for x in range(len(arr) - 1, 0, -1):
        y = randrange(x + 1)
        arr[x], arr[y] = arr[y], arr[x]

knux_shuffle()
print(arr[:])
x = get_indexes()
for i in range(max_cores*2):
    print(next(x))