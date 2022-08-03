print("-------- CO-VID 19 PANDEMIC -------")
print("WELL HERE YOU CAN FIND INFORMATION RELATED TO CO-VID AND SOME OTHER RELATABLE MATERIAL")
print("enter 1 to know about Co-VID 19")
print("enter 2 to know about the crisis of co-vid")
print("enter 3 to know about economy downfall worldwide")
print("enter 4 if you want to see the graph of economic downfall of various countries!")
print("enter 5 month wise iniiation steps of the goverment at the start up of co-vid!")
print("enter 6 to see the steps taken by the government of India  at the 20th day of lockdown of co-vid")
print("please enter only valid code otherwise an inappropriate message will pop up!")
code=int(input("enter the code to know about the required information="))

if code==1:
    f=open("cov.txt","r")
    message=f.read()
    print(message)
    f.close()
elif code==2:
    f=open("effects.txt","r")
    cov=f.read()
    print(cov)
    f.close()
elif code==3:
    print("You have the choice to see the GDP of all the countries or a specific country!")
    choice=input("enter the choice which do you want to see:( for every country or a specific one!)")
    if choice==("all" or "All"or"ALL") :
        import csv
        f=open("gdp.csv","r")
        data=csv.reader(f)
        print("GDP of countries affected by Co-Vid at a greater note:")
        for i in data:
            print(i)
        f.close()
    elif choice==("specific country"):
        country=input("enter the country name for which you want to see=")
        if country=="India":
            import csv
            f=open("india.csv","r")
            data=csv.reader(f)
            print("GDP of India=")
            for i in data:
                print(i)
            f.close()
        elif country=="United States":
            import csv
            f=open("us.csv","r")
            data=csv.reader(f)
            print("GDP of United States=")
            for i in data:
                print(i)
            f.close()
        elif country=="Brazil":
            import csv
            f=open("brail.csv","r")
            data=csv.reader(f)
            print("GDP of Brazil=")
            for i in data:
                print(i)
            f.close()
        elif country=="Russia":
            import csv
            f=open("russia.csv","r")
            data=csv.reader(f)
            print("GDP of Russia=")
            for i in data:
                print(i)
            f.close()
        elif country=="China":
            import csv
            f=open("china.csv","r")
            data=csv.reader(f)
            print("GDP of China=")
            for i in data:
                print(i)
            f.close()
        elif country=="Chile":
            import csv
            f=open("chile.csv","r")
            data=csv.reader(f)
            print("GDP of Chile=")
            for i in data:
                print(i)
            f.close()
        elif country=="Mexico":
            import csv
            f=open("mexico.csv","r")
            data=csv.reader(f)
            print("GDP of Mexico=")
            for i in data:
                print(i)
            f.close()
elif code==4:
    import matplotlib.pyplot as D
    x=["India","United States","Brazil","Russia","China","Chile","Mexico"]
    y=[4.70,5.20,4.70,1.30,1.50,1.50,0.7]
    col=["blue","red","yellow","green","pink","grey"]
    D.title("GDP(%) of some countries during CO-VID")
    D.xlabel("Countries")
    D.ylabel("Current GDP(%)")
    D.bar(x,y,color=col)
    D.show()
elif code==5:
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="sona",database="covid")
    mycursor=mydb.cursor()
    mycursor.execute("create table initiative(Sl_no integer(5),Month_of_Initiation char(25), Initiation char(1000)")
    mycursor.execute("insert into initiative values(1,March 25,The 21-day lockdown was put in place to contain the spread of novel coronavirus in the country.")
    mycursor.execute("insert into initiative values(2,April 14,The 3 week lockdown came to an end if no further cases came out")
    mycursor.execute("insert into initiative values(3,April 15,Lockdown 2 was taken into force!")
    mycursor.execute("insert into initiative values(4,May 3,Lockdown 2 was ended")
    mycursor.execute("insert into initiative values(5,May 4,Lockdown 3 started till 17th May")
    mycursor.execute("insert into initiative values(6,May 18,Lockdown 4 till May31")
    mycursor.execute("insert into initiative values(7,June 1,Finally Unlock 1 came into force till June 30!")
    mycursor.execute("insert into initiative values(8,July 1,Then another lockdown was set off till July 31")
    mydb.commit()
    for i in mycursor:
        print(i)
    mydb.close()    
elif code==6:
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="sona",database="covid")
    mycursor=mydb.cursor()
    mycursor.execute("create table steps(Sl_no integer(5),Steps_taken char(2000)")
    mycursor.execute("insert into steps values(1,The government recently introduced the Aarogya Setu mobile application to educate citizens about novel coronavirus and help them make informed decisions amid the crisis.")
    mycursor.execute("insert into steps values(2, On Sunday, an oil ministry spokesperson said that poor households using 5kg cooking gas cylinders will be entitled to eight free refills in three months as a relief from the disruptions due to the Covid-19 outbreak. The number of free refills will be limited to three for beneficiaries using 14.2kg cylinders.")
    mycursor.execute("insert into steps values(3,The government said it plans to set up a chain of 20 lakh retail shops called ‘Suraksha Stores’ across India which will provide daily essentials to citizens while maintaining stringent safety norms, news agency PTI reported.")
    mycursor.execute("insert into steps values(4,Union Human Resource Development Minister Ramesh Pokhriyal on Sunday launched a web portal to monitor and record the initiative by the ministry to combat Covid-19 with Knowledge, Technology and Innovation (YUKTI).")
    mycursor.execute("insert into steps values(5,Under its Ujjawala scheme, the government is providing free LPG refills for the next three months to over 8.3 crore poor women.")
    mycursor.execute("insert into steps values(6,Earlier this week, the finance ministry announced that it will make an immediate release of Rs 18,000 crore in tax refunds to individuals and businesses.")
    mycursor.execute("insert into steps values(7, The government decided to double the collateral-free loan amount for women in self-help groups to Rs 20 lakh.")
    mycursor.execute("insert into steps values(8,Under the PM-KISAN scheme, the finance ministry said that over 6 crore farmers have been benefited amid the lockdown. Rs 13,855 crore have gone towards payment of the first instalment of PM-KISAN.")
    mycursor.execute("insert into steps values(9,Wages under MGNREGA to be hiked to Rs 202 from Rs 182. The move would bring in Rs 2,000 in addition to workers.")
    mycursor.execute("insert into steps values(10, Last month, Finance Minister Nirmala Sitharaman announced a relief package worth Rs 1.70 lakh crore in the wake of the Covid-19 outbreak.")
    mycursor.execute("insert into steps values(11, Under a special provision, the government had announced that individuals could now withdraw three months salary from Employees’ Provident Fund (EPF) account amid the coronavirus crisis. The EPF withdrawals have been exempt from service charge.")
    mycursor.execute("insert into steps values(12,Under the National Social Assistance Programme, Rs 1,400 crore has been disbursed to about 2.82 crore old age people, widows and disabled people.")
    mycursor.execute("insert into steps values(13,The last date for filing income tax returns for the financial year 2018-19 has been extended to June 30, 2020. The interest rate on delayed income tax payment has been decreased to 9% from 12%.")
    mycursor.execute("insert into steps values(14,Over 2 crore construction workers received financial support worth Rs 3,066 crore under the Building and Construction Workers’ Fund.")
    mycursor.execute("insert into steps values(15,The deadline for filing GST returns for March, April, May has been extended to June 30, 2020. There will be no interest or penalty on late fee for delayed returns for companies with turnover up to Rs 5 crore.")
    mycursor.execute("insert into steps values(16,Nearly 20 crore women Jan Dhan account holders received Rs 500 each in their account. The total disbursement under the head was 9,930 crore, the finance ministry said.")
    mycursor.execute("insert into steps values(17,Deadline for linking Aadhaar with PAN card has also been extended from March 31 to June 30, 2020.")
    mycursor.execute("insert into steps values(18,The government has also released around Rs 30,000 crore in assistance to various sections of the society.")
    mycursor.execute("insert into steps values(19,The government said it will release 12 million MT of food grain during the April-June quarter under Pradhan Mantri Garib Kalyan Ann Yojana amid the Covid-19 crisis.")
    mycursor.execute("insert into steps values(20,The government is also providing medical insurance cover of Rs 50 lakh per person to health workers fighting the coronavirus pandemic.")
    mydb.commit()
    for i in mycursor:
        print(i)
    mydb.close()

   
else:
    print("the inputed code is not valid!n/ please try another code!")
    
    
