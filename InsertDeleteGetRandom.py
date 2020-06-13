# Problem available at: https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/540/week-2-june-8th-june-14th/3358/

# Question:
'''
Design a data structure that supports all following operations in average O(1) time.

insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.


'''

class RandomizedSet:

    def __init__(self):
        self.set_ = []
        

    def insert(self, val: int) -> bool:
        
        if val not in self.set_:
            self.set_.append(val)
            return True
        else:
            return False
            

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        
        if val in self.set_: 
            self.set_.remove(val)
            return True
        else:
            return False
    

    def getRandom(self) -> int:
        return random.choice(self.set_)
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()