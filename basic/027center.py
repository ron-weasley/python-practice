from time import sleep
from math import sin, cos, radians

for i in range(25):
    x=i%10
    print("`".center(10*x if x<5 else 100-10*x))
    sleep(0.05)

# increase 40 to get more wave - wave
# for n in range(1, 40):
# 	circle_1 = 100 * (1 + sin(radians(n*10)))
# 	circle_2 = 100 * (1 + cos(radians(n*10)))
# 	print("#".center(int(circle_1)))
# 	print("*".center(int(circle_2)))
# 	sleep(1)