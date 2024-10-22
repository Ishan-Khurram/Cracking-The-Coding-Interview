def oneAway(s, k):
    # if the value is more than 1 change away, return false.
    if abs(len(s) - len(k)) > 1:
        return False
    
    # check if there is only one difference between the same length values.
    if len(s) == len(k):
        counter = 0
        for char, char1 in zip(s, k):
            if char != char1:
                counter += 1
            if counter > 1:
                return False
        return True
                
    # Check which string is longer.
    if len(s) > len(k):
        longer = s
        shorter = k
    else:
        longer = k
        shorter = s
        
    # initialize pointers for both strings.
    l = 0
    r = 0
    
    # counter to check the total differences between strings.
    differences = 0
    
    # ensure pointers do not go out of bounds.
    while l < len(longer) and r < len(shorter):
        # if longer string at index pointer doesn't equal its counterpart in the other string, increment the difference counter
        if longer[l] != shorter[r]:
            differences += 1
            # if difference counter exceeds 1, return false.
            if differences > 1:
                return False
            # increment the longer pointer if characters don't match
            l += 1
        # if characters match, increment both pointers to move to the next character.
        else:
            l += 1
            r += 1
            
    return True 

if __name__ == '__main__':
    print(oneAway(s="pale", k="pale"))
    
