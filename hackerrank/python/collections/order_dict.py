from collections import OrderedDict

new_dict = OrderedDict()
new_dict["jeff"] = 36
new_dict["john"] = 33
new = sorted(new_dict.items(), key=lambda x: x[1])
print new
for k,v in new_dict.iteritems():
    print k,v
