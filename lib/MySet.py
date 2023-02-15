class MySet:
    pass
    def __init__(self, enumerable = []):
        self.dictionary = {}
        for value in enumerable:
            self.dictionary[value] = True
            
    def has(self, value):
        # This will return None instead of False when the value isn't in our set
        # return self.dictionary[value]
        # using the in keyword will return True or False
        return value in self.dictionary
    
    def add(self, value):
        pass
        self.dictionary[value] = True # Add the value as a key in our dictionary
        return self # Return the updated set
    
    def delete(self, value):
        # del self.dictionary[value] # Delete the key from our dictionary using the del keyword
        self.dictionary.pop(value, None) # Delete the key from our dictionary
        return self # Return the updated set
    
    def size(self):
        pass
        return len(self.dictionary)
    
    def clear(self):
        self.dictionary = {}
        return self.dictionary
    
    def __str__(self):
        pass
        set_list = []
        for key, value in self.dictionary.items():
            set_list.append(str(key))
        return f'MySet: {{{",".join(set_list)}}}'
     
    
set = MySet([1, 2, 3, 3])
print(set) # is the same as print(set.__str__())
        

# def first_repeated_value(list):
#     for i in range(0, len(list)):
#         for j in range(i+1, len(list)):
#             if list[i] == list[j]:
#                 return list[i]
#     return None

# def first_repeated_value(list):
#   # create a Set to keep track of values we've seen
#   number_set = set()
#   # iterate over each element from the list
#   for i in range (0, len(list)):

#     # if we've already seen a value, we've found the duplicate!
#     if list[i] in number_set:
#         return list[i]
#     # otherwise, add the value to our set
#     number_set.add(list[i])
#   # return None if we reach the end and haven't found our value
#   return None

# print(first_repeated_value([1,2,3,3,4,4]))