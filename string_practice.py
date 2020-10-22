#ABDAADBC  ====> AC
def remove_adj_dup(strng):
    if len(strng) < 2:
        return strng
    prv = strng[0]
    k = 0
    cur = 1

    size = len(strng)
    str = list(strng)
    while cur < size:
        if prv != str[cur]:
            k += 1
            str[k] = str[cur]
            prv = str[k]
            cur += 1

        else:
            while cur < size and prv == str[cur]:
                cur += 1
            k -= 1
            prv = str[k]

    return("".join(str[:k+1]))

str = "ABDAADBC"
ret = remove_adj_dup(str)
print("Remove adjacent duplicate: ", ret)
