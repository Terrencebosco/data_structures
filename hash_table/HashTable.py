"""
notes:
key value pairs.
we can use a "hash function" to store the key value pairs. an example of this
function is the ascii values (http://www.asciitable.com/).
so for example "march 6" we add the ascii values addes up to 609, we can take the mod
of 609 and get the value 9 (609 % 10 = 9) then we can store the value of
"march 6" at position 9

hash table pt.2
collision handling..
collision occures when multiple keys have the same index so we have multiple values
for the same key. the two keys collide to the same index.

one way of handling this is by "chaining". so if a key index has multiple values
assocciated with it, its value is a list with a key value pair for each element.
O(n). we have to linearly search these subs list.

linear probing:
we find the spot of collision we just move to the next free element.
"""

### as of now class doesnt not handle collision
# custom hash fucntion
def get_hash(key):
    # save the total hash value for each charater in key
    # in this case the key is a string
    hashs_value = 0
    for c in key:
        # ord will retrun the ascii value for that string then save it to the hash_value
        hash_values += ord(c)
    # return the mod of the hash value as the "location" of that key
    # ie "9" for "march 6" -> see above where "10" is the size of the list.
    return hash_values % 10

# hash table class
class HashTable:
    def __init__(self):
        self.MAX = 10
        # instead of every element being "None" we will use an empty list
        self.arr = [[] for i in range(self.MAX)]


    def get_hash(self, key):
        h = 0
        for c in key:
            h += ord(c)
        return h % self.MAX


    # this allows us to use indexing to call the value
    # ie "Hashtable[key] = value"
    def __setitem__(self, key, val):
        h = self.get_hash(key)

        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element)==2 and element[0]==key:
                # storing tuble, immutable
                # find the array element then set the ith element to the new arr
                self.arr[h][inx] = (key, val)
                found = True
                break

        # if element doesnt exist add it
        if not found:
            self.arr[h].append((key, val))


    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]


    def __delitem__(self, key):
        h = self.get_hash(key)
        for idx, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][idx]

# -------------------------------
    # non pythonic way.
    def add(self, key, val):
        # get the "location" of the key with the ascii value
        h = self.get_hash(key)
        # set corresponding "location" to given value
        self.arr[h] = val

    #get value for given key
    def get(self, key):
        h = self.get_hash(key)
        return self.arr[h]



if __name__ == "__main__":
    ht = HashTable()
    print(ht.get_hash('march 6'))
    ht['march 6'] = 130
    ht['march 17'] = 500
    print('-'*10)
    print(ht.arr)
    print(ht.get('march 6'))
    ht['march 7'] = 230
    print(ht['march 7'])
    print('-'*10)
    print(ht.arr)
    print('-'*10)
    print(ht.arr)
    print(ht['march 6'])
    del ht['march 6']
    print('-'*10)
    print(ht.arr)
