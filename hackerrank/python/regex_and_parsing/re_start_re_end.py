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