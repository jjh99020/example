def hap(x,y):
    return x+y
print hap(10,20)

#lambda 형식
print (lambda x,y:x+y)(10,20)

#map(함수,리스트) 리스트의 원소를 함수에 하나씩 적
#**제곱근 인듯..
print map(lambda x: x**2, range(5))
print list(map(lambda x: x**2, range(5)))#파이썬 3에선 리스트화 해줘야

#reduce(함수,순서형자료)

from functools import reduce #파이썬3에선 필요
print reduce(lambda x,y:x+y,[0,1,2,3,4])# 첫인자가 누적값 
print reduce(lambda x, y: y+x, 'asdfg')#문자열도 가능 한글은 거꾸로배치하면 깨짐

#filter(함수,리스트) 참인값만 출력
print filter(lambda x:x<5, range(10))
