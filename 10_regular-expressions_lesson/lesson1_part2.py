# Regular Expressions (Functions)

import re


# match() → checks for a match at the beginning of the string
match_text = "Python is easy"
match_result = re.match(r"Python", match_text)
print(match_result.group())


# fullmatch() → checks whether the entire string matches
fullmatch_text = "12345"
fullmatch_result = re.fullmatch(r"\d+", fullmatch_text)
print(fullmatch_result.group())


# sub() → replaces matched text
sub_text = "I like cats"
sub_result = re.sub(r"cats", "dogs", sub_text)
print(sub_result)


# subn() → replaces matched text and returns replacement count
subn_text = "cat cat cat"
subn_result = re.subn(r"cat", "dog", subn_text)
print(subn_result)


# split() → splits the string using a pattern
split_text = "apple,banana,orange"
split_result = re.split(r",", split_text)
print(split_result)


# compile() → creates a reusable regex pattern
compile_pattern = re.compile(r"\d+")
compile_text = "Age 25 and 30"
print(compile_pattern.findall(compile_text))


# search() → searches for the first match anywhere
search_text = "My age is 25"
search_result = re.search(r"\d+", search_text)
print(search_result.group())


# findall() → returns all matches as a list
findall_text = "I have 2 apples and 5 oranges"
findall_result = re.findall(r"\d+", findall_text)
print(findall_result)


# finditer() → returns an iterator containing all match objects
finditer_text = "I have 2 apples and 5 oranges"
finditer_result = re.finditer(r"\d+", finditer_text)

for item in finditer_result:
    print(item.group())
