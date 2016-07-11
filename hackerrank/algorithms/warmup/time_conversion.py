from datetime import datetime

time = '12:05:45AM'
end = time[-2:]
ti = time[:-2]
time = ti + " " + end
if end == 'PM':
    in_time = datetime.strptime(time, "%I:%M:%S %p")
    out_time = datetime.strftime(in_time, "%H:%M:%S")
    print out_time
if end == 'AM':
    in_time = datetime.strptime(time, "%I:%M:%S %p")
    out_time = datetime.strftime(in_time, "%H:%M:%S")
    print out_time

