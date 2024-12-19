import random

# Suggested code may be subject to a license. Learn more: ~LicenseLog:2808102141.
random_integer = random.randint(1, 10)
print(random_integer)

ran= random.randint(1,999)

student_score=[]

for a in range(100):
    student_score.append(random.randint(1,999))

print(student_score)

max_number=0

for max in student_score:
    if max> max_number:
        max_number=max

print(f"The max number in the loop: {max_number}")

tog=1
for addto in range(1,101,):
    tog *=addto

print(tog)
