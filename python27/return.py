def function(x):
    a=3
    b=5
    y= a*x+b
    return y

c = function(10)

print c

def triangle(x,h):

    return x*h/2

print triangle(2,4)

print 2== 1+1

if 1+1==2:
    print 'yes'
else:
    print 'no'

def exam():
    ans= raw_input('1+2=')#raw_input 문자열을 받는 함수
    return 1+2== int(ans)#int 문자열을 숫자로 변환하는함수

exam()
