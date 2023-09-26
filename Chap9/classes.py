class Complex:
    def __init__(self, real_part, imag_part):
        self.r = real_part
        self.i = imag_part

class MyClass:
    """A simple class"""

    i = 12345

    def f(self):
        return 'hi randy!'

class Dog:
    kind = 'Canine'#a class variable. All instances have kind = Canine

    def __init__(self, name):
        self.name = name#each instance can have a unique name

x = Complex(3.0, -4.5)
print(x.r, x.i)

x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter

mc = MyClass()
mcf = mc.f

for i in range(6):
    print(mcf())

d = Dog('Luna')
e = Dog('Moon')

print(d.kind, d.name, e.kind, e.name)

#This next is weird.
#You can define a class function outside the class
def f1(self, x, y):
    return min(x, y)

class Q:
    f = f1#f is a function object in side a class, so it is a method of the class
    #even though it's defined outside the class :/

    def g(self):
        return 'what?'

    h = g

cue = Q()
print(cue.f(79, 45))
print(cue.h())
print(cue.g())


class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)


sack = Bag()
sack.add(9)
sack.addtwice(7)

print(sack.data)

print(sack.__class__)

sackness = isinstance(sack, int)
print(sackness)

#NAME MANGLING
class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method,
    #will get replaced with __Mapping__update

class MappingSubclass(Mapping):

    def update(self, keys, values):#the subclass defines its own version of update
        #this should clash
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)



print(dir(Mapping))#shows one as __Mapping__update
#print(dir(MappingSubclass))

class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self #this works because an iterator is an object that implements __next__()

    def __next__(self):
        if self.index == 0:
            raise StopIteration #we've run out of stuff
        self.index = self.index - 1
        return self.data[self.index] #return the data element at index, here index will
        #always be a negative number so will work back from the end to the front


rev = Reverse('Ray Hamburger')
print(iter(rev))
for char in rev:
    print(char)
    

#a Generator - the __iter__() and __next__() methods are created automatically
def reverse(data):
    #anje = range(len(data)-1, -1, -1)
    #print(anje)
    #print(list(anje))
    #for index in anje:#start, stop, step
    for index in range(len(data)-1, -1, -1):
        #range is an immutable sequence of numbers
        #its content will follow r[i] = start + step*i. So r[0] = 3 + -1*0 = 3.
        #r[1] = 3 + -1*1 = 2, etc...
        #for a negative step (like -1 here), the condition is i >= 0 and r[i] > stop
        #so things will continue while r[i] > -1
        #the for loop will call __next__() each time through
        #the Generator will stop at yield, give anje[3], 'f', stop, remembering its context
        #and then on the next call to __next__() will yield anje[2], 'l', etc.
        yield data[index]

print('\n\n')
for char in reverse('golf'):
    print(char)


#Generator Expressions .....
#(expression for index in range()) <-- that's a generator expression, a condensed
#form of a generator
print(sum(i*i for i in range(0, 12))) #sum of squares

xvec = [10, 20, 30]
yvec = [7, 5, 3]

print(sum(x*y for x,y in zip(xvec, yvec))) #dot product
#zip returns [(x1, y1), (x2, y2), ...]

data = 'golf'
print(list(data[i] for i in range(len(data)-1, -1, -1)))#works same as reverse
#Generator above





    

        
