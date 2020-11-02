str = 'X-DSPM-Confidence: 0.8475'

ipos = str.find(':')
print(ipos)
piece = str[ipos+1:] 
print(piece) 
# print(piece + 42.0) error 
value = float(piece) # 공백이 있다고 해서 형변환이 되지 않는것은 아님
print(value)
print(value+42.0)