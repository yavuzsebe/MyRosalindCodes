def product(x):
        final = [[]]
        l = 3 #needs to be routed
        groups = [list(x)] * l
        for i in groups:
            final = [x+[y] for x in final for y in i]
        for k in final:
            yield "".join(k)


list1=list(product("ABCDEFG")) #needs to be routed
for el in list1:
    print(el)
