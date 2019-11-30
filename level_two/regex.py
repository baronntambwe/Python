import re 

def multi_re_find(patterns, phrase):
    for pat in patterns:
        print("Searching for pattern {}".format(pat))
        print(re.findall(pat, phrase))
        print('/n')
    

test_phrase = "sddsd...sddsd....sddsd...sdddssddd....sdddsd...sddsddd"
test_pattern = ['sd*'] # 0 or more d
test_pattern = ['sd+'] # 1 or more d
test_pattern = ['sd?'] # 0 or 1 d
test_pattern = ['sd{4}'] # 4 d
test_pattern = ['sd{2,4}'] # 2 or 4 d
test_pattern = ['sd[sd]+'] # 1 or more s or d

test_pattern = ['[^!@&]+'] # Remove 1 or more !, @ and &

multi_re_find(test_pattern,test_phrase)