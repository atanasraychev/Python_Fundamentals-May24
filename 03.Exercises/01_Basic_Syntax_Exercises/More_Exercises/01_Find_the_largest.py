number = int(input())

#converting the number to list of integers
number_string = str(number)
list_number = [int(x) for x in number_string]

# sorting the list of integers
list_number.sort(reverse = True)

# converting the list to one single string number
max_number_string = [str(i) for i in list_number] # list of integers to list of str (so we can use .join() )

max_number = "".join(max_number_string) #concat all elements of the list

# converting the string number to int number
result = int(max_number)
print(result)
