def stringComprehension(s):
    
    # if string is empty, or only one char in string, return the og string.
    if not s or len(s) == 1:
        return s
    
    # counter to start at one since there is guarenteed to be at least one of the chracter if shown in string.
    counter = 1
    new_string = ""
    
    for char in range(1, len(s)):
        if s[char] == s[char - 1]:
            counter += 1  # to count the amount of times a char appears in a row.
        else:
            new_string += s[char - 1] + str(counter) # append values to new string and reset counter.
            counter = 1
            
    # get the last character, and since the counter is not reset since it exited the loop, append the remaining counter to the last character.
    new_string += s[char-1] + str(counter)
    
    # return string with the shortest length.
    if len(new_string) > len(s):
        return s
    else:
        return new_string
    
    

if __name__ == '__main__':
    print(stringComprehension(s=""))
          