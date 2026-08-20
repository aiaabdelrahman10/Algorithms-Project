print("Welcome")
s = input("Please enter your input: ")

def longest_balanced_substring(s):

    if s is None:
        return 0

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

    ans = 0
    i = 0

    while i < n:
        j = i + 1
        while j < n:

            c1 = clean[i]
            c2 = clean[j]

            if c1 == c2:
                j = j + 1
                continue

            count1 = 0
            count2 = 0
            start = i
            k = i

            while k < n:
                ch = clean[k]

                if ch != c1 and ch != c2:
                    count1 = 0
                    count2 = 0
                    start = k + 1
                else:
                    if ch == c1:
                        count1 = count1 + 1
                    else:
                        count2 = count2 + 1

                    if count1 == count2:
                        length = k - start + 1
                        if length > ans:
                            ans = length

                k = k + 1

            j = j + 1
        i = i + 1

    return ans


result = longest_balanced_substring(s)
print(result)
