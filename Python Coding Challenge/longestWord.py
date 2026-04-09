# input = "I love programming" 

# for i in input:

def longest_word(s):
    words = s.split()   # split by space
    longest = ""

    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest


# Example
s = "I love programming"
print(longest_word(s))