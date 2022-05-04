#Remove SPSS from input_list=['SAS', 'R', 'PYTHON', 'SPSS'] and add 'SPARK' in its place.
input_list =  ['SAS', 'R', 'PYTHON', 'SPSS']
input_list[-1]='SPARK'
print(input_list);

# output: ['SAS', 'R', 'PYTHON', 'SPARK']

# Description: Convert a string input_str = 'I love Data Science & Python' to a list by splitting it on ‘&’.
input_str = 'I love Data Science & Python'
print(input_str.split('&'));
# output: ['I love Data Science ', ' Python']

#Description: Convert a list ['Pythons syntax is easy to learn', 'Pythons syntax is very clear'] to a string using ‘&’. The
list1= ['Pythons syntax is easy to learn', 'Pythons syntax is very clear']
str_out = list1[0]+' & '+list1[-1]
print(str_out);
# output: Pythons syntax is easy to learn & Pythons syntax is very clear

# Description: Extract Python from a nested list input_list = [['SAS','R'],['Tableau','SQL'],['Python','Java']]
input_list = [['SAS','R'],['Tableau','SQL'],['Python','Java']]
print(input_list[2][0]);
#output: Python

# Description: Write a program to check whether a string is a palindrome or not. Print 1 if the string is a palindrome and 0 otherwise.
input_str = input(str("String: "))
str_formatted = input_str.lower()
if str_formatted == str_formatted[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")
#output : String: malayalam ---> Palindrome

#Description: Write a program that satisfies below examples
#Input 1: caloRie ConsuMed
#Output 1: calorie_consumed
#Input 2: 1
#Output 2: data_science
#Input 3: datascience
#Output 3: datascience

check_str = input(str("Enter String: "))
def string_formatter(check_str):
    formatted_str = check_str.lower().replace(" ","_")
    print(formatted_str)
string_formatter(check_str)

#output: Enter String: data science ---> data_science