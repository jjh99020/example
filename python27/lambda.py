def hap(x,y):
    return x+y
print hap(10,20)

#lambda ����
print (lambda x,y:x+y)(10,20)

#map(�Լ�,����Ʈ) ����Ʈ�� ���Ҹ� �Լ��� �ϳ��� ��
#**������ �ε�..
print map(lambda x: x**2, range(5))
print list(map(lambda x: x**2, range(5)))#���̽� 3���� ����Ʈȭ �����

#reduce(�Լ�,�������ڷ�)

from functools import reduce #���̽�3���� �ʿ�
print reduce(lambda x,y:x+y,[0,1,2,3,4])# ù���ڰ� ������ 
print reduce(lambda x, y: y+x, 'asdfg')#���ڿ��� ���� �ѱ��� �Ųٷι�ġ�ϸ� ����

#filter(�Լ�,����Ʈ) ���ΰ��� ���
print filter(lambda x:x<5, range(10))
