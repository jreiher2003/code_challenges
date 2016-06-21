from collections import Counter, OrderedDict 

class OrderedCounter(Counter, OrderedDict):
     'Counter that remembers the order elements are first encountered'

     def __repr__(self):
         return '%s(%r)' % (self.__class__.__name__, OrderedDict(self))

     def __reduce__(self):
         return self.__class__, (OrderedDict(self),)

lst = ["bcdef","abcdefg","bcde","bcdef"]
x = OrderedCounter(lst)
print len(x)
print " ".join([str(v) for k,v in x.iteritems()])
