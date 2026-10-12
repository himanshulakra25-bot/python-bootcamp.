# import random 
# computer_number = random.randint(1,5)

# for attemt in range(1,4):
#     user_guess = int(input("guess number(between 1-5=>)"))

#     if user_guess == computer_number:
#         print("congrats")
#         break
#     else:
#         print("try again")
# else:
#     print("attempts finish try next time")

marks = [85, 90, -1, 78, -1, 92]

total_marks = 0
present_count = 0

for mark in marks:
    if mark == -1:
        continue
    total_marks += mark
    present_count += 1

print("Total Marks of Present Students:", total_marks)
print("Number of Students who took the exam:", present_count)