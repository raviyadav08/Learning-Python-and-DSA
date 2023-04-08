"""
Exercise: Multithreading
Create any multithreaded code using for loop for creating multithreads
for i in range(10):
    th = Thread(target=func_name, args=(i, ))
    
print total active threads in multithreaded code using 
threading.active_count()
"""
import time
import threading

def calculate_square(numbers):
    for i in numbers:
        time.sleep(0.2)
        print(f'square of num {i} = {i**2}')

def calculate_cube(numbers):
    for i in numbers:
        time.sleep(0.2)
        print(f'cube of num {i} = {i**3}')

arr = [2,3,4,5]

st = time.time()

t1 = threading.Thread(target=calculate_square,args=(arr,))
t2 = threading.Thread(target=calculate_cube,args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()

print(f"Time taken to process the executions : {time.time()-st}")


