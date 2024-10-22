def isUnique(s):
    hashmap = {}
    
    for char in s:
        if char in hashmap:
            hashmap[char] += 1
        else:
            hashmap[char] = 1
            
    for value in hashmap.values():
        if value > 1:
            return False
    return True

if __name__ == '__main__':
    print(isUnique(s="saps"))
          