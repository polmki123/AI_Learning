import os

path = os.path.dirname(os.path.realpath(__file__))
fname = input('Enter File:')
if len(fname) < 1 : fname = 'clown.txt'
filename = os.path.join(path, fname )

hand = open( filename )

di = dict() # {}
for lin in hand :
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds :
        di[w] = di.get(w,0) + 1
        
largest = -1
theword = None
for k, v in di.items() :
    print(k,v)
    if v > largest : 
        largest = v
        theword = k
print('Done', theword, largest)

# data = sorted( di.items(), key = lambda x : x[1], reverse = True) # 정렬을 사용하여 구할 수 도 있다. 
# print('Done', data[0][0], data[0][1]) 

# data = di.items() 
# data = max(data) # max함수를 사용해도 된다. 
# print('Done', data[0], data[1])

