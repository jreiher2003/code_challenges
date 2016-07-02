import re
m = re.match(r'(\w+)@(\w+)\.(\w+)','username@hackerrank.com')
print m.group(0)       # The entire match 
#'username@hackerrank.com'
print m.group(1)       # The first parenthesized subgroup.
#'username'
print m.group(2)       # The second parenthesized subgroup.
#'hackerrank'
print m.group(3)       # The third parenthesized subgroup.
#'com'
print m.group(1,2,3)   # Multiple arguments give us a tuple.
# ('username', 'hackerrank', 'com')



###### groups 
import re
m = re.match(r'(\w+)@(\w+)\.(\w+)','username@hackerrank.com')
print m.groups()
#('username', 'hackerrank', 'com')


### groupdict()
m = re.match(r'(?P<user>\w+)@(?P<website>\w+)\.(?P<extension>\w+)', 'myname@hackerrank.com')
print m.groupdict()
#{'website': 'hackerrank', 'user': 'myname', 'extension': 'com'}