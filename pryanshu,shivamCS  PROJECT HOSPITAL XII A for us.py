'''PLS RUN THIS IN POWERSHELL OR CMD BEFORE RUNNING THE PROGRAM(active internet conn. required)
 
set TABULATE_INSTALL=lib-only 
pip install tabulate          
'''
print('-------------"WELCOME TO OUR VIRTUAL PSP HOSPITAL"--------------')   
H='''      
                       |----HOSPITAL---|
                       I_I_I_I_I_I_I_I_I    
                  +    |---------------|    +
                |---|  ||-| |-| |-| |-||  |---|
      _________|-----|_|---------------|_|-----|_________
      I_I_I_I_I_I_I_I|I_I_I_I_I_I_I_I_I_I|I_I_I_I_I_I_I_|
      |-------|------|-------------------|------|-------|
      ||-| |-||  |-| ||-| |-| |-| |-| |-|| |-|  ||-| |-||
    ((|-------|------|-------------------|------|-------|))
    ()|  |_|  |  |_| |::::: ------- :::::| |_|  |  |_|  |()
    ))|  |_|  |  |_| | |_| |_.-"-._| |_| | |_|  |  |_|  |((
    ()|-------|------| |_| | | | | | |_| |------|-------|()
    @@@@@@@@@@@@@@@@@|-----|_|_|_|_|-----|@@@@@@@@@@@@@@@@@
    PSP             @@@@/=============\@@@@
                           /       \                         '''
print(H)
def map():
    print('''          
         __________________________________________________________________________
        │PHARMACY│   │7A│7B│7C│7D│7E│7F│       ____________  │          │         │ 
        │________║   ║__│__│__│__│__│__│      │            │ │CAFETERIA │         │   
        │        │    _____________________   ║            │ │__________│         │
        │     ___│   ║DC1 │ DC3 │ DC5 │ DC7│  │  SURGERY   │            ║  PATIENT│
        │ICU  │      │____│_____│_____│____║  │            │            │    WARD │
        │     │      ║DC2 │ DC4 │ DC6 │ DC8│  ║            │            │         │
        │     │      │____│_____│_____│____║  │____________│            ║         │
        │_____│______                                                   │         │                      
        │            ║______________                                    │         │                                                
........│            │      │       │              _________________    │         │
. DROP  │  EMERGENCY │      │       │            │CASHIER │        ║    ║         │
. OF    ║            │      │WAITING│            │________│___ADMIN│____│         │
.CANOPY ║            │X-RAY │ROOM   ║            │REGISTRATION║    │ IT │         │  
........│____________│______│_______│            │____________│____│____│_________│                 
                                    │                   │
                                    │    MAIN LOBBY     │
                                    │_______     _______│
                                           /     \                             ''')
import mysql.connector
mydb=mysql.connector.connect(host='localhost',
                             user='root',
                             password='9457')
cur=mydb.cursor()
d=cur.execute('show databases')
f=cur.fetchall()
db=0
for i in f:
    if i[0]=='myhp':
        db=1
if db!=1:        
    cur.execute('create database myhp')
mydb=mysql.connector.connect(host='localhost',user='root',password='9457',database='myhp')
def patienttable():
    cur=mydb.cursor()
    t=cur.execute('show tables')
    r=cur.fetchall()
    tb=0
    for i in r:
        if i[0]=='patient':
            tb=1
    if tb!=1:
        s="create table patient(phno varchar(11) primary key,pname varchar(50),address varchar(100),IDPROOF varchar(15))"
        cur.execute(s)
def patient():
    cur=mydb.cursor()
    patienttable()
    no=input('ARE YOU VISITING OUR HOSPITAL FOR THE FIRST TIME? (Y or N)')    
    if no in 'Yy':
        print('Please fill your entries given below(IN BLOCK LETTERS)')
        i='insert into patient values(%s,%s,%s,%s)'
        global ph
        ph=int(input('enter phone no.'))
        na=input('enter your name')
        ad=input('enter your address')
        idp=input('enter any valid id proof')
        p1=(ph,na,ad,idp)
        cur.execute(i,p1)
        mydb.commit()
        choice()
    if no in 'Nn':
        from tabulate import tabulate
        ph=int(input('enter your phone number to login'))
        s='select * from patient where phno like %s'
        t=(ph,)
        cur.execute(s,t)
        result=cur.fetchall()
        if result==[]:
            print('no such record exist pls enter correct details or register as new patient')
            patient()
        else:
            print(tabulate(result, headers=['Patient Name','Phone No.','address','ID Proof'], tablefmt='psql'))  
            choice()
def choice():
    cur=mydb.cursor()
    c=input('enter A to get a appointment with a doctor or press C for any medical test')
    if c in 'cC':
        test=input('FOR BODY TEMPERATURE CHECK- PRESS 1 \n BLOOD PRESSURE- PRESS 2 \n BLOOD TEST- PRESS 3 \n EYESIGHT CHECKUP-PRESS 4 \n X-RAY- PRESS 5 \n ULTRASOUND- PRESS 6 \n MAGNETIC RESONANCE IMAGING(MRI)- PRESS 7')
        if test=='1':
            print('YOUR TESTING FEES IS ₹150 you are requested to proceed to cashier to pay the fees and get the coupon for the test')
            print('you may proceed to room no. 7A  to get your TEMPERATURE checked')
            m=input('press M to see the hospital map otherwise press any number key')
            if m in 'Mm':
                map()
            else:
                x=0
            exit()    
        if test=='2':
            print('YOUR TESTING FEES IS ₹200 you are requested to proceed to cashier to pay the fees and get the coupon for the test')
            print('you may proceed to room no. 7B  to get your BLOOD PRESSURE checked')
            m=input('press M to see the hospital map otherwise press any number key')
            if m in 'Mm':
                map()
            else:
                x=0
            exit()
        if test=='3':
            print('YOUR TESTING FEES IS ₹1000 you are requested to proceed to cashier to pay the fees and get the coupon for the test')
            print('you may proceed to room no. 7B to get your BLOOD TEST done')
            m=input('press M to see the hospital map otherwise press any number key')
            if m in 'Mm':
                map()
            else:
                x=0
            exit()
        if test=='4':
            print('YOUR TESTING FEES IS ₹350 you are requested to proceed to cashier to pay the fees and get the coupon for the test')
            print('you may proceed to room no. 7E  for your EYESIGHT CHECKUP')
            m=input('press M to see the hospital map otherwise press any number key')
            if m in 'Mm':
                map()
            else:
                x=0
            exit()    
        if test=='5':
            print('YOUR TESTING FEES IS ₹1200 you are requested to proceed to cashier to pay the fees and get the coupon for the test')
            print('you may proceed to room no. 7C to get your X-RAY done')
            m=input('press M to see the hospital map otherwise press any number key')
            if m in 'Mm':
                map()
            else:
                x=0
            exit()
        if test=='6':
            print('YOUR TESTING FEES IS ₹2500 you are requested to proceed to cashier to pay the fees and get the coupon for the test')
            print('you may proceed to room no. 7D  to get your ULTRASOUND done')
            m=input('press M to see the hospital map otherwise press any number key')
            if m in 'Mm':
                map()
            else:
                x=0
            exit()    
        if test=='7':
            print('YOUR TESTING FEES IS ₹6000 you are requested to proceed to cashier to pay the fees and get the coupon for the test')
            print('you may proceed to room no. 7F  to get your MRI done')
            m=input('press M to see the hospital map otherwise press any number key')
            if m in 'Mm':
                map()
            else:
                x=0
            exit()
    if c in 'aA':
        appointments()
def apptab():
    cur=mydb.cursor()
    t=cur.execute('show tables')
    r=cur.fetchall()
    tb=0
    for i in r:
        if i[0]=='appointments':
            tb=1
        if tb!=1:
            s="create table appointments(pname varchar(50),phno varchar(11),doctor varchar(20))"
            cur.execute(s)
def appointments():
    cur=mydb.cursor()
    i='insert into appointments values(%s,%s,%s)'
    x='y'
    while x in 'yY':
        cur=mydb.cursor()
        na=input('please enter your name')
        da=input('please enter with which doctor you want appointment:(neurologist,surgeon,cardiologist,psychiatrist,audiologist,radiologist )')
        p1=(na,ph,da)
        cur.execute(i,p1)
        mydb.commit()
        if da=='neurologist':
            print('you may proceed to room no. DC1 for your appointment')
            m=input('press M to see the hospital map otherwise press any number key')
            if m in 'Mm':
                map()
                x=input('want to book more appointments(y/n)')
            else:
                x=input('want to book more appointments(y/n)') 
        elif da=='psychiatrist':
            print('you may proceed to room no. DC2  for your appointment')
            m=input('press M to see the hospital map otherwise press any number key')
            if m in 'Mm':
                map()
                x=input('want to book more appointments(y/n)')
            else:
                x=input('want to book more appointments(y/n)')                
        elif da=='cardiologist':
            print('you may proceed to room no. DC3  for your appointment')
            m=input('press M to see the hospital map otherwise press any number key')
            if m in 'Mm':
                map()
            else:
                x=input('want to book more appointments(y/n)')
        elif da=='audiologist':
            print('you may proceed to room no. DC4  for your appointment')
            m=input('press M to see the hospital map otherwise press any number key')
            if m in 'Mm':
                map()
                x=input('want to book more appointments(y/n)')
            else:
                x=input('want to book more appointments(y/n)')
        elif da=='radiologist':
            print('you may proceed to room no. DC5  for your appointment')
            m=input('press M to see the hospital map otherwise press any number key')
            if m in 'Mm':
                map()
            else:
                x=input('want to book more appointments(y/n)')
        elif da=='surgeon':
            print('you may proceed to room no. DC5  for your appointment')
            m=input('press M to see the hospital map otherwise press any number key')
            if m in 'Mm':
                map()
                x=input('want to book more appointments(y/n)')
            else:
                x=input('want to book more appointments(y/n)')
        else:
            print("Pls mention a valid doctor")
    mexit()
def exit():
    e=input('To go to PREVIOUS MENU press P,To go to MAIN MENU press M or press E to exit')
    if e in 'pP':
        choice()
    if e in 'Mm':
        main()
    else:
        feedback()
        quit()
def doctor():
    cur=mydb.cursor()
    t=cur.execute('show tables')
    r=cur.fetchall()
    tb=0
    for i in r:
        if i[0]=='doctor':
            tb=1
    if tb!=1:
        s="create table doctor(ID varchar(15) primary key,dname varchar(50), specialist varchar(50) ,PHNO varchar(15), address varchar(100),country varchar(50))"
        cur.execute(s)
        i='insert into doctor values(%s,%s,%s,%s,%s,%s)'
        d=[('NP01K','Dr.Pryanshu','Neurologist',7078036828,'San francisco california','USA'),('CS02C','Dr.Shivam','Cardiologist',8600001010,'Seattle Washington','USA'),('AP03R','Dr.Aman Raj','Psychiatrist',9451250013,'Cape Town','South Africa'),('VA04T','Dr.Vimal','Audiologist',7542189634,'flat no.198 Burj khalifa','Dubai'),('RA05B','Dr.Amit Bansal','Radiologist',8265487120,'HSR layout Bangalore','India')]
        cur.executemany(i,d)
        mydb.commit()    
def staff():
    cur=mydb.cursor()
    t=cur.execute('show tables')
    r=cur.fetchall()
    tb=0
    for i in r:
        if i[0]=='staff':
            tb=1
    if tb!=1:
        s="create table Staff(sname varchar(50),job varchar(50),PHNO varchar(15) ,address varchar(100))"
        cur.execute(s)
        i='insert into staff values(%s,%s,%s,%s)'
        st=[('Akash','Compounder','9457123820','Fish market Mathura'),('Arvind','Care Assistant','8234516280','Balaji puram'),('Sachin pachara','Ward Boy','8945679538','Gokul Dham Mathura'),('Alia Bhatt','Nurse','7835942685','Andehri Mumbai'),('Somesh kushwah','Coordinator','8750035464','Patna')]
        cur.executemany(i,st)
        mydb.commit()    
def admin():
    v=input('To see all records of PATIENTS press P\nTo see all records of DOCTORS press D\nTo see all records of OTHER STAFF press S\nTo delete records press X\nTo add a new record press A\n To search a record press Sh')
    cur=mydb.cursor()
    staff()
    doctor()
    patienttable()
    def search():
        s=input('To search a record of a PATIENT press P\nTo search a record of a DOCTOR press D\nTo search a record of a STAFF MEMBER press S')
        cur=mydb.cursor()
        if s in 'pP':
            from tabulate import tabulate
            s="y"
            while s in 'yY':
                sp=input("enter phone no of patient to be searched")
                
                u='select * from patient where phno like %s'
                t=(sp,)
                cur.execute(u,t)
                result=cur.fetchall()
                if result==[]:
                    print('no such record exist pls enter correct details')
                else:
                    print(tabulate(result, headers=['PHONE NO.', 'Name','Address','ID PROOF'], tablefmt='psql'))
                    s=input('want to search more records? (y/n)')
        if s in 'dD':
            from tabulate import tabulate
            s="y"
            while s in 'yY':
                sp=input("enter ID of doctor to be searched")
                z='select * from doctor where ID like %s'
                t=(sp,)
                cur.execute(z,t)
                result=cur.fetchall()
                if result==[]:
                    print('no such record exist pls enter correct details')
                    s='y'
                else:
                    print(tabulate(result, headers=['ID','Name','Specialist','PHONE NO.','Address','Country'], tablefmt='psql'))
                s=input('want to search more records? (y/n)')
        if s in 'sS':
            from tabulate import tabulate
            s="y"
            while s in 'yY':
                sp=input("enter phone no of staff to be searched")
                x='select * from staff where phno like %s '
                t=(sp,)
                cur.execute(x,t)
                result=cur.fetchall()
                if result==[]:
                    print('no such record exist pls enter correct details')
                    s='y'
                else:
                    print(tabulate(result, headers=[ 'Name','JOB','PHONE NO.','Address'], tablefmt='psql'))
                s=input('want to search more records? (y/n)')
    from tabulate import tabulate
    cur=mydb.cursor()
    if v in 'Pp':
        s='select * from patient'
        cur.execute(s)
        r=cur.fetchall()
        print("        Total number of patients: ",cur.rowcount)
        print(tabulate(r, headers=['PHONE NO.', 'Name','Address','ID PROOF'], tablefmt='psql'))
        mexit()    
    if v in 'dD':
        s='select * from doctor'
        cur.execute(s)
        d=cur.fetchall()
        print("        Total number of doctors: ",cur.rowcount)
        print(tabulate(d, headers=['ID','Name','Specialist','PHONE NO.','Address','Country'], tablefmt='psql'))
        mexit()    
    if v in 'sS':
        s='select * from staff'
        cur.execute(s)
        e=cur.fetchall()
        print("        Total number of members: ",cur.rowcount)
        print(tabulate(e, headers=[ 'Name','JOB','PHONE NO.','Address'], tablefmt='psql'))
        mexit()
    if v in 'xX':
        x='y'
        while x in 'yY':
            cur=mydb.cursor()
            c=input('To delete records of any DOCTOR press 1\nTo delete records of any STAFF MEMBER press 2')
            if c=='1':
                id=input('enter ID of doctor whose record is to be deleted')
                search='select ID from doctor where id like %s'
                t=(id,)
                cur.execute(search,t)
                rr=cur.fetchall()
                z=0
                if rr==[]:
                    print('record not found pls enter correct details ')
                else:
                    s='delete from doctor where ID like %s'
                    cur.execute(s,t)
                    print('Record deleted Successfully')
                    z=1
                    x=input('do you want to delete more records(y/n)')     
            if c=='2':
                ph=input('enter phno of staff member whose record is to be deleted')
                search='select phno from staff where phno like %s'
                tt=(ph,)
                cur.execute(search,tt)
                rr=cur.fetchall()
                z=0
                if rr==[]:
                    print('record not found pls enter correct details ')
                else:
                    s='delete from staff where phno like %s'
                    cur.execute(s,tt)
                    print('Record deleted Successfully')
                    z=1
                    x=input('do you want to delete more records(y/n)')
        mexit()            
    if v in "aA":
        x='y'
        while x in 'yY':
            cur=mydb.cursor()
            c=input('To ADD records of any DOCTOR press 1\nTo ADD records of any STAFF MEMBER press 2')
            if c=='1': 
                id=input('Enter ID of the  new doctor ')
                search='select ID from doctor where id like %s'
                t=(id,)
                cur.execute(search,t)
                rr=cur.fetchall()
                z=0
                if rr==[]:
                    a='insert into doctor values(%s,%s,%s,%s,%s,%s)'
                    na=input('enter name of doctor')
                    sp=input('enter speciality of doctor')
                    ph=input('enter phone no of doctor')
                    ad=input('enter address of doctor')
                    co=input('enter country of doctor')
                    d=[(id,na,sp,ph,ad,co),]
                    cur.executemany(a,d)
                    mydb.commit()
                    print('record added successfully')
                    x=input('do you want to add more records(y/n)')
                else:
                    print('record already exists pls enter new ID')           
            if c=='2':
                p=input('Enter Phone No. of the new staff member ')
                search='select phno from staff where phno like %s'
                t=(p,)
                cur.execute(search,t)
                rr=cur.fetchall()
                z=0
                if rr==[]:
                    a='insert into staff values(%s,%s,%s,%s)'
                    na=input('enter name of staff member')
                    j=input('enter job of staff member')
                    ad=input('enter address of staff member')
                    d=[(na,j,p,ad),]
                    cur.executemany(a,d)
                    mydb.commit()
                    print('record added successfully')
                    x=input('do you want to add more records(y/n)')           
                else:
                    print('record already exists pls enter new Phone number')
                 
        mexit()
    if v in "shSH":
        search()
        mexit()
    else:
        print('    enter a valid entry')
        admin()
def doctorprocess():
    from tabulate import tabulate
    cur=mydb.cursor()
    id=input('enter your ID')
    z='select dname from doctor where ID like %s'
    t=(id,)
    cur.execute(z,t)
    result=cur.fetchall()
    if result==[]:
        print('no such record exist pls enter correct ID')
        doctorprocess()    
    else:
        print('_____________________________WELCOME',result,'_______________________________')
        x='y'
        while x in 'yY':
            c=input('To see your PROFILE  details press 1\n To see your APPOINTMENTS press 2')
            if c=='1':
                nq='select * from doctor where ID like %s'
                cur.execute(nq,t)
                nr=cur.fetchall()
                print(tabulate(nr, headers=['ID','Name','Specialist','Phone No.','Address','Country'], tablefmt='psql'))  
                x=input('do you want to see your appointments(y/n)')
            if c=='2':
                st='select specialist from doctor where ID like %s'
                cur.execute(st,t)
                f=cur.fetchall()
                q='select pname,phno from appointments where doctor like %s'
                for i in f:
                    tp=i
                cur.execute(q,tp)
                fr=cur.fetchall()
                print("Total number of patients: ", cur.rowcount)
                print(tabulate(fr, headers=['Phone No.','Patient Name'], tablefmt='psql'))
                x=input('do you want to see your profile(y/n)')
        mexit()
def main():
    i=int(input('''IF YOU ARE ADMIN(PRESS 1)
IF YOU ARE A DOCTOR(PRESS 2)
IF YOU ARE A PATIENT(PRESS 3)'''))
    if i==1:
        x='Y'
        while x in 'yY':
            paswd=input('ENTER THE PASSWORD')
            if paswd=='1234':
                admin()
                x='n'
            else:
                print('INCORRECT PASSWORD')    
    if i==2:
        doctor()
        doctorprocess()
    if i==3:
        patient()
    else:
        print("please select a valid option")
        main()
def mexit():
    e=input('To go to MAIN MENU press M or press E to exit')
    if e in 'Mm':
        main()
    else:
        feedback()
        quit()
def feedback():
    f=int(input('PLEASE RATE OUR PROGRAM IN 1 TO 5 '))
    if f==1:
        print('Ouch! , it hurts(ಥ﹏ಥ),we will try our best to improve it ')
    elif f==2:
        print('Expecting better next time~(´•︵•`)~')
    elif f==3:
        print('we will try to meet your expectations next time(⌣_⌣”)')
    elif f==4:
        print('we will try to make it 5 soon ~°(ᴖ◡ᴖ)°~')
    elif f==5:
        print('it was a great pleasure~(⌐■_■)ノ♪♬')
    else:
        print('please enter valid rating')
        
doctor()
staff()
apptab()
main()       







