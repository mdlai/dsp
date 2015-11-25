# Hint:  use Google to find python function
import datetime

####a)
date_start = '01-02-2013'
date_stop = '07-28-2015'

d_start = datetime.datetime.strptime(date_start,"%m-%d-%Y")
d_stop = datetime.datetime.strptime(date_stop,"%m-%d-%Y")
print d_stop - d_start

####b)
date_start = '12312013'
date_stop = '05282015'

d_start = datetime.datetime.strptime(date_start,"%m%d%Y")
d_stop = datetime.datetime.strptime(date_stop,"%m%d%Y")
print d_stop - d_start

####c)
date_start = '15-Jan-1994'
date_stop = '14-Jul-2015'

d_start = datetime.datetime.strptime(date_start,"%d-%b-%Y")
d_stop = datetime.datetime.strptime(date_stop,"%d-%b-%Y")
print d_stop - d_start
