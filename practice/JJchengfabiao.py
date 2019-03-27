# -*- coding:UTF-8 -*-
#一行完成
#print(''.join([''.join(['%s*%s=%-2s' % (y, x, x*y)for y in range(1, x+1)])for x in range(1, 10)]))

#全部
# for i in range(1, 10):
#     for j in range(1, 10):
#         print('%s*%s=%2s' % (j, i, i*j), end=' ')
#     print()

#1*1 2*2对角线
# for i in range(1, 10):
#     for j in range(i, i+1):
#         print('%s*%s=%2s' % (i, j, i*j), end=' ')
#     print()

#左下三角
# for i in range(1, 10):
#     for j in range(1,i+1):
#         print('%s*%s=%2s' % (i, j, i*j), end=' ')
#     print()

#左上三角
# for i in range(1, 10):
#     for j in range(i, 10):
#         print('%s*%s=%2s' % (i, j, i * j), end=' ')
#     print()

#右上三角
# for i in range(1, 10):
#     for k in range(1, i):
#         print(end="       ")
#     for j in range(i, 10):
#         print('%s*%s=%2s' % (i, j, i * j), end=' ')
#     print()

#右下三角
for i in range(1, 10):
    for k in range(1, 10-i):
        print(end="       ")
    for j in range(1, i+1):
        print('%s*%s=%2s' % (i, j, i * j), end=' ')
    print()