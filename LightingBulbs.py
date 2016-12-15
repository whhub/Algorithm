"""
#coding=utf8
2015盏灯，一开始全部熄灭，序号分别是1-2015，先把1的倍数序号的灯的开关全部按一次，然后把2的倍数的灯的开关全部按一次，然后把3的倍数的开关按一次，以此类推，最后把2015的倍数灯的开关按一次。问最后亮着的灯有多少盏？
"""
# 44

bulb_number = 2015
bulb_number_ = bulb_number + 1
bulbStatus = [False] * bulb_number_

for i in range(1, bulb_number_):
    for j in range(i, bulb_number_):
        if j % i:
            continue
        bulbStatus[j] = not bulbStatus[j]

lighting_bulb_count = 0
for k in range(1, bulb_number_):
    if bulbStatus[k]:
        lighting_bulb_count += 1

print(lighting_bulb_count)
