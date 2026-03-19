for i in range(n):
    print(i) # O(n)

for i in range(n):
    for j in range(i):
        print(i,j) # O(n2)

i =1
while i<n:
    i*=2 #O(log n)

for i in range(n):
    for j in range(i):
        print(i,j) # O(n2)

for i in range(n):
    print(i) # O(n)
                        # O(n)
for j in range(n):
    print(J) # O(n)


for i in range(n):
    j=1
    while j<n:
        j*=2 # O(n log n)

def func(n):
    if n ==0:
        return
    func(n-1) # O(n)

def func(n):
    if n <= 1:
        return
    func(n/2)
    func(n/2) # O(log n2)