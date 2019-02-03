import re

paragraph='hey i'm here to know who the hell are you'

result=re.findall('[A-Z]',paragraph)

print(result)
