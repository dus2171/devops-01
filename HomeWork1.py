# function that calculates the Sum of the list

listValues = [4, 2, 7, 8, 9, 10, 2, 8, 6]
listSum = sum(listValues)
print(listSum)

# function that calculates the Average of the list

listLength = len(listValues)
listAverage = listSum / listLength
print(listAverage)

# function that counts the vowel letters (a,e,i,o,u) in a given string

count = 0
string = "Type a sentence and I will count the vowels!".lower()
for char in string:
    if char in 'aeiou':
        count += 1
print(count)

# program that receives Name of user and his age, then prints the Name and on which year he will reach the age of 120

name = input("What is your name: ")
age = int(input("How old are you: "))


def age120(age):

    turn = 120-age+2018
    return turn

turn = age120(age)

message = 'Hello %s, your age is %d and you will turn 120 in the year %d' % (name, age, turn)
print(message)