# def outer():
#     x = 10
#     print x
#     def inner():
#         x = 5
#         print x
#     inner()
# # print outer()
# from pprint import pprint 
# pprint(dir(outer))
# print outer.__class__
# print outer.__call__()
# print outer.__closure__
# print outer.__code__
# print outer.__defaults__
# print outer.__module__
# print outer.__name__
# print outer.__repr__()
# print outer.__init__

def format_phonenums(func):
    def inner(lst):
        for i in range(len(lst)):
            lst[i] = "+91 " + lst[i][-10:-5] + ' ' + lst[i][-5:]
        func(lst)
    return inner

@format_phonenums
def sorted_lst(lst):
    print '\n'.join(sorted(lst))

lst1 = ['07895462130','919875641230','9195969878']
print sorted_lst(lst1)