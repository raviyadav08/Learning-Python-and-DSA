import time
import multiprocessing

square = []
cube = []

def calculate_square(numbers):
    global square
    for i in numbers:
        time.sleep(5)
        print(f"Square: {i**2}")
        square.append(i**2)
    print(square)

def calculate_cube(numbers):
    global cube
    for i in numbers:
        time.sleep(5)
        print(f"Cube: {i**3}")
        cube.append(i**3)
    print(cube)


if __name__ == "__main__":
    arr = [1,2,3,4,5,6]

    p1 = multiprocessing.Process(target=calculate_square,args=(arr,))
    p2 = multiprocessing.Process(target=calculate_cube,args=(arr,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Done!")