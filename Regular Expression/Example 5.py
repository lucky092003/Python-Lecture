import re 
pattern = r"hllo"
text = "hello"
match = re.search(pattern , text)
print("Match found:", match.group() if match else "No match")