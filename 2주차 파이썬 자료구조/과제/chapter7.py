import os

path = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(path, 'mbox-short.txt' )
fh = open( filename , 'r')

print(fh)

for lx in fh:
    # ly = lx.rstrip()
    ly = lx # 그냥 할 경우 기본 print 출력 + 개행문자열로 인해서 사이사이가 한칸씩 벌어짐 
    print(ly.upper())