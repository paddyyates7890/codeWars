def get_sum(a,b):
    num = []
    ans = 0
    if a == b:
        return a
    
    else:
        if a > b:
            diff = a - b
            num.append(b)
            for i in range(diff):
                num.append(b + 1)
        elif a < b:
            diff = b - a
            num.append(a)
            for i in range(diff):
                num.append(a + 1)  
                
    print(num)        
    for i in range(len(num)):
        ans += num[i]    

    return ans
print(get_sum(1,2))
print(get_sum(-1,2))