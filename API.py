import requests
import json
import concurrent.futures
import time

def store_info(ls, x):
    with open("data.json", "a") as file:
        for i in range(20):
            response = requests.get(ls[x][i])
            response = response.json()
            json.dump(response, file, indent=4)
            file.write('\n')


def division():
    ls_threads = []
    ls_products = []
    for i in range(1, 101):
        product = f"https://dummyjson.com/products/{i}"
        ls_products.append(product)

    for i in range(0, 100, 20):
        x = ls_products[i:i+20]
        ls_threads.append(x)

    return ls_threads


def thread_pool(ls_threads):
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as pool:
        pool.submit(store_info, ls_threads, 0)
        pool.submit(store_info, ls_threads, 1)
        pool.submit(store_info, ls_threads, 2)
        pool.submit(store_info, ls_threads, 3)
        pool.submit(store_info, ls_threads, 4)



if __name__ == '__main__':
    tm = time.perf_counter()
    ls_threads = division()
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as proces:
        proces.submit(thread_pool, ls_threads)

    en = time.perf_counter()
    print(en-tm)