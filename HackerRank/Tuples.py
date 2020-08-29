n = int(input())
mytuple = map(int,input().split())
mytuple = tuple(mytuple)
print(hash(mytuple))