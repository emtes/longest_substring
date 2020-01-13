'''
P:
find the length of a string's largest substring without repeating chars
-- how long is a substring we can pull without any repeating chars in a given string?
INPUT: string
OUTPUT: int

E:
in: 'abcjsfl' out: 7 // all unique
in: 'pwwkew' out: 3 // wke length of 3

D:
strings should do, maybe sets later

A:
-declare empty string
-declare a current_max_length variable
-for the characters of inStr
    - check if they're already in emptyStr ?
    y: make current_max_length length of what emptyStr is now
        IF its larger than the amount it already was
        clear empty string, add current str
    n: add current char
- return current_max_length

'''
def longest_substring(string):
    stage = ''
    current_length = 0
    max_length = 0
    for char in string:
        if char in stage:
            current_length = len(stage)
            if current_length > max_length:
                max_length = current_length
            stage = ''
            stage += char
        else:
            stage += char
            max_length = len(stage)
    return max_length

## BUG1: this doesn't start trcking a new substring until
## BUG2:
# Tests 3, 1, 3, 6
print(longest_substring('abcabcbb'))
print(longest_substring('bbbbb'))
print(longest_substring('pwwkew'))
print(longest_substring('pwwkewabc'))
