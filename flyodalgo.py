def min(a,b):
    if a<b:
        return a
    else:
        return b

def flyodalg(arr,n):
    for k in range(0,n+1):
        for i in range(0,n+1):
            for j in range(0,n+1):
                arr[i][j]=min(arr[i][j],arr[i][k]+arr[k][j])

    for i in range(0,n+1):
        for j in range(0,n+1):
            print(" ",arr[i][j],end="")
        print("")

arr=[[0   ,2   ,9999,1   ,8   ],
     [6   ,0   ,3   ,2   ,9999],
     [9999,9999,0   ,4   ,9999],
     [9999,9999,2   ,0   ,3   ],
     [3   ,9999,9999,9999,0   ],
    ]
n=4
print("given matrix is:")
for i in range(0,n+1):
        for j in range(0,n+1):
            print(" ",arr[i][j],end="")
        print("")
print("matrix after applying flyod's algorithm is:")
flyodalg(arr,4)

arr1=[[0   ,9999,1   ,1   ,8   ],
     [6   ,0   ,3   ,2   ,9999],
     [9999,9999,0   ,4   ,9   ],
     [7   ,9999,2   ,0   ,3   ],
     [3   ,8   ,9999,9999,0   ],
    ]
print()
print("given matrix is:")
for i in range(0,n+1):
        for j in range(0,n+1):
            print(" ",arr1[i][j],end="")
        print("")
print("matrix after applying flyod's algorithm is:")
flyodalg(arr1,4)








