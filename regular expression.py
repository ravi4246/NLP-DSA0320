import re
text1 = "DSA-0316 Natural Language Processing"
text2 = "DSA-0314 Natural Language Processing"
word = "Natural Language Processing"
pattern = fr'\b{word}\b'
match1 = re.search(pattern, text1)
if match1:
    print("found the text")
else:
    print("not found in text")
match2 = re.search(pattern, text2)
if match2:
    print("found the text")
else:
    print("not found in text")
