'''
Michael Mcmanimon
shapes
'''

shape = input("what type of shape do you want to draw?: ")


#Triangle 

while shape == "triangle" :
    
    num = int(input("Enter the number of rows:"))
    for i in range(1,num+1):
            for j in range(1,i+1):
                print("*",end = "")
            print()

            
#Line
            
while shape == "line":

    num = int(input("Enter the length:"))
    for i in range(1,num+1):
        print("*",end = "")
    print()

    
    
#Square
    
while shape == "square":
    
    row = abs(eval(input('Enter height: ')))
    col = abs(eval(input('Enter width: ')))
    print ('*'*col)

    for i in range (row-2):
      print ('*'+' '*(col-2)+'*')
    print ('*'*col)
    

#pyramid
    
while shape == "pyramid":

    k = 0
    rows = int(input("Enter the desired number of rows: "))
    for i in range(1, rows+1):
        for space in range(1, (rows-i)+1):
            print(end="  ")
        while k != (2*i-1):
            print("* ", end="")
            k = k + 1
        k = 0
        print()

