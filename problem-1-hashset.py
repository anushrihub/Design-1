## Problem 1:(https://leetcode.com/problems/design-hashset/)

# Created a attribute in form of `list` that stores the keys.
# Add - Use class's own `contains` and `remove` methods, to remove any existing key. 
#       Used the list's append method to add keys. O(n)
# Remove - Using del statement and iteration to remove (instead of using list's `remove` method). O(n)
# Contains - iterate and match to return if found. O(n)

class MyHashSet:
    # method to intialize the hashset
    def __init__(self):
        self.hashset = []

    # method to insert the value into the hashset
    def add(self, key: int) -> None:
        # check the given values in the hashset
        if self.contains(key):
            # if present remove the value
            self.remove(key)
        # append the value in either cases
        self.hashset.append(key)

    # method to remove the value from the hashset    
    def remove(self, key: int) -> None:
        # iterate over the hashset
        for i, element in enumerate(self.hashset):
            # match the element with the given value
            if element == key:
                # remove the key if it matches
                    del self.hashset[i:i+1]
    
    # method to check whether the key is exist in hashset or not
    def contains(self, key: int) -> bool:
        # iterate over the hashset
        for i in self.hashset:
            # match the key with the value
            if i == key:
                return True
        return False



# myHashSet = MyHashSet()
# print(myHashSet.add(1))      # set = [1]
# print(myHashSet.add(2))      # set = [1, 2]
# print(myHashSet.contains(1)) # return True
# print(myHashSet.contains(3)) # return False, (not found)
# print(myHashSet.hashset)
# print(myHashSet.add(2))      # set = [1, 2]
# print(myHashSet.contains(2)) # return True
# print(myHashSet.remove(2))
# print(myHashSet.hashset)   # set = [1]
# print(myHashSet.contains(2)) # return False, (already removed)
# print(myHashSet.hashset)