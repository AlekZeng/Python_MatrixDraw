global MatrixSize
global matrix
matrix=[]
MatrixSize = 50

def CreateMatrix(): 
    
    for x in range(MatrixSize):    
        matrix.append([])
        for n in range(MatrixSize):
            matrix[x].append(1)

def DrawMatrix():    
    for n in range(MatrixSize):    
        for x in matrix[n]:
            if x==0:
                print(" ",end="")
            elif x==1:
                print("*" ,end="")
        
        print()
        
        
def SetValueMatrix(x,y,value):
    matrix[y][x] = value
    #Truexy=(y*MatrixSize)-(MatrixSize-x)
    #matrix.insert((Truexy),value)


def DrawDiamond(x,y,n,z):    
    global removeSP
    removeSP=1
    SP=1
    for row in range(n):
        for star in range(1,row):
            SetValueMatrix(x+n-removeSP,y+row,z)
            for sec in range(star):
                SetValueMatrix(x+n-removeSP+sec,y+row,z)
            removeSP=removeSP-1
        removeSP=1
        removeSP=removeSP+SP
        SP=SP+1 
    SP=1
    removeSP=n+1
    for row in range(n,2*n):
        for star in range(1,2*n-row):
            SetValueMatrix(x+n-removeSP,y+row,z)
            for sec in range(star):
                SetValueMatrix(x+n-removeSP+sec,y+row,z)
            removeSP=removeSP-1
        removeSP=n+1
        removeSP=removeSP-SP
        SP=SP+1
      
def DiamondOutline(x,y,n,t):

    DrawDiamond(x,y,n,0)        
    DrawDiamond(x+t,y+t,n-t,1)

CreateMatrix()
DiamondOutline(7,5,8,1)
DiamondOutline(10,5,8,1)
DrawMatrix()
