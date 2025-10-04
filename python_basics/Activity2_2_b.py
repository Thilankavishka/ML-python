x = 10
n = 1
max = 0
min = 100
sum = 0
while n <= 10:
  mark = int(input(f"Enter your mark_{n}: "))
  if mark > max:
    max = mark

  if mark < min:
    min = mark

  sum = sum + mark
  n = n + 1

print("Maximum Mark: ", max)
print("Minimum Mark: ", min)
print("Average Mark: ", sum / x)
"""
Enter your mark_1: 80 
Enter your mark_2: 99
Enter your mark_3: 55
Enter your mark_4: 22
Enter your mark_5: 10
Enter your mark_6: 50
Enter your mark_7: 66
Enter your mark_8: 95
Enter your mark_9: 15
Enter your mark_10: 22
Maximum Mark:  99
Minimum Mark:  10
Average Mark:  51.4

"""
