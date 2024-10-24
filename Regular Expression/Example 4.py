import re 
pattern = r"h.llo"
text = "hello"
match = re.search(pattern , text)
print("Match found:", match.group() if match else "No match")