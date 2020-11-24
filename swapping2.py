def swap():
    Input1 = input("Enter the name of file1 - ")
    Input2 = input("Enter the name of file2 - ")
    data1 = open(Input1)
    content1 = data1.read()
    data2 = open(Input2)
    content2 = data2.read()
    d1 = open(Input1,'w')
    c1 = d1.write(content2)
    d2 = open(Input2,'w')
    c2 = d2.write(content1)
    

swap()    