# DeomoSetTuple.py
tp = (1,2,3,)
print( len(tp))
print(tp[0])

#함수를 정의
def calc(a,b):
    return a+b, a*b

#함수를 호출
result = calc(3,4)
print(result[0])
print(result[1])

print("id:%s, name:%s" % ("kim","김유신"))

print("---set 연습---")
a = {1,2,3,3}
b = {3,4,4,5}
print(a)
print(b)
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

print("---형식 변환---")
b = set((1,2,3))
print( type(b) )
print(b)
c=list(b)
c.append(4)
print(c)

color={"apple":"red", "banana":"yellow"}
print(len(color))
print(color["banana"])
color["cherry"]="red"
print(color)
del color["apple"]
print(color)
