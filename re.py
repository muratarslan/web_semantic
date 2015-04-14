import re

def urlify(s):
     s = re.sub(r"[^\w\s]", '', s)
     s = re.sub(r"\s+", '_', s)
     return s.title()



# Prints: Elvis_Presley"
print urlify("elvis presley")
