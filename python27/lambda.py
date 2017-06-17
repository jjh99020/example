def hap(x,y):
    return x+y
print hap(10,20)

#lambda method
print (lambda x,y:x+y)(10,20)

#map(method,list) map method use the variables in the list sequentially

print map(lambda x: x**2, range(5))
print list(map(lambda x: x**2, range(5)))#python3 

#reduce(method,list)

from functools import reduce #python3 
print reduce(lambda x,y:x+y,range(5))# frist variable is accumulte variable
print reduce(lambda x, y: y+x, 'asdfg')#String is also possible. If you change back and forth, Korean is broken 

#filter(method,list) ture state return
print filter(lambda x:x<5, range(10))
