"""
notes:
key value pairs.
we can use a "hash function" to store the key value pairs. an example of this
function is the ascii values (http://www.asciitable.com/).
so for example "march 6" we add the ascii values addes up to 609, we can take the mod
of 609 and get the value 9 (609 % 10 = 9) then we can store the value of
"march 6" at position 9
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
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for c in key:
            h += ord(c)
        return h % self.MAX

    # this allows us to use indexing to call the value
    # ie "Hashtable[key] = value"
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]


    def add(self, key, val):
        # get the "location" of the key with the ascii value
        h = self.get_hash(key)
        # set corresponding "location" to given value
        self.arr[h] = val

    #get value for given key
    def get(self, key):
        h = self.get_hash(key)
        return self.arr[h]

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None

if __name__ == "__main__":
    ht = HashTable()
    print(ht.get_hash('march 6'))
    ht.add('march 6', 130)
    print('-'*10)
    print(ht.arr)
    print(ht.get('march 6'))
    ht['march 7'] = 230
    print(ht['march 7'])
    print('-'*10)
    print(ht.arr)
    del ht['march 6']
    print('-'*10)
    print(ht.arr)
