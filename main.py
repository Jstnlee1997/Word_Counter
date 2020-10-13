import re

# Creating a HashTable class, with 100 available elements, that would record the number of each word in a given text
class HashTable:
    def __init__(self):
        self.MAX = 100     # the size of it is 100 elements
        self.arr = [[] for i in range(self.MAX)]    #creating an array, which contains as many empty arrays as MAX indicated

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)   # find the ASCII value of the character
        return h % self.MAX

    def __setitem__(self, key, val):
        h = self.get_hash(key)

        found = False
        # If we are given a key value pair where the key is already being used and we want to simply replace the value:
        for idx, element in enumerate(self.arr[h]):     # use enumerate to iterate through items in an array
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key,val)
                found = True
                break

        # do this only if the key does not exist in the hash table
        if not found:
            self.arr[h].append((key,val))    # tuple 

    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]   #returns the value

    def __delitem__(self, key):
        h = self.get_hash(key)

        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]

WordCount = HashTable()
with open('<Input your text file>.txt', 'r') as f:
    for line in f:
        for word in line.split():
            string = ""
            for char in range(0,len(word)):
                # We are only interested in characters a-z etc.
                if word[char].isalpha() == True:
                    # Obtain the lowercase of each word, but if you want to be case sensitive, merely remove the ".lower()" method
                    string += word[char].lower()

            # Check if the current word has been added into the Hash table, if it hasn't, add it and give it a count value of 1
            if WordCount['{}'.format(string)] is None:
                WordCount['{}'.format(string)] = 1
            
            # If the current word exists in the Hash Table, merely increase its count value by 1
            else:
                WordCount['{}'.format(string)] += 1

# Output
print(WordCount.arr)