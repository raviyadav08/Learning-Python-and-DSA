from multiprocessing import Pool
import time

def f(num):
    sum = 0
    for x in range(num):
        sum = x*x
    return sum

if __name__ == "__main__":

    t1 = time.time()
    p = Pool()
    result = p.map(f,range(20000))
    p.close()
    p.join()

    print(f"Pool processing took: {time.time()-t1} ")


    t2 = time.time()
    sum = 0
    result = []
    for i in range(20000):
        result.append(f(i))

    print(f'Serial processing took: {time.time()-t2}')