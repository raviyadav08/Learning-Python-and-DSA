def isPrime(num):
    i = 2
    flag = 0

    while i < num:
        if num % i == 0:
            flag = 1
        
        i = i+1

    if flag == 0:
        print(num, ' is a prime number')
    else:
        print(num,' is not a prime number')

num = int(input('Enter a number : '))
isPrime(num)
