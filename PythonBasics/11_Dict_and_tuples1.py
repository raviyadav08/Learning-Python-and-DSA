"""
We have the following information on countries and their population (population is in crores),

Country	Population
China	143
India	136
USA	32
Pakistan	21

Using above create a dictionary of countries and its population
Write a program that asks user for three type of inputs,
print: if user enter print then it should print all countries with their population in this format,
china==>143
india==>136
usa==>32
pakistan==>21

add: if user input add then it should further ask for a country name to add. If country already exist in our dataset
then it should print that it exist and do nothing. If it doesn't then it asks for population and add that new
country/population in our dictionary and print it

remove: when user inputs remove it should ask for a country to remove. If country exist in our dictionary then remove it
and print new dictionary using format shown above in (a). Else print that country doesn't exist!

query: on this again ask user for which country he or she wants to query. When user inputs that country it will print
population of that country.
"""

countries = {"China": 143, "India": 136, "USA": 32, "Pakistan": 21}
# print('1.Print all the country details \n2.Add a country \n3.Remove a country \n4.Query a country details')

while exit:
    print('\nCommands :')
    print("1.Enter 'print' to print all the details of countries from dictionary")
    print("2.Enter 'add' to add a new country in dictionary")
    print("3.Enter 'remove' to remove a country from the list")
    print("4.Enter 'query' to query details of a particular country")
    print("5.Enter 'exit' to quit.")

    user_input1 = str(input('\nEnter your Input : '))

    if user_input1 == 'exit':
        exit()

    elif user_input1 == 'print':
        print('')
        for key, value in countries.items():
            print(f"{key} ==> {value}")

    elif user_input1 == 'add':
        country_input = str(input("Enter country name to be added : "))
        if country_input in countries:
            print('\nCountry already exist in dictionary!!!')
        else:
            population_input = int(input("Enter the population of the said country : "))
            countries[country_input] = population_input
            print('\nNew country added to the dictionary')

    elif user_input1 == 'remove':
        remove_input = str(input("Enter the name of the country to be removed : "))
        if remove_input in countries:
            del countries[remove_input]
            for key, value in countries.items():
                print(f"{key} ==> {value}")
        else:
            print("\nThe country does not exist in dictionary!!!")

    elif user_input1 == 'query':
        input_query = str(input("Enter the name of the company that you want to query : "))
        if input_query in countries:
            print(f'Population : {countries[input_query]}')
        else:
            print("Country does not exist in dictionary!")

    else:
        print("\nPlease enter a valid Command!!!")
