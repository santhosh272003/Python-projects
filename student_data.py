with open(r'C:\Users\nirma\git Python projects\Python-projects\student_data.txt','w') as s:
    s.write('sno,Name,Age,Mark\n')
    s.write('1,Karthic,60,0\n')
    s.write('2,srikanth,85,1\n')
    s.write('3,jayabalan,21,100\n')
    s.write('4,srinivasan,21,99\n')
    s.write('5,rahman,35,8\n')
    s.write('6,Hari,50,10\n')
    s.write('7,sarathi,35,45\n')
    s.write('8,Dravid,50,100\n')
    s.write('9,santhosh,98,90\n')
    s.write('10,Rahul,50,10\n')
    s.write('11,solai,60,99\n')
    s.write('12,Pasumali,60,100\n')             
    s.close()

with open(r'C:\Users\nirma\git Python projects\Python-projects\student_data.txt','r') as n:
    out=n.readline().rstrip('\n').split(',')
    print(out)
    result=[]
    Age_res=[]
    fail_res=[]
    age=[]
    agename=[]
    
    
    for line in n:
        #print(line)
        title=line.rstrip('\n').split(',')
        #print(title)
        data_dict={}
        data_dict[out[0]]=title[0]
        data_dict[out[1]]=title[1]
        data_dict[out[2]]=int(title[2])
        data_dict[out[3]]=int(title[3])
        #print(data_dict)
# 1. 
        if title[1][0]=='s':
            result.append(title)
    
# 2.
        if data_dict[out[2]]>=50:
            Age_res.append(title)
#3.
        if int(title[3])<35:
            fail_res.append(title)
#4.
        if data_dict[out[2]]==50:
            age.append(title)  
#5.
        if title[1][-1] in 'aeiouAEIOU':
            agename.append(title)
            
            
            
   
    print("1. How many Students name are starting with 'S'?")
    print()
    print(out)
    for s in result:
        print(s)
    print()

    print(" 2. How many Students are above age>=50 ?")
    print()
    print(out)
    for a in Age_res:
        print(a)
    print()

    print("3.How many students are failed in the exam ?")
    print()
    print(out)
    for n in fail_res:
        print(n)
    print()

    print("4.Names of the Students whose age is 50 ?")
    print()
    print(out)
    for d in age:
        print(d)
    print()

    print("5.Age and marks of the students whose names are ending with vowel?")
    print()
    print(out)
    for y in agename:
        print(y)

    
        
    
        
    
        

            
    

        

    
    


    
