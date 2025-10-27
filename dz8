#1
def pol(a):
    def _rpn_to_pn(f):
        stack = []
        opecys = str(f).split()
        for token in opecys:
            if token.replace('.', '', 1).isdigit():
                stack.append(token)
            elif token in {'+', '-', '*', '/'}:
                b = stack.pop()
                a = stack.pop()
                stack.append(f"{token} {a} {b}")
        return stack
    a = a.split()
    output = []
    stack = []
    d = {"^": (4, "r"), "*": (3, "l"), "/": (3, "l"), "+": (2, "l"), "-": (2, "l")}
    for i in a:
        if i.isdigit():
            output.append([i])
        else:
            if len(stack) == 0:
                stack.append(i)
            elif i == "(":
                stack.append(i)
                continue
            elif i == ")":
                g = stack
                for j in range(len(g) - 1, 0, -1):
                    if g[-1] != "(":
                        output.append(g[-1])
                        stack.pop(j)
                    else:
                        stack.pop(j)
                        break
                continue
            else:
                k = len(stack)
                for j in range(k):
                    if stack[-1] == "(":
                        continue
                    if d[stack[-1]][0] >= d[i][0] and d[stack[-1]][1] == "l":
                        output.append(stack[-1])
                        stack.pop(-1)
                stack.append(i)
    for i in sorted(stack, reverse=True):
        if i != "(":
            output.append(i)
    res = ""
    for i in output:
        if type(i) == list:
            for j in i:
                res+=j
        else:
            res+=str(i)
        res+=" "
    res = res[:-1]
    return res, *_rpn_to_pn(res)



print(*pol("( 2 - 3 ) * ( 12 - 10 ) + 4 / 2"), sep="\n")


#2
def stec_calc(inp):
    stack = []
    operas = inp.split()
    for opera in operas:
        if opera.replace('.', '', 1).replace('-', '', 1).isdigit() or \
                (opera.startswith('-') and opera[1:].replace('.', '', 1).isdigit()):
            stack.append(float(opera))
        elif opera in {'+', '-', '*', '/', '^'}:
            b = stack.pop()
            a = stack.pop()
            if opera == '+':
                result = a + b
            elif opera == '-':
                result = a - b
            elif opera == '*':
                result = a * b
            elif opera == '/':
                result = a / b
            elif opera == '^':
                result = a ** b
            stack.append(result)
    return stack[0]


print(stec_calc("1 2 3 * + 4 -"))



#3
a = "10 + 5 * 3 - 6"
a = a.split()
output = []
stack = []
d = {"^": (4, "r"), "*": (3, "l"), "/": (3, "l"), "+": (2, "l"), "-": (2, "l")}
for i in a:
    if i.isdigit():
        output.append([i])
    else:
        if len(stack) == 0:
            stack.append(i)
        elif i == "(":
            stack.append(i)
            continue
        elif i == ")":
            g = stack
            for j in range(len(g) - 1, 0, -1):
                if g[-1] != "(":
                    output.append(g[-1])
                    stack.pop(j)
                else:
                    stack.pop(j)
                    break
            continue
        else:
            k = len(stack)
            for j in range(k):
                if stack[-1] == "(":
                    continue
                if d[stack[-1]][0] >= d[i][0] and d[stack[-1]][1] == "l":
                    output.append(stack[-1])
                    stack.pop(-1)
            stack.append(i)
for i in sorted(stack, reverse=True):
    if i != "(":
        output.append(i)
for i in output:
    if type(i) == list:
        print(i[0], end=" ")
    else:
        print(i, end=" ")
