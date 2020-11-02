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

#intro 가장 큰거 찾기 
filename2 = os.path.join(path, 'intro.txt' )
hand = open( filename2 )

di = dict() # {}
for lin in hand :
    wds = lin.rstrip().split()
    for w in wds :
        di[w] = di.get(w,0) + 1

tmp = di.items() 
# 람다식을 사용해서  2번째 요소 사용 가능 
tmp = sorted(tmp , key = lambda x : x[1], reverse = True )

# print(tmp[:5])

for v,k in tmp[:5] :
    print(v, k)
