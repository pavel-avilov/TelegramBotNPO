def cost(str):
    for i in reversed(range(0, len(str), 3)):
        try:
            print(str[i], end=' ')
        except:
            print(str[i], end=' ')
number = '421234569'
a = "{:,}".format(number)

print(a)

cost('4569')
