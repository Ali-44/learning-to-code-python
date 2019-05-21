
count=0
total=0.0
while True:
    user_No=input('Enter a number:')
    if user_No =='done':
        break
    try:
        fuser_No=float(user_No)
    except:
        print('error')
        continue
    count=count+1
    total=total+fuser_No
print('All done')

if count >0 :
    print(count,total,(total/count))
