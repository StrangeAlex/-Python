#Task 1
height = input()
weight = input()
name = input()
print(f"Hello! My name is {name}! My weight is {weight} and the height is {height}.")


#Task 2
time = int(input("Enter the time in seconds:"))
hours = time // 3600
minutes = time % 3600 // 60
seconds = time % 3600 % 60
print(f"{hours}:{minutes}:{seconds}")


#Task 3
n = str(input())
print(int(n) + int(n+n) + int(n + n + n))


#Task 4
n = str(input())
max = 0
for i in n:
    while int(i) > max:
        max = int(i)
print(max)


#Task 5
a = float(input())
b = float(input())
if a > b:
    print("Profit!")
else:
    print("nah")
print(f"Soot is {a/b}")
c = int(input())
print((a-b)/c)

#Task 6
a = float(input())
b = float(input())
day = 1
while a < b:
    a += a * 0.1
    day += 1
print(day)
