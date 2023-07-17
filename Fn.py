def mysum(x,*vartuple):
     result = x
     for i in vartuple:
         result += i
         print(result)
mysum(5,10,3,4,6)
