def bitmask(word):
    mask = 0
    for ch in word:
        i = ord(ch)-ord('0')
        mask |= 1 << i
    print("Original Mask: ",mask, bin(mask)[2:])
    
    submask = mask
    while submask:
        submask = (submask-1)&mask
        print(submask)

bitmask("123")
