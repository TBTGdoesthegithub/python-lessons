"""
--- DIRECTIONS ---

Hello there, please complete all of the questions. For each, solve the problem. 
In these, you might have to write the output of the code or write some code to solve a problem.
You can either write your solutions on a piece of paper or make a copy of this and write it on this file
Or, just answer the question
Good luck!

--- TOPICS ---

strings, special values, string replacements, lists, indexing

--- QUESTIONS ---
"""

# 1: Define each of these data types in one sentance, each:
	# - int
	# - float
	# - string
	# - boolean
	# - list
# Int is a number that doesn't have decimals
# Float is a number with decimals
# String is word with "" or '' surrounding them
# Boolean is a true/false statement
# List is a data type that holds more than 1 variables.
	
# 2: How can I fix this string declaration? 
fred = "How do dinosaurs pay their bills?
# fred = "How do dinosaurs pay their bills?"

# 3: Print the following using a multiline string:
"""
 ___
|[_]|
|+ ;|
`---'

"""
# print("""
#  ___
# |[_]|
# |+ ;|
# `---'
# """)

# 4: How can I fix this string declaration using the escape character ("\")?
silly_string = 'He said, "Aren't can't shouldn't wouldn't."'
# silly_string = 'He said, \"Aren\'t can\'t shouldn\'t wouldn\'t.'

# 5: How can I fix this string declaration using a multiline string?
silly_string = 'He said, "Aren't can't shouldn't wouldn't."'
# silly_string = '''He said, "Aren't can't shouldn't wouldn't"'''

# 6: Write a variable called "fav" that will store the following string:
Andrew said, "Python is the best programing lanuage! Isn't it great?"
# fav = 'Andrew said, "Python is the best programing lanuage! Isn\'t it great?\"'

# 7: What is the output of the following code?
fav = '%s is the best programming language!'
python = "python"
java = "java"
print(fav % python)
print(fav & java)
# python is the best programming language!
# java is the best programming language!

# 8: What is the output of the following code?
fav = '%s and %s are the best programming languages!'
c = "C"
cpp = "C++"
print(fav & (cpp, c))
# C++ and C are the best programming languages!

# 9: What is the ouput of the following code: (WARNING: this one is kinda hard --take your time!)
t = "e"
f = "pass%sd"
s = f % t
x = "yo%s"
z = "u "
m = x % z
k = "!"
print(m + s + k)
# you passed!

# 10: What is the output of the following code (think about it):
print("Hello\no" * 3)
# Hello
# oHello
# oHello
# o

# 11: What is the index of 'c'
langs = ['lisp', 'cpp', 'c', 'java']
# 2

# 12: What is the output of this code:
cypher = ['k', ' ', 'r', 'c', 'w', 'd', '!', 'o', 's', 'n', 'e', 'a', '!']
print(cypher[11] + cypher[9] + cypher[5] + cypher[2] + cypher[10] + cypher[4] + cypher[1] + cypher[2] + cypher[7] + cypher[3] + cypher[0] + cypher[8] + cypher[12])
# andrew rocks
