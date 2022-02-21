def longest_repetition(chars):
    x = []
    x.append(chars[0])
    count = 0
    tmp = ''
    y = []
    for i in range(len(chars)):
        x.append(chars[i])        
    # count the number of the same letters and then run again to count the next letter and so on and then
    # compare the different length values
    tmp = x[0]
    print(count_same(x, count, tmp, y))   
    
        
def count_same(x = [], count = int, tmp = chr, y = []):
    charic = ''
    lengthofc = 0
    run = True
    i = len(y)
    t = 1
    tn = 0
    ts = ''
   
    if count <= len(x) - 1:
        charic = x[count]
        if charic == tmp:
            tmp = x[count]
            lengthofc += 1
            count += 1
            count_same(x, count, tmp, y)   
        else:
            y.append(lengthofc)
            lengthofc = 0
            count += 1
            count_same(x, count, tmp, y)   #
            
    
    while run == True:
        if y[i] > y[i-1]:
            tn = y[i]
            y[i] = y[i - 1]
            y[i - 1] = tn
            ts = x[i]
            x[i] = x[i-1]
            x[i-1] = ts 
        
        if i - 1 == -1:
            run = False
            
    charic = x[0]
    lengthofc = y[0]        
    
    return (charic,lengthofc) 
        
longest_repetition("aaaabb")