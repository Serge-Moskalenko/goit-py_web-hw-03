import time
from multiprocessing import Pool, cpu_count


def factorize(*numbers):
    result = []
    for number in numbers:
        factors = []
        for i in range(1, number + 1):
            if number % i == 0:
                factors.append(i)
        result.append(factors)
    return result


def process_factors(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors


def process_factorize(*numbers):
    with Pool(cpu_count()) as pool:
        result = pool.map(process_factors, numbers)

    return result


if __name__ == "__main__":

    a, b, c, d = factorize(128, 255, 99999, 10651060)
    a, b, c, d = process_factorize(128, 255, 99999, 10651060)

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [
        1,
        2,
        4,
        5,
        7,
        10,
        14,
        20,
        28,
        35,
        70,
        140,
        76079,
        152158,
        304316,
        380395,
        532553,
        760790,
        1065106,
        1521580,
        2130212,
        2662765,
        5325530,
        10651060,
    ]

    start_time = time.time()
    factorize(128, 255, 99999, 10651060)
    end_time = time.time()
    print(f"1 Process {end_time - start_time:.4f} seconds")
    start_time = time.time()
    process_factorize(128, 255, 99999, 10651060)
    end_time = time.time()
    print(f"20 Process {end_time - start_time:.4f} seconds")
