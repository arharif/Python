if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    perm = []
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if (i+j+k)!=n:
                    perm.append([i,j,k])
                
    print(perm)
 
# Method 2
# arr = [[X, Y, Z] for X in range(x+1) for Y in range(y+1) for Z in range(z+1) if X + Y + Z != N]