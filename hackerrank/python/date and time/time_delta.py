from datetime import timedelta, datetime

d = timedelta(days=1)
print d
# x=datetime("Sun 10 May 2015 13:54:36 -0700")

y=("Sun 10 May 2015 13:54:36 +0000").split()
print y

from datetime import datetime
print('\n'.join([str(abs(int((datetime.strptime(input(), 
	"%a %d %b %Y %H:%M:%S %z")-datetime.strptime(input(), 
	"%a %d %b %Y %H:%M:%S %z")).total_seconds()))) 
for n in range(int(input()))]))