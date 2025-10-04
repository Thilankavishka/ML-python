x = 1
student = 5

while x <= student:
  mark = int(input(f"Enter your mark_{x}: "))
  if mark >= 75:
    print("Your Grade is A")
  elif mark >= 65:
    print("Your Grade is B")
  elif mark >= 55:
    print("Your Grade is C")
  elif mark >= 45:
    print("Your Grade is S")
  else:
    print("Your Grade is F")
  x = x + 1
"""
Enter your mark_1: 88
Your Grade is A
Enter your mark_2: 55
Your Grade is C
Enter your mark_3: 22
Your Grade is F
Enter your mark_4: 45
Your Grade is S
Enter your mark_5: 44
Your Grade is F
"""
