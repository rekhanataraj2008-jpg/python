ATM PY.py
print("select the services you want:")
print('1.withdraw')
print('2.deposit\n3.saving\n4.balance')
PIN=123
service=int (input('plz select:'))
if service==1:
    print('withdraw')
amount =int(input ('Enter a amount:')
pin=int(input('Enter your secret pin:'))
run=True
while=run==0:
if pin==PIN:
    print("collect your amount',amount)
    run=False
else:
    print('incorrect pin')
    run=True
             
elif service==2:
    print('deposit')
elif service==3:
    print('saving')
elif service==4:
    print('balance')
else:
    print('kindly select the above services')
