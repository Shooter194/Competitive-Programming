def ispar(x):
    # code here
    stack = []
    pre_dict = {'}' : '{', ')' : '(', ']' : '['}
    balance = True
    for pre in x:
        if pre in pre_dict.values():
            stack.append(pre)
        elif (len(stack) == 0):
            balance = False
            break
        else:
            top = stack.pop()
            if top != pre_dict.get(pre):
                balance = False
                break
                
    if len(stack) == 0 and balance:
        return "balanced"
    else:
        return "unbalanced"
        
print(ispar("{{}]"))
