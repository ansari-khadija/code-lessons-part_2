# Regular Expressions (Quantifiers)

import re


# + → one or more occurrences
plus_text = "a aa aaa aaaa"
print(re.findall(r"a+", plus_text))


# * → zero or more occurrences
star_text = "a aa aaa"
print(re.findall(r"a*", star_text))


# ? → zero or one occurrence
question_text = "color colour"
print(re.findall(r"colou?r", question_text))


# {n} → exactly n occurrences
exact_text = "aa aaa aaaa"
print(re.findall(r"a{3}", exact_text))


# {n,} → n or more occurrences
minimum_text = "a aa aaa aaaa"
print(re.findall(r"a{3,}", minimum_text))


# {n,m} → between n and m occurrences
range_text = "a aa aaa aaaa aaaaa"
print(re.findall(r"a{2,4}", range_text))
