'''
elevi = [["Robert", 9], ["Andrei", 9.20], ["Stefan", 9.40], ["Cucumber", 4.30]]

for x in range(len(elevi)):
    temp = elevi[x][0]
    elevi[x][0] = elevi[x][1]
    elevi[x][1] = temp

elevi.sort()

for x in range(len(elevi)):
    temp = elevi[x][0]
    elevi[x][0] = elevi[x][1]
    elevi[x][1] = temp

for y in elevi:
    print(y)
'''


'''
string = "x"
for p in range(6):
    print(string*p)
'''

'''
n = 15
for x in range(0, n+1):
    print((x % 6 == 0) * "Nicu")
'''

'''
print(2 ** 100)
'''

'''
17 = 10001 # 2^4 + 1
11 = 1011 # 2^3 + 3
19 = 10011 # 2^4 + 3
23 = 10111 # 2^4 + 2^2+3

63 = 111111 # 2^5 (32) + 2^4 (16) + 2^3 + 2^2 + 3 (15)

65 = 1000001 # 2^6 (64) + 1
'''

'''
a = 52
b = 53
c = 67
e = 5
d = 17

temp = a ^ a ^ b ^ c ^ e ^ a ^ e ^ c ^ b ^ c ^ a ^ d ^ c
print(temp) # d
'''

'''
# 1100
# 0001
# 0000
numar = 12
print(numar & 1 == 0) # nr par
'''

'''
from librarypy import arde

def nmain():
    print("Calculez radical si etc: " + str(arde()))

def retard():
    print("N-ai ma nimic :(")

nmain()


retard()
'''

'''
if __name__=='__main__':
    print('salut')
'''

'''
global x

x = 1

print(x)
'''

'''
# big data
a = 2 ** 1000000
print(a)
'''
