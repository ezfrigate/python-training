def fun(a,b,c):
    print("a is : " + a)
    print("b is : " + b)
    print("c is : " + c)

list = ["a","b","c"]
# fun(list) will throw err but
fun(*list) #explode list

d = {'a' : "aaa", 'b': "bbb", 'c': "ccc"}
fun(**d) #key MUST match the param name 