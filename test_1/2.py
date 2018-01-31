
# coding=utf-8
'''
print ('ABCDEFG'[:3])

L = range(0, 30);
print(L);


for i in L:
    print(i);


L = list(range(20));

print(L);

for i in L:
    print(i);

'''

#用filter求素数

def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


def _not_divisible(n):
    #print('x=',x);
    print('n=',n);
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列


# 打印1000以内的素数:
for n in primes():
    if n < 10:
        print(n)
    else:
        break