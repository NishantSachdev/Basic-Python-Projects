import mysql.connector
pydb= mysql.connector.connect(host = "localhost", user = "root", password = "n&ss1819", database ="studentdatabase")
mycursor = pydb.cursor()

print("Welcome to Student Database System")

def admin_opt1():
    mycursor.execute("show tables in studentdatabase")
    print("")
    for x in mycursor:
        print(x)

def admin_opt2():
    mycursor.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'student_info'")
    print("")
    for x in mycursor:
        print(x)

def admin_opt3():
    mycursor.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'student_marks'")
    print("")
    for x in mycursor:
        print(x)

def admin_opt4():
    print("")
    mycursor.execute("select * from student_info")
    myresult=mycursor.fetchall()
    for x in myresult:
        print(x)

def admin_opt5():
    print("")
    mycursor.execute("select * from student_info")
    myresult=mycursor.fetchall()
    for x in myresult:
        print(x)

def admin_opt6():
    print("")
    id= input("Enter student id: ")
    name= input("Enter student name: ")
    email= input("Enter student email: ")
    roll= input("Enter student roll: ")
    branch= input("Enter student branch: ")
    semester= input("Enter student semester: ")
    query_vars1=(id,name,email,roll,branch,semester)
    mycursor.execute("insert into student_info (id,name,email,roll,branch,semester) values (%s,%s,%s,%s,%s,%s)",query_vars1)
    pydb.commit()
    print("Success")

def admin_opt7():
    print("")
    id= input("Enter student id: ")
    sub1= input("Enter marks for sub1: ")
    sub2= input("Enter marks for sub2: ")
    sub3= input("Enter marks for sub3: ")
    sub4= input("Enter marks for sub4: ")
    sub5= input("Enter marks for sub5: ")
    sub6= input("Enter marks for sub6: ")
    query_vars2=(id,sub1,sub2,sub3,sub4,sub5,sub6)
    mycursor.execute("insert into student_marks (id,sub1,sub2,sub3,sub4,sub5,sub6) values (%s,%s,%s,%s,%s,%s,%s)",query_vars2)
    pydb.commit()
    print("Success")

def admin_opt8():
    print("")
    del_id1= tuple(input("Enter the ID of student whose information is to be deleted: "))
    mycursor.execute("delete from student_info where id = %s",del_id1)
    pydb.commit()
    print("Success")

def admin_opt9():
    print("")
    del_id2= tuple(input("Enter the ID of student whose marks are to be deleted: "))
    mycursor.execute("delete from student_marks where id = %s",del_id2)
    pydb.commit()
    print("Success")

def admin_opt10():
    print("")
    opt_inp1=input("Select what you want to update: \n1.name \n2.email \n3.roll \n4.branch \n5.semester \n")
    upd_val1=input("Enter the updated value: ")
    upd_id1=input("Enter the ID of the student whose information is to be updated: ")
    query_vars3=(upd_val1,upd_id1)
    if opt_inp1=="1":
        mycursor.execute("update student_info set name = %s where id = %s",query_vars3)
        pydb.commit()
    if opt_inp1=="2":
        mycursor.execute("update student_info set email = %s where id = %s",query_vars3)
        pydb.commit()
    if opt_inp1=="3":
        mycursor.execute("update student_info set roll = %s where id = %s",query_vars3)
        pydb.commit()
    if opt_inp1=="4":
        mycursor.execute("update student_info set branch = %s where id = %s",query_vars3)
        pydb.commit()
    if opt_inp1=="5":
        mycursor.execute("update student_info set semester = %s where id = %s",query_vars3)
        pydb.commit()

def admin_opt11():
    print("")
    opt_inp2=input("Select what you want to update: \n1.sub1 \n2.sub2 \n3.sub3 \n4.sub4 \n5.sub5 \n6.sub6 \n")
    upd_val2=input("Enter the updated value: ")
    upd_id2=input("Enter the ID of the student whose information is to be updated: ")
    query_vars4=(upd_val2,upd_id2)
    if opt_inp2=="1":
        mycursor.execute("update student_marks set sub1 = %s where id = %s",query_vars4)
        pydb.commit()
    if opt_inp2=="2":
        mycursor.execute("update student_marks set sub2 = %s where id = %s",query_vars4)
        pydb.commit()
    if opt_inp2=="3":
        mycursor.execute("update student_marks set sub3 = %s where id = %s",query_vars4)
        pydb.commit()
    if opt_inp2=="4":
        mycursor.execute("update student_marks set sub4 = %s where id = %s",query_vars4)
        pydb.commit()
    if opt_inp2=="5":
        mycursor.execute("update student_marks set sub5 = %s where id = %s",query_vars4)
        pydb.commit()


print("Choose your action: \n1.Show Tables \n2.Show Columns From student_info Table \n3.Show Columns From student_marks Table \n4.Show student_info database \n5.Show student_marks database \n6.Insert Student Information \n7.Insert Student Marks \n8.Delete Student Information \n9.Delete Student Marks \n10.Update Student Information \n11.Update Student Marks \n")
option=input("Enter your Action: ")
if option=="1":
    admin_opt1()
elif option=="2":
    admin_opt2()
elif option=="3":
    admin_opt3()
elif option=="4":
    admin_opt4()
elif option=="5":
    admin_opt5()
elif option=="6":
    admin_opt6()
elif option=="7":
    admin_opt7()
elif option=="8":
    admin_opt8()
elif option=="9":
    admin_opt9()
elif option=="10":
    admin_opt10()
elif option=="11":
    admin_opt11()




    


