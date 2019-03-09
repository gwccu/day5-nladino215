# File name: problemSetDay5.py
for a in range(5):
    print(a)
for b in range(5,8):
    print(b)
for c in range(5,18,3):
    print(c)
for d in range(0,31,5):
    print(d)

for y in range(1):
    print('*')
for y in range(1):
    print('*' * 3)
for y in range(1):
    print('*' * 5)
for y in range(1):
    print('*' * 7)

for y in range(1):
    print('   *')
for y in range(1):
    print('  ***')
for y in range(1):
    print(' *****')
for y in range(1):
    print('*******')

i = 1500
while i <=1700:
    if i % 7 == 0:
        print(i)
        print('these are divisible by 7')
        count += 1
    elif i % 5 == 0:
        print(i)
        print('these are multiples of 5')
        count += 1
print('end')
