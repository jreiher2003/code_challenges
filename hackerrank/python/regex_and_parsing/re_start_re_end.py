import re 
email = "tony@tiremove_thisger.net"
m = re.search("remove_this", email)
print email[:m.start()] + email[m.end():]


jeff = "jeff is the man bitches"
j = re.search(r'.', jeff)
print j.start()
print j.end()
print jeff.index(jeff[-1])
print len(jeff)

import re

S =raw_input()
pattern = raw_input()

result = []
for i in range(len(S)):
    m = re.match(pattern, S[i:])
    if m:
        result.append((i + m.start(), i + m.end()-1))
        print (i + m.start(), i + m.end()-1)

if not result:
    print (-1, -1)