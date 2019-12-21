a = int(input('hour = '))
b = int(input('minute = '))
c = int(input('seconds = '))
a1 = int(input('hour1 = '))
b1 = int(input('minute1 = '))
c1 = int(input('seconds1 = '))
abc = (a*60*60)+(b*60)+c
abc1 = (a1*60*60)+(b1*60)+c1
time = abc - abc1
print(abs(time),'sec')