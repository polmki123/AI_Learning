import os

path = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(path, 'mbox-short.txt' )
han = open( filename )

# 처음 단어가 From 인 것만 출력 하도록 그리고 거기서 2번째 단어 

def Guardian( input ):
    if type(input) != type([]) : #타입 비교 
        return  False
    if len(input) < 3 or input[0] != 'From' :
        return False 
    return True 

for line in han:
    line = line.rstrip() # 공백 제거 
    # print('Line : ', line)
    # if line == '' :
    #     print( 'Skip Blank' )
    #     continue
    wds = line.split()
    # print('Words: ' , wds)
    if not Guardian(wds) :
        # print('Ignore')
        continue
    print(wds[2])
    # if len(wds) < 3 or wds[0] != 'From' :
    #     continue
