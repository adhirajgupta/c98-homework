

def swap():
    data1 = open("file1.txt",'r')
    content1 = data1.read()
    data2 = open("file2.txt",'r')
    content2 = data2.read()
    dat1 = open("file1.txt",'w')
    conten1 = dat1.write(content2)
    dat2 = open("file2.txt",'w')
    conten2 = dat2.write(content1)
       
swap()    


