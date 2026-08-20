print("Welcome")
s = input("Please enter your input: ")

def longest_balanced_substring(s):

    clean = ""
    i = 0
    while True:
        try:
            ch = s[i]
        except:
            break
        if ch != " " and ch != "\t" and ch != "\n":
            clean = clean + ch
        i = i + 1

    try:
        clean[0]
    except:
        return 0

    n = 0
    while True:
        try:
            clean[n]
            n = n + 1
        except:
            break

    def expand(start, end, c1, c2, count1, count2):
        if end == n:
            return 0

        ch = clean[end]

        if c1 is None:
            c1 = ch
            count1 = 1
        elif ch == c1:
            count1 = count1 + 1
        elif c2 is None:
            c2 = ch
            count2 = 1
        elif ch == c2:
            count2 = count2 + 1
        else:
            return 0

        current = 0
        if c1 is not None and c2 is not None and count1 == count2:
            current = end - start + 1

        next_val = expand(start, end + 1, c1, c2, count1, count2)

        if current > next_val:
            return current
        else:
            return next_val

    def helper(start):
        if start == n:
            return 0
        a = expand(start, start, None, None, 0, 0)
        b = helper(start + 1)
        if a > b:
            return a
        else:
            return b

    return helper(0)

print(longest_balanced_substring(s))
