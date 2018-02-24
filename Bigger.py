def bigger(a,b,c):
    if a > b:
        if a > c:
            return a
        else:
            return c
    else:
        if b > c:
            return b
        else:
            return c
        
        
print bigger(1,9,10)
print bigger(10,100,11)
print bigger(1000,3000,100)
print bigger(1200,24000,16)
