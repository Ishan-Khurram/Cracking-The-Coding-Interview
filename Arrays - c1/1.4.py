def palindrome(s):
    # lower values in string
    s = s.lower()
    
    # create hashmap
    hashmap = {}
    
    # Filter to keep only alphabetic characters
    s_only_letters = "".join([char for char in s if char.isalpha()])
    print(s_only_letters)
    
    # loop over string, add values to hashmap
    for char in s_only_letters:
        if char not in hashmap:
            hashmap[char] = 1
        else:
            hashmap[char] += 1

    # ensures there is only one value that is equal to 1
    one_count = 0

    for value in hashmap.values():
        # Allow at most one value to be equal to 1
        if value == 1:
            one_count += 1
            if one_count > 1:
                return False
        # if the value is not an even number, palindrome is impossible.
        else:
            if value % 2 != 0:
                return False

    return True
if __name__ == '__main__':
    print(palindrome(s="tact Coa"))
    
    # A man, a plan, a canal — Panama!



