import time
import multiprocessing


def calculate_square(numbers,result):
    for idx , n in enumerate(numbers):
        print(f"Square: {n**2}")
        result[idx] = n**2
        
    print('Inside the process: ',result[:])

def calculate_cube(numbers,result):
    for idx , n in enumerate(numbers):
        print(f"Cube: {n**3}")
        result[idx] = n**3
    print('Inside the process: ',result[:])


if __name__ == "__main__":
    
    arr = [1,2,3,4,5,6]

    square_result = multiprocessing.Array('i',len(arr))
    cube_result = multiprocessing.Array('i',len(arr))
    # print('Length of array: ',len(arr))

    p1 = multiprocessing.Process(target=calculate_square,args=(arr,square_result))
    p2 = multiprocessing.Process(target=calculate_cube,args=(arr,cube_result))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('\nOutside the process Squrare result: ',square_result[:])
    print('Outside the process cube result: ',cube_result[:])

    print("Done!")