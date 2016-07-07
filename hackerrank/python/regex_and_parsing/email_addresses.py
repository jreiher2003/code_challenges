import re

emailre = "^[a-zA-Z]+[\w.\-\_]+@[a-zA-Z]+.[\w]{1,3}$"
string = "this <is_som@radom.stuff>"
e = string.split()[1].strip("<>")
if re.search(emailre, e):
    print string
