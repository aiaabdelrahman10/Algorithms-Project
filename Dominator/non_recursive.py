print("Welcome")
print("Enter integers one by one. Press Enter on empty line to finish:")

A = []

def read_number():
    try:
        line = input()
    except:
        return None

    if line == "":
        return None

    num = 0
    neg = False
    i = 0
    in_number = False

    while True:
        try:
            c = line[i]
        except:
            break

        if c == '-' and not in_number:
            neg = True
            in_number = True
            num = 0
        elif c >= '0' and c <= '9':
            num = num * 10 + (ord(c) - ord('0'))
            in_number = True
        else:
            print("Invalid input! Enter integers only.")
            return read_number()

        i += 1

    if neg:
        num = -num
    return num


while True:
    n = read_number()
    if n is None:
        break
    A.append(n)


try:
    A[0]
except:
    print("No Dominator Found")
    exit()


def array_length(A, i=0):
    try:
        A[i]
    except:
        return 0
    return 1 + array_length(A, i+1)


def find_candidate(A, i=0, size=0, value=0):
    try:
        A[i]
    except:
        return value
    if size == 0:
        return find_candidate(A, i+1, 1, A[i])
    elif A[i] == value:
        return find_candidate(A, i+1, size+1, value)
    else:
        return find_candidate(A, i+1, size-1, value)


def collect_indices(A, value, i=0, indices=None):
    if indices is None:
        indices = []
    try:
        A[i]
    except:
        return indices
    if A[i] == value:
        indices.append(i)
    return collect_indices(A, value, i+1, indices)


def dominator(A):
    cand = find_candidate(A)
    indices = collect_indices(A, cand)
    n = array_length(A)
    if len(indices) > n // 2:
        return indices
    else:
        return []

res = dominator(A)
if not res:
    print("No Dominator Found")
else:
    print("Dominator Indices =", res)
