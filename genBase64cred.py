import sys
import base64
from itertools import combinations
import time

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!?@%"
file = open("enumBase64Cred.txt","w")

def contains_max_three_digits(s):
    digit_count = sum(c.isdigit() for c in s)
    return digit_count <= 4

def contains_max_four_letters(s):
    letter_count = sum(c.isalpha() for c in s)
    return letter_count <= 5

def firsAndLasttNotLowCase(s):
    return not(s[0].islower()) and not(s[len(s)-1].islower())


def main(length):
    for combination in combinations(chars,length):
        combination = ''.join(combination)
        if(contains_max_three_digits(combination) and contains_max_four_letters(combination) and firsAndLasttNotLowCase(combination)):
            print(combination)
            payload = sys.argv[1] + ":" + combination
            #print(payload)
            bs64_payload = base64.b64encode(payload.encode()).decode()
            #print(bs64_payload)
            file.write(bs64_payload+"\n")
            time.sleep(0.001)
    file.close()




if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("""
This script will generate every possible length_given-length string and will encode each one as followed in base64 -> username:password
Usage: script.py username length_given
              """)
        sys.exit(0)
    else:
        main(int(sys.argv[2]))
