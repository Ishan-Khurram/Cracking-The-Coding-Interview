def checkPermutation(s, k):
    hashmap = {}
    
    if len(s) != len(k):
        return False
    
    # Add value to hashmap from string 1
    for char in s:
        if char in hashmap:
            hashmap[char] += 1
        else:
            hashmap[char] = 1
    
    # decrement values from hashmap for string 2.
    for char in k:
        if char in hashmap:
            hashmap[char] -=1
        else:
            hashmap[char] = -1
            
    # Get all values in hashmap
    values = iter(hashmap.values())
    
    # Get first value in hashmap
    first_value = next(values)

    # make sure all values are equal to first_value
    for value in values:
        if value != first_value:
            return False
        
    return True
            

if __name__ == '__main__':
    print(checkPermutation(s="aero", k="hero"))
          