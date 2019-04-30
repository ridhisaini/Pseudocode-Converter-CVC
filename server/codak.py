key_word={"Promot":"input()","print":"print"}
string_operations={"add":"+","sub":"-","mul":"*","div":"/","mod":"%" }
operations = ["+" , "-" , "*" , "/"] 
key=["number","string"]

# compiler function to python code
""" arguments -->
    input_ : this is the input file of sudocode resulted from preprocessing stage
    result : the output file which contains python code will be appear to the user and comiled
    exec_file : this file contains the code will send to the client from server in the background
    """
def compile_sudo (input_ , result, exec_file):
    indent = 0
    text = input_.readline().rstrip('\n')
    while text:
        text_list = text.split()
        if ((text_list[0]) == ("endfor"))  :
            indent = indent - 1
            text = input_.readline().rstrip('\n')
            continue

        #this is because the indents python take instead of brackets
        result.write("   " * indent)
        exec_file.write("   " * indent)
        print("   " * indent ,end = "")
 
        #promot use to take input from user
        if text_list[0] == "Promot" :
            result.write('print("Please Enter your input:")\r\n')
            exec_file.write("c.send(bytes('Please Enter your input:','utf8'))\r\n")
            exec_file.write("c.send(bytes('input','utf8'))\r\n")
            exec_file.write("ack=c.recv(1024)\r\n")
            exec_file.write("user_input=c.recv(1024).decode()\r\n")

            temp= key_word[text_list[0]]
            #this if when the user input interger number
            if(key[0] in text_list):

                text = input_.readline().rstrip('\n')
                text_list = text.split(" ")
                if text_list[0] == "Save" :
                    str1 = text_list[-1]
                    print(str1,"=int(",temp,")")
                    result.write("%s =int( %s )\r\n" %(str1,temp))
                    exec_file.write("%s =int( user_input )\r\n" %(str1))
                    
            #this if when the user input string
            else :
                if text_list[0] == "Save" :
                    str1 = text_list[-1]
                    print(str1,"=",temp)
                    result.write("%s = %s \r\n "%(str1,temp))
                    exec_file.write("%s = user_input \r\n "%(str1))

        #print use to print the output to the user in ui             
        elif text_list[0] == "print" :
            str1 = ' '.join(text_list[1:])
            print(key_word[text_list[0]],'(',str1,')')
            result.write("%s ( %s )\r\n"%(key_word[text_list[0]],str1))
            exec_file.write("f = open('out.txt','w+')\r\n")
            exec_file.write("   " * indent)
            exec_file.write("%s (%s  , file = f ) \r\n" %(key_word[text_list[0]],str1.lstrip()))
            exec_file.write("   " * indent)
            exec_file.write("f.close()\r\n")
            exec_file.write("   " * indent)
            exec_file.write("f = open('out.txt','r+')\r\n")
            exec_file.write("   " * indent)
            exec_file.write("s = f.readline().rstrip('\\n ')\r\n")
            exec_file.write("   " * indent)
            exec_file.write("print(s)\r\n")
            exec_file.write("   " * indent)
            exec_file.write("c.send(bytes(s,'utf8'))\r\n")
            exec_file.write("   " * indent)
            exec_file.write("print(bytes(s,'utf8'))\r\n")
            exec_file.write("   " * indent)
            exec_file.write("ack=c.recv(1024)\r\n")
            exec_file.write("   " * indent)
            exec_file.write("f.truncate(0)\r\n")
            exec_file.write("   " * indent)
            exec_file.write("f.close()\r\n")
        
        #the operation dictionary for equation statments
        elif([i for i in operations if i in text_list]):
            temp=' '.join(text_list)
            print(temp)
            result.write("%s\r\n"%(temp))
            exec_file.write("%s\r\n"%(temp))
        
        #initialize use to initialize lists with fixed size 100
        elif text_list[0] == "initialize" :
            print(text_list[1] , "= [0]*100")
            result.write("%s = [0]*100 \r\n"%(text_list[1]))
            exec_file.write("%s = [0]*100 \r\n"%(text_list[1]))


        #for loop in format of "for i in range(x,y):"
        elif text_list[0] == "for" :
            indent =  indent + 1    #increase the indent counter after for statement
            iterator = text_list[1]
            item = text_list.index(next(i for i in key if i in text_list))
            if(text_list[item]=="to"):
                print("for" , iterator ,"in range(",text_list[item-1],',',int(text_list[item+1])+1,'):')
                result.write("for %s in range (%s,%d) :\r\n" %( iterator ,(text_list[item-1]),(int(text_list[item+1])+1)))
                exec_file.write("for %s in range (%s,%d) :\r\n" %( iterator ,(text_list[item-1]),(int(text_list[item+1])+1)))


       #reading new line in input file
        text = input_.readline().rstrip('\n')


    # close files and return result file to execute
    result.close()
    exec_file.close()
    return result


