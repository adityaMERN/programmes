s=str(input())
stack=[]
for i in s:
    if i in ['[','{','(']:
        stack.append(i)
    elif i==')' and len(stack)!=0 and stack[-1]=='(':
        stack.pop()
    elif i=='}' and len(stack)!=0 and stack[-1]=='{':
        stack.pop()
    elif i==']' and len(stack)!=0 and stack[-1]=='[':
        stack.pop()
    else:
        print(False)
if not len(stack):
    print(True)
else:
    print(False)