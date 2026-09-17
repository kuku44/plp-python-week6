# FIXED: range(1, 10) stops before 10, so I changed it to range(1, 11).
for i in range(1, 11):
    print(i)


# FIXED: The loop was missing n -= 1, so n never changed and the loop never stopped.
n = 3
while n > 0:
    print(n)
    n -= 1



# FIXED: total was reset to 0 inside the loop, so I moved it before the loop.
total = 0
for i in range(1, 6):
    total = total + i
print(total)