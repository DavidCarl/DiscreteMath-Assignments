def main():
    a = [1,2,3,4,5,6,7,8,9]
    b = [1,2,3,4,5,6,7,8,9]
    print('Same: ', compare(a, b))
    print('A is subset of B:', compare(a[1:],b))
    print('B is subset of A:', compare(a,b[:-2]))

def compare(a, b):
    if len(a) is len(b): 
        return 0 if sub_comp(a, b) else -2
    elif len(a) > len(b): 
        return 1 if sub_comp(a, b) else -2
    else: 
        return -1 if sub_comp(b, a) else -2

def sub_comp(a, b):
    for i in b:                
        if i not in a:
            return False
    return True