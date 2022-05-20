def SwapFileData():
    file_1=input("Enter the file name 1:")
    file_2=input("Enter the file name 2:")


    with open(file_1,'r') as a:

       data_a = a.read() 
       
    with open(file_2,'r') as b:
            data_b = b.read()


    with open(file_1,'w') as a:
     a.write(data_b)

    with open(file_2,'w') as b:
     b.write(data_a)

    
SwapFileData()