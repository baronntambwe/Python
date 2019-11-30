import re 

def multi_re_find(patterns, phrase):
    for pat in patterns:
        print("Searching for pattern {}".format(pat))
        print(re.findall(pat, phrase))
        print('/n')
    

test_phrase = "sddsd...sddsd....sddsd...sdddssddd....sdddsd...sddsddd"
test_pattern = ['sd*']

multi_re_find(test_pattern,test_phrase)