import re

pattern = re.compile(r"\d+")
text = "123 apples, 456 bananas"
match = pattern.findall(text)
print("Matches:", match)