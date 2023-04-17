odd_nums = []

max_num = int(input("Enter a number: "))

for i in range(max_num):
    if i % 2 == 1:
        odd_nums.append(i)

print(odd_nums)