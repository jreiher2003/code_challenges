import re 
print re.split("-","+91-011-2711-1111")

print re.split("[,.]", "100,000,000,000")

import re
print "\n".join(i for i in re.split("[,.]*", raw_input())if len(i)>0)