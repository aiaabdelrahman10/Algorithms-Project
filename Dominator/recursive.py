print("Welcome")
print("Enter integers one by one. Press Enter on empty line to finish:")

A = []


while True:
    try:
        line = input()
    except:
        break

    if line == "":
        break


    num = 0
    neg = False
    i = 0
    started = False
    valid = True

    while True:
        try:
            c = line[i]
        except:
            break

        if c == '-' and not started:
            neg = True
            started = True
        elif c >= '0' and c <= '9':
            num = num * 10 + (ord(c) - ord('0'))
            started = True
        else:
            valid = False
            break
        i += 1

    if not valid:
        print("Invalid input! Enter integers only.")
        continue

    if neg:
        num = -num

    A.append(num)


if A == []:
    print("No Dominator Found")
    exit()


n = 0
for _ in A:
    n += 1


size = 0
value = 0
for i in range(n):
    if size == 0:
        value = A[i]
        size = 1
    elif A[i] == value:
        size += 1
    else:
        size -= 1


indices = []
for i in range(n):
    if A[i] == value:
        indices.append(i)


count = 0
for _ in indices:
    count += 1

if count > n // 2:
    print("Dominator Indices =", indices)
else:
    print("No Dominator Found")
