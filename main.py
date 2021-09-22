l=[]
class main:
    def items():
        lim=int(input("Enter the size of the array:"))
        for i in range(1,lim+1):
            l1=int(input("enter the numbers:"))
            l.append(l1)
        print("your array is:",l)
        p=int(input("enter the element that you want to check:"))
        if p in l:
            print(p,"is presented in this array so the resulting index is:::",l.index(p))
        else:
            l.append(p)
            l.sort()
            print("The resulting index is:::",l.index(p),"as that's the only place to insert",p,"which satisfy the arrays condition ")
            print("your final array is:")
            print(l)
            
        
x=main
x.items()

