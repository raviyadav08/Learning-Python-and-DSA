import os

os.chdir('C:/Users/iamsu/Desktop/Ravi Files/Certificates')

num = 0
for file in os.listdir():
    
    num = num+1
    
    file_name , file_ext = os.path.splitext(file)
    
    file_num , file_new_name = (file_name.split(f'{num}'))

    new_name = f'{file_new_name}{file_ext}'

    os.rename(file , new_name)

    

    