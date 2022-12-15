from poolshuffle import *

today = date.today()
logging.basicConfig(filename=f"test_result_{today.strftime('%b_%d')}.log", format='%(asctime)s - %(message)s', level=logging.INFO, filemode="w")
max_cores = cpu_count()
arr = Array('i', range(10))
# def init_worker():
#     global goal
#     global arr
#     goal = 10
    


def dev_info():
    print(f"Max number of cores: {max_cores}")
    print(f"Initial array: {arr[:]}")
    print(f"Indexes: {[i for i in range(len(arr))]}")


# def shuffle():
#     base_idx = list(range(len(shared_arr)))
#     uniq_idx = create_unique_pairs(base_idx, max_cores)
#     print(uniq_idx)
#     with Pool() as worker_pool:
#         worker_pool.starmap(swap_elements, uniq_idx)

def create_unique_pairs(base_idx, max_cores):
    uniq_idx = []
    for _ in range(max_cores):
        if len(base_idx) > 1 and len(uniq_idx) < max_cores:
            x = base_idx.pop(random.randrange(len(base_idx)))
            y = base_idx.pop(random.randrange(len(base_idx)))
            uniq_idx.append((x, y))
        else:
            break
    return uniq_idx

# def swap_elements(x, y):
#     shared_arr[x], shared_arr[y] = shared_arr[y], shared_arr[x]


def get_indexes(arr_len, y_only=False):
    res = []
    res2 = []
    for x in range(arr_len - 1, -1, -1):
        y = random.randrange(x + 1)
        res.append((x, y))
        res2.append(y)
    logging.info(f"Generated indexes list: {res}")
    return res if not y_only else res2

def knuth_shuffle():
    global arr
    idx_list = get_indexes(len(arr))
    print(len(idx_list))
    for x, y in idx_list:
        arr[x], arr[y] = arr[y], arr[x]
    print("H = ", idx_list)


if __name__ == "__main__":
    # Knuth sequential shuffle
    random.seed(42)
    knuth_shuffle()
    print(arr[:])

    # with Manager() as manager:
    #     arr_in = Array('i', range(10))
    #     # Random parallel shuffle
    #     print(arr[:])
    #     random.seed(42)
    #     shuffle(arr_in)
    #     print(arr[:])