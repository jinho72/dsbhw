# 1.⁠ ⁠Display Fibonacci Series upto 10 terms

def fibonacci(n):
    fib_series = [0,1]
    for i in range(2, n):
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series


# 2.⁠ ⁠Display numbers at the odd indices of a list

list = [1,2,3,4,5,6,7,8,9]

for i in range(1, len(list), 2):
    print(list[i])




# 3.⁠ ⁠⁠string = """


#I have provided this text to provide tips on creating interesting paragraphs.

#First, start with a clear topic sentence that introduces the main idea.

#Then, support the topic sentence with specific details, examples, and evidence.
#
#Vary the sentence length and structure to keep the reader engaged.

#Finally, end with a strong concluding sentence that summarizes the main points.

#Remember, practice makes perfect!



#Your task is to count the number of different words in this text

all_words = []

string = "First, start with a clear topic sentence that introduces the main idea. Then, support the topic sentence with specific details, examples, and evidence.Vary the sentence length and structure to keep the reader engaged. Finally, end with a strong concluding sentence that summarizes the main points. Remember, practice makes perfect!"

for wor in string:
    if wor == " ":
    
    else:







#4.⁠ ⁠Write a function count_vowels(word) that takes a word as an argument and returns the number of vowels in the word

def count_vowels(word):
    vowels = "aeiouAEIOU"
    total_vowels = 0
    for alpha in word:
        if alpha in vowels:
            total_vowels += 1

    return total_vowels

word = "interestingEvent"
print(count_vowels(word))



#5.⁠ ⁠Iterate through the following list of animals and print each one in all caps.

#animals=['tiger', 'elephant', 'monkey', 'zebra', 'panther']

animals=['tiger', 'elephant', 'monkey', 'zebra', 'panther']

for ani in animals:
    print(ani.upper())



#6.⁠ ⁠Write a program that iterates from 1 to 20, printing each number and whether it's odd or even.


for i in range(1, 21):
    if i % 2 == 0:
        print(i, "even")
    else
        print(i, "odd")





#7.⁠ ⁠Write a function sum_of_integers(a, b) that takes two integers as input from the user and returns their sum.

def sum_of_integers(a,b):
    return a+b

print(sum_of_integers(34,3))




















