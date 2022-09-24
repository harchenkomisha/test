def sum(num, res = 0):
    if not num:
        return res
    res += num%10
    num //= 10
    return sum(num, res)
              
 
print(sum(int(input())))
