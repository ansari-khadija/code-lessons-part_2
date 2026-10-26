# Regular Expressions (Symbols)

import re

# \d → matches any digit (0-9)
digit_text = "abc123"
print(re.findall(r"\d", digit_text))


# \w → matches letters, numbers, and underscore (_)
word_text = "Hi_123!"
print(re.findall(r"\w", word_text))


# \s → matches whitespace
space_text = "Hello World"
print(re.findall(r"\s", space_text))


# . → matches any one character
dot_text = "cat"
print(re.findall(r"c.t", dot_text))


# ^ → matches the beginning of a string
start_text = "Python"
print(re.findall(r"^P", start_text))


# $ → matches the end of a string
end_text = "Hello Python"
print(re.findall(r"Python$", end_text))


# + → matches one or more occurrences
plus_text = "a aa aaa"
print(re.findall(r"a+", plus_text))


# * → matches zero or more occurrences
star_text = "a aa aaa"
print(re.findall(r"a*", star_text))


# ? → matches zero or one occurrence
question_text = "color colour"
print(re.findall(r"colou?r", question_text))


# [abc] → matches either a, b, or c
bracket_text = "apple ball cat dog"
print(re.findall(r"[abc]", bracket_text))
