class Set:
    def __init__(self, value = []):    # Constructor
        self.data = []                 # Manages a list
        self.concat(value)

    def intersection(self, other):        # other is any sequence
        res = []                       # self is the subject
        for x in self.data:
            if x in other:             # Pick common items
                res.append(x)
        return Set(res)                # Return a new Set

    def union(self, other):            # other is any sequence
        res = self.data[:]             # Copy of my list
        for x in other:                # Add items in other
            if not x in res:
                res.append(x)
        return Set(res)

    def concat(self, value):
        for x in value:                
            if not x in self.data:     # Removes duplicates
                self.data.append(x)
    
    def issubset(self, other):  # Caution in order
        condition = True
        for x in self.data:
            condition = condition and x in other.data
        return condition

    def issuperset(self,other):
        condition = True
        for x in other.data:
            condition = condition and x in self.data
        return condition

    def intersection_update(self, other):
        res = []
        inter = self.intersection(other)
        for i in inter:
            res.append(i)
        del self.data[:]
        self.data += res
        return self

    def difference_update(self, other):
        res = self.data[:]
        for i in other.data:
            if i in res:
                res.remove(i)
        del self.data[:]
        self.data += res
        return self
    
    def symmetric_difference_update(self, other):
        res1 = self.union(other)
        res2 = self.intersection(other)
        res1 -= res2
        del self.data[:]
        self.data += res1
        return self
    
    def add(self, elem):
        res = [elem]
        self.data += res
        return self

    def remove(self, elem):
        raise KeyError('action: elem is not in the set')
        self.data.remove(elem)
        return self
    
    def __len__(self):          return len(self.data)        # len(self)
    def __getitem__(self, key): return self.data[key]        # self[i], self[i:j]
    def __and__(self, other):   return self.intersection(other) # self & other
    def __or__(self, other):    return self.union(other)     # self | other
    def __repr__(self):         return 'Set({})'.format(repr(self.data))  
    def __iter__(self):         return iter(self.data)       # for x in self:
    def __le__(self,other):     return self.issubset(other)
    def __lt__(self,other):     return self.issubset(other) and self.data != other.data
    def __ge__(self,other):     return self.issuperset(other)
    def __gt__(self,other):     return self.issuperset(other) and self.data != other.data
    def __ior__(self,other):    self.data += other.data; return self
    def __iand__(self,other):   return self.intersection_update(other)
    def __isub__(self,other):   return self.difference_update(other)
    def __ixor__(self,other):   return self.symmetric_difference_update(other)
    
################## test code ##################

x = Set([1,3,5,7,9])
y = Set([1,5,9])
print(y.issubset(x))
print(x.issuperset(y))
print(y<=x)
print(y<x)
print(y>x)
print(y>=x)

a = Set([1,3,5])
b = Set([2,4,5])
a|=b
print(a)

c = Set([2,6,7])
d = Set([2,5,6,9])
c&=d
print(c)

e = Set([1,2,3,4,5])
f = Set([2,3])
e-=f
print(e)

g = Set([1,2,3,4,5])
h = Set([2,3,4,5,6])
print(g.symmetric_difference_update(h))

i = Set([1,2,3,4,5])
j = Set([2,3,4,5,6])
i^=j
print(i)

k = Set([1,5,9])
k.add(11)
print(k)

l = Set([1,4,7])
l.remove(5)
print(l)