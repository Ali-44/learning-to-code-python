fname=input('Enter file name:')
try:
    fhandle=open(fname)
except:
    print('Enter correct file name')
    quit()

count=0
total=0
for i in fhandle :
    i=i.rstrip()
    if not i.startswith('X-DSPAM-Confidence:'):
        continue
    count= count +1
    locater=i.find(':')
    num=i[locater+1:]
    fnum=float(num)
    total=total+ fnum

average=total/count
print('Average spam confidence:', average)
