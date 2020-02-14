def ishappy(n):
    d = {} # create a hashtable cause its O(1)
    while True: #enter loop
        res = 0
        while n > 0:        
            res += (n % 10) ** 2
            n //= 10
        n = res
        if res == 1:
            return True
        elif res in d:
            return False
        else:
            d[n] = 1


ishappy(19)

