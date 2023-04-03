
current_sugar_level = int(input('Enter your current sugar level : '))

if current_sugar_level >= 80 and current_sugar_level <= 100:
    print('Your sugar level is in normal range')
elif current_sugar_level < 80:
    print('Your sugar level is low')
elif current_sugar_level > 100:
    print('Your sugar level is high')
else :
    print('Enter a valid input!!!')
