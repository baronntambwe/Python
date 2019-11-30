import re 

def multi_re_find(patterns, phrase):
    for pat in patterns:
        print("Searching for pattern {}".format(pat))
        print(re.findall(pat, phrase))
        print('/n')
    

test_phrase = "sddsd...sddsd....sddsd...sdddssddd....sdddsd...sddsddd"

# Selection
test_pattern = ['sd*'] # 0 or more d
test_pattern = ['sd+'] # 1 or more d
test_pattern = ['sd?'] # 0 or 1 d
test_pattern = ['sd{4}'] # 4 d
test_pattern = ['sd{2,4}'] # 2 or 4 d
test_pattern = ['sd[sd]+'] # 1 or more s or d
test_pattern = ['[a-z]+'] # Siquence of lower case characters
test_pattern = ['[A-Z]+'] # Siquence of upper case characters

# Removal
test_pattern = ['[^!@&]+'] # Remove 1 or more !, @ and &

# Escape
test_pattern = [r'\d+'] # Return all digits
test_pattern = [r'\D+'] # Return all non-digits
test_pattern = [r'\s+'] # Return all white spaces
test_pattern = [r'\S+'] # Return all non-white spaces
test_pattern = [r'\w+'] # Return all alphanumeric spaces
test_pattern = [r'\W+'] # Return all non-alphanumeric spaces


multi_re_find(test_pattern,test_phrase)