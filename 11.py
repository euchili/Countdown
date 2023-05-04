import time
theTime = input("Insert time to count down (HH:MM:SS)")


b=[int(i) for i in theTime.split(":")]
second=b[0]*3600+b[1]*60+b[2]


for x in range(second, 0, -1):
     sec = x % 60
     min = int(x / 60) % 60
     hours = int(x / 3600)
     print(f'{hours:02}:{min:02}:{sec:02}')
     time.sleep(1 / 2)
time.sleep(2)
print("Done")
