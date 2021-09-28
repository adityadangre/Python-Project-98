#Function to Swap file data
def swapFileData(f1,f2): #Taking props as f1 and f2
    try:
        with open(f1, "r") as file1: #Reading f1
            data1 = file1.read()
        
        with open(f2, "r") as file2: #Reading f2
            data2=file2.read()

        with open(f1, "w") as file1: #Writing f1
            file1.write(data2)

        with open(f2, "w") as file2: #Writing f2
            file2.write(data1)
        
        print("Swpping of file is sucessfully done!!!") #After swapping, a message
    
    except IOError: #If file not found, a message
        print('File not Found!!!')

#Main Program
#Taking input of f1 and f2 through user
f1=input("Name of 1st File: ")
f2=input("Name of 2nd File: ")

if(f1==f2): #If file name is same, a message
    print("Please give different file names to swap!!!")
else: #else call the swapFileData function
    swapFileData(f1, f2)