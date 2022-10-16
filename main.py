

# uzdevums 1
 
try:
    file1 = open("admin.txt")
    s = (file1.read())
   
except FileNotFoundError:
    print("not possible open file")
  
try:
    file2 = open("viesis.txt")
    s+= (file2.read())
except FileNotFoundError:
    print("not possible open file")
  
file1.close()
file2.close()


with open('final.txt', 'wt') as file3:
    file3.write(s)

file3.close()


 
try:
    file3 = open("final.txt")
    print("atbilde uz 1 uzdevumu,kopigs saturs no diviem failem,no jauna faila\n")
    print(file3.read())
   
except FileNotFoundError:
    print("not possible open file")

file3.close

#uzdevums 2


 
try:
    file2 = open("admin.txt")
    s2=file2.read()
    word_list= s2.split()
    num_list = [int(num) for num in filter(
        lambda num: num.isnumeric(), word_list)]
    print("atbilde uz 2 uzdevumu\n")
    print("Average admin age : ",int(sum(num_list)/len(num_list)))
    print("Most oldest admin : ",max(num_list))
    print("Most youngest admin : ",min(num_list))
    print("")
          
except FileNotFoundError:
    print("not possible open file")

file2.close

#uzdevums 3

 
try:
    file3 = open("final.txt")
    s3=file3.read()
    print("atbilde uz 3 uzdevumu\n")
    print("Admin skaitliska vertiba : ",s3.count("admin"))
    print("Viesis skaitliska vertiba : ",s3.count("guest")) 
except FileNotFoundError:
    print("not possible open file")

file3.close


