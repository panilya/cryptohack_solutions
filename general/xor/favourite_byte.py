data = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
hx = [i for i in bytes.fromhex(data)]

for n in range(255):
    str = [n ^ elem for elem in hx]
    flag = "".join(chr(c) for c in str)
    print(flag)
