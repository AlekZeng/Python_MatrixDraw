#######################
#Author:Alek Zeng
#Date: 03/20/2018
########################
global MatrixSize  #Sets the size of the matrix
global matrix #Initial matrix array
matrix=[]
MatrixSize = 50

def CreateMatrix(): #defines function that creates the matrix
    
    for x in range(MatrixSize):    
        matrix.append([])
        for n in range(MatrixSize):
            matrix[x].append(1)

def DrawMatrix():  # Defines function that prints out the final matrix,AKA the driver
    for n in range(MatrixSize):    
        for x in matrix[n]:
            if x==0:
                print(" ",end="")
            elif x==1:
                print("*" ,end="")
        
        print()
        
        
def SetValueMatrix(x,y,value): #function used to change things in the matrix
    matrix[y][x] = value

def DrawDiamond(x,y,n,z):  #creates diamond in the matrix  
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
      
def DiamondOutline(x,y,n,t): #creates an outlined diamond in the matrix

    DrawDiamond(x,y,n,0)        
    DrawDiamond(x+t,y+t,n-t,1)

CreateMatrix() # Form intial matrix
DiamondOutline(7,5,8,1) #adds outlined diamond to matrix
DiamondOutline(10,5,8,1) #adds outlined diamond to matrix
DrawMatrix() # prints out the final matrix
