n = 3 # Set amount of disk here

# n is number of disks
# f is from
# t is to
# a is auxiliary
def move(n, f, t, a):
    if n == 1:
        print('Move disk 1 from', f, 'to', t)
        return
    move(n-1, f, a, t)
    print('Move disk', n, 'from', f, 'to', t)
    move(n-1, a, t, f)

def towerOfHanoi():
    move(n, 'A', 'C', 'B')

towerOfHanoi()