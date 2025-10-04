mark1 = 55
mark2 = 80 
mark3 = 90

def cal_averqe(m1, m2, m3):
    average = (m1 + m2 + m3) / 3
    return average

avg1 = cal_averqe(55, 65, 88)
avg2 = cal_averqe(80, 70, 90)
avg3 = cal_averqe(90, 95, 100)

print("Average 1 is: ", avg1)
print("Average 2 is: ", avg2)
print("Average 3 is: ", avg3)