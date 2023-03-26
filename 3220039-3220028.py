'''Python Calendar'''

import calendar
import csv
from csv import writer
import os.path
import datetime
import pandas as pd
import time
from time import sleep

#ΒΑΣΙΚΟ ΠΡΙΝΤ
def table(year,month):
    header(year,month)
    # Το h ειναι το συνολο ολων των στοιχειων τις παρακατω λιστας περιλαμβανοντας και τα 0
    h=0
    f=False
    # Λιστα με ολες τις μερες του μηνα
    lista=calendar.monthcalendar(year, month)
    for i in range(len(lista)):
        # Το l ειναι ο αριθμος των ημερων για καθε εβδομαδα 
        l=0
        for j in lista[i]:
            if month==1:
                # Για την εμφανιση των υπολοιπωμενων ημερων του τρεχοντα μηνα
                # Το f ειναι μια λογικη τιμη ετσι ωστε να μπει μονο μια φορα στη πρωτη if 
                if j==0  and f==False:
                    f=True
                    lista2=calendar.monthcalendar(year-1,12)
                    # Koβει τη λιστα ετσι ωστε να παρει μονο τη τελευται εβδομαδα του μηνα
                    lista2=lista2[-1]
                    # Κοβει τη λιστα ετσι ωστε να παρει της μερες του προηγουμενου μηνα χωρις τα 0
                    lista2=lista2[:first(year,month)] 
                    for i in lista2:
                        l+=1
                        print ("    " ,str(i) , end=" | ") 
                # Ελεγχει αν εχουν εμφανιστει ηδη οι 7 μερες της εβδομαδας ετσι ωστε να εμφανισει τις μερες στη κατω γραμμη
                elif l==6 and j!=0:
                    # Ελεχγει αν ειναι μονοψηφιος
                    if j<=9:
                        date=f'{year}-0{month}-0{j}'
                        # Υπαρχει event?
                        if date in lst_star:
                            print("[* ",j,"]")
                        else:
                            print("[  ",j,"]")
                    # Ελεχγει αν ειναι διψηφιος
                    else:
                        date=f'{year}-0{month}-{j}'
                        # Υπαρχει event?
                        if date in lst_star:
                            print("[*",j,"]")
                        else:
                            print("[ ",j,"]")
                    h+=1
                # Ελεγχει αν δεν ειναι το τελος της εβδομαδας ετσι ωστε να εμφανισει σε σειρα τις μερες
                elif j!=0:
                    if j<=9 :
                        date=f'{year}-0{month}-0{j}'
                        if date in lst_star:
                            print('[* ',j,']', end=' | ')
                        else:
                            print("[  ",j,"]", end=" | ")
                    else:
                        date=f'{year}-0{month}-{j}'
                        if date in lst_star:
                            print('[*',j,']', end=' | ')
                        else:
                            print("[ ",j,"]", end=" | ")
                    l+=1
                    h+=1
                # Ελεχγει αν ειναι εχει εμφανισει ολες τις μερες του τρεχοντα μηνα ετσι ωστε να εμφανισει τις μερες του επομενου μηνα
                elif h==calendar.monthrange(year,month)[1]:
                    h+=1
                    t=1
                    lista3=calendar.monthcalendar(year,month+1)
                    lista3=lista3[0]
                    lista3=lista3[first(year,month+1):]
                    for i in lista3:
                        if t==len(lista3):
                            print ("     " ,str(i) )
                        else:
                            print ("     " ,str(i) , end=" | ") 
                            t+=1
# TA ΠΑΡΑΠΑΝΩ ΣΧΟΛΙΑ ΑΝΤΙΣΤΟΙΧΟΥΝ ΚΑΙ ΓΙΑ ΤΑ ΠΑΡΑΚΑΤΩ IF
            elif month==12:
                if j==0 and f==False:
                    f=True
                    lista2=calendar.monthcalendar(year,month-1)
                    lista2=lista2[-1]
                    lista2=lista2[:first(year,month)] 
                    for i in lista2:
                        l+=1
                        print ("    " ,str(i) , end=" | ") 
                elif l==6 and j!=0:
                    if j<=9:
                        date=f'{year}-{month}-0{j}'
                        if date in lst_star:
                            print("[*  ",j,"]")
                        else:
                            print("[  ",j,"]")
                    else:
                        date=f'{year}-{month}-{j}'
                        if date in lst_star:
                            print("[*  ",j,"]")
                        else:
                            print("[ ",j,"]")
                    h+=1
                elif j!=0:
                    if j<=9 :
                        date=f'{year}-{month}-0{j}'
                        if date in lst_star:
                            print('[* ',j,']', end=' | ')
                        else:
                            print("[  ",j,"]", end=" | ")
                    else:
                        date=f'{year}-{month}-{j}'
                        if date in lst_star:
                            print('[*',j,']', end=' | ')
                        else:
                            print("[ ",j,"]", end=" | ")
                    l+=1
                    h+=1
                elif h==calendar.monthrange(year,month)[1]:
                    t=1
                    lista3=calendar.monthcalendar(year+1,1)
                    lista3=lista3[0]
                    lista3=lista3[first(year+1,1):]
                    for i in lista3:
                        if t==len(lista3):
                            print ("     " ,str(i) )
                        else:
                            print ("     " ,str(i) , end=" | ") 
                            t+=1
                    break
            else:
                if j==0  and f==False:
                    f=True
                    lista2=calendar.monthcalendar(year,month-1)
                    lista2=lista2[-1]
                    lista2=lista2[:first(year,month)] 
                    for i in lista2:
                        l+=1
                        print ("    " ,str(i) , end=" | ")
                elif l==6 and j!=0:
                    if j<=9:
                        if len(str(month))==1:
                            date=f'{year}-0{month}-0{j}'
                        else:
                            date=f'{year}-{month}-0{j}'
                        if date in lst_star:
                            print("[*  ",j,"]")
                        else:
                            print("[  ",j,"]")
                    else:
                        if len(str(month))==1:
                            date=f'{year}-0{month}-{j}'
                        else:
                            date=f'{year}-{month}-{j}'
                        if date in lst_star:
                            print("[*  ",j,"]")
                        else:
                            print("[ ",j,"]")
                    h+=1
                elif j!=0:
                    if j<=9 :
                        if len(str(month))==1:
                            date=f'{year}-0{month}-0{j}'
                        else:
                            date=f'{year}-{month}-0{j}'
                        if date in lst_star:
                            print('[* ',j,']', end=' | ')
                        else:
                            print("[  ",j,"]", end=" | ")
                    else:
                        if len(str(month))==1:
                            date=f'{year}-0{month}-{j}'
                        else:
                            date=f'{year}-{month}-{j}'
                        if date in lst_star:
                            print('[*',j,']', end=' | ')
                        else:
                            print("[ ",j,"]", end=" | ")
                    l+=1
                    h+=1
                elif h==calendar.monthrange(year,month)[1]:
                    h+=1
                    t=1
                    lista3=calendar.monthcalendar(year,month+1)
                    lista3=lista3[0]
                    lista3=lista3[first(year,month+1):]
                    for i in lista3:
                        if t==len(lista3):
                            print ("     " ,str(i) )
                        else:
                            print ("     " ,str(i) , end=" | ") 
                            t+=1    
    print('  ')
    print('_______________________________________________________________')
    print( )
    menu()
    i=input('    ->  ')
    options(i,month,year)


#ΠΡΩΤΕΣ ΜΕΡΕΣ
# Βρισκει σε ποια μερα ξεκιναει ο μηνα
def first(year,month):
    '''
    >>> first(2023,12)
    4
    >>> first(2023,2)
    2
    '''
    f=calendar.monthrange(year,month)
    return f[0]

#ΕΠΙΚΕΦΑΛΙΔΑ
def header(year,month):
    month_letters= greek_months(month)
    print('_______________________________________________________________')
    print( )
    print(month_letters , year )
    print( )
    print('_______________________________________________________________')
    print( )
    print('  ΔΕΥ   |   ΤΡΙ   |   ΤΕΤ   |   ΠΕΜ   |   ΠΑΡ   |   ΣΑΒ   |   ΚΥΡ')
    print( )

#EPILOGES 
def options(i,month,year):
    if i=='':
        if month==12:
            month=1
            year=year+ 1
        else:
          month=month+1
        print( )
        print( )
        print( )
        return table(year,month)
    elif i== '-':
        if month==1:
            month=12
            year=year- 1
        else:
          month=month-1
        print( )
        print( )
        print( )
        return table(year,month)
    elif i=='q':
        return
    elif i=='+':
        print( )
        menu2()
        choice2=int(input('    ->  '))
        if choice2==0:
            return table(year,month)
        elif choice2==1:
            option1()
        elif choice2==2:
            option2()
        else:
            option3()
    elif i=='*':
        emfanisi()
        keno=input('Πατήστε οποιοδήποτε χαρακτήρα για επιστροφή στο κυρίως μενού:')
        return table(year,month)
    else:
        print('Δώσε μία από τις επιλογές')
        return table(year,month)


#Turning the number into the greek name of the month it represents

def greek_months(month):
    MONTHS=['ΙΑΝ','ΦΕΒ','ΜΑΡΤ','ΑΠΡ','ΜΑΙ','ΙΟΥΝ','ΙΟΥΛ','ΑΥΓ','ΣΕΠΤ','ΟΚΤ','ΝΟΕ','ΔΕΚ']
    return MONTHS[month-1]

#The main menu

def menu():
    """
    >>> menu()
    Πατήστε ENTER για προβολή του επόμενου μήνα, "q" για έξοδο ή κάποια από τις παρακάτω επιλογές:
         "-" για πλοήγηση στον προηγούμενο μήνα
         "+" για διαχείριση των γεγονότων του ημερολογίου
         "*" για εμφάνιση των γεγονότων ενός επιλεγμένου μήνα     
    """
    print('Πατήστε ENTER για προβολή του επόμενου μήνα, "q" για έξοδο ή κάποια από τις παρακάτω επιλογές:')
    print('     "-" για πλοήγηση στον προηγούμενο μήνα')
    print('     "+" για διαχείριση των γεγονότων του ημερολογίου')
    print('     "*" για εμφάνιση των γεγονότων ενός επιλεγμένου μήνα')

#The menu if "+" is chosen

def menu2():
    '''
    >>> menu2()
    Διαχείριση γεγονότων ημερολογίου, επιλέξτε ενέργεια:
         1 Καταγραφή νέου γεγονότος
         2 Διαγραφή γεγονότος
         3 Ενημέρωση γεγονότος
         0 Επιστροφή στο κυρίως μενού
    '''
    print('Διαχείριση γεγονότων ημερολογίου, επιλέξτε ενέργεια:')
    print('     1 Καταγραφή νέου γεγονότος')
    print('     2 Διαγραφή γεγονότος')
    print('     3 Ενημέρωση γεγονότος')
    print('     0 Επιστροφή στο κυρίως μενού')

#Επιλογη 1 Καταγραφη Νεου Γεγονοτος
def option1():
    print(' ')
    print('=== Καταγραφή νέου γεγονότος ====')
    print(' ')
    date=str(input('Δώσε την ημερομηνία του γεγονότος: '))
    year=int(str(date[0])+str(date[1])+str(date[2])+str(date[3]))
    month=int(str(date[5])+str(date[6]))
    day=int(str(date[8])+str(date[9]))
    # Eλεγχος Εγκυροτητας
    while year<2020 or month>12 or month<1 or day<1 or day>calendar.monthrange(year,month)[1]:
        date=str(input('Δώσε σωστά την ημερομηνία του γεγονότος: '))
        year=int(str(date[0])+str(date[1])+str(date[2])+str(date[3]))
        month=int(str(date[5])+str(date[6]))
        day=int(str(date[8])+str(date[9]))
    time=str(input('Δώσε την ώρα του γεγονότος: '))
    hour,minute=time.split(':')
    hour=int(hour)
    minute=int(minute)
    # Eλεγχος Εγκυροτητας
    while hour<0 or hour>23 or minute>59 or minute<0:
        time=str(input('Δώσε σωστά την ώρα του γεγονότος: '))
        hour=int(str(time[0])+str(time[1]))
        minute=int(str(time[3])+str(time[4]))
    duration=int(str(input('Δώσε την διάρκεια του γεγονότος: ')))
    # Eλεγχος Εγκυροτητας
    while duration<0 or duration!=int(duration):
        duration=int(str(input('Δώσε σωστά την διάρκεια του γεγονότος: ')))
    title=str(input('Δώσε την ονομασία του γεγονότος: '))
    # Eλεγχος Εγκυροτητας
    while ',' in title:
        title=str(input('Δώσε σωστά την ονομασία του γεγονότος: '))
    lst=[]
    lst.append(date)
    lst.append(time)
    lst.append(duration)
    lst.append(title)
    addcsv(lst)
    lst_star.append(date)
    today = datetime.date.today()
    year2 = today.year
    month2=today.month
    return table(year2,month2)

    

#ΔΙΑΓΡΑΦΗ ΓΕΓΟΝΩΤΩΝ
def option2():
    print(' ')
    print('=== Διαγραφή γεγονότος ====')
    print(' ')
    prosorino=[]
    date=str(input('Δώσε την ημερομηνία του γεγονότος: '))
    year=int(str(date[0])+str(date[1])+str(date[2])+str(date[3]))
    month=int(str(date[5])+str(date[6]))
    while year<2020 or month>12 or month<1 :
        date=str(input('Δώσε σωστά την ημερομηνία του γεγονότος: '))
        year=int(str(date[0])+str(date[1])+str(date[2])+str(date[3]))
        month=int(str(date[5])+str(date[6]))
    lst=anazitisi()
    print(' ')
    j=0
    j2=0
    for i in lst:
        l=i[0]
        l2=int(str(l[5])+str(l[6]))
        l3=int(str(l[0])+str(l[1])+str(l[2])+str(l[3]))
        if l2==month and l3==year:
            print(str(j)+'.'+' '+'['+lst[j2][3]+']'+' '+'->' +' ' +'Date:'+' ' +lst[j2][0]+','+' '+'Time:'+' '+lst[j2][1]+','+' '+'Duration:'+ lst[j2][2])
            prosorino.append(lst[j2][3])
            j=j+1
        j2=j2+1
    rv=input('Δώσε τον αριθμό του γεγονότος που θες να διαγράψεις: ')
    rv=int(rv)
    k=0
    p=0
    for i in lst: 
        for j in i:
            if j==prosorino[rv]:
                k=p
        p=p+1
    lst_star.remove(lst[k][0])
    lst.remove(lst[k])
    delete()
    arx=['date','time','duration','name']
    addcsv(arx)
    for i2 in lst:
        addcsv(i2)
    today = datetime.date.today()
    year2 = today.year
    month2=today.month
    return table(year2,month2)

               
#ΑΝΑΖΗΤΗΣΗ ΓΕΓΟΝΟΤΩΝ
def option3():
    prosorino=[]
    print(' ')
    print('=== Aναζήτηση γεγονότος ====')
    print(' ')
    etos=int(input('Εισάγετε έτος: '))
    print(' ')
    minas=int(input('Εισάγετε μήνα: '))
    lst=anazitisi()
    print(' ')
    j=0
    j2=0
    # Εμφανιση γεγονοτων
    for i in lst:
        l=i[0]
        l2=int(str(l[5])+str(l[6]))
        l3=int(str(l[0])+str(l[1])+str(l[2])+str(l[3]))
        if l2==minas and l3==etos:
            print(str(j)+'.'+' '+'['+lst[j2][3]+']'+' '+'->' +' ' +'Date:'+' ' +lst[j2][0]+','+' '+'Time:'+' '+lst[j2][1]+','+' '+'Duration:'+ lst[j2][2])
            prosorino.append(lst[j2][3])
            j=j+1
        j2=j2+1
    epilogi=input('Επέλεξε ένα γεγονός προς ενημερώση: ')
    if not(epilogi in range(j)):
        today = datetime.date.today()
        year2 = today.year
        month2=today.month
        return table(year2,month2)
    else:
        epilogi=int(epilogi)
        print(' ')
        k=0
        p=0
        for i in lst: 
            for j in i:
                if j==prosorino[epilogi]:
                    k=p
            p=p+1
        date=input('Ημερομηνία γεγονότος'+' ' +'('+lst[k][0]+'):')
        print(' ')
        time=input('Ωρα γεγονότος'+' ' +'('+lst[k][1]+'):')
        print(' ')
        duration=input('Διάρκεια γεγονότος'+' ' +'('+lst[k][2]+'):')
        print(' ')
        name=input('Ονομα γεγονότος'+' ' +'('+lst[k][3]+'):')
        if date!='':
            lst[k][0]=date
        if time!='':
            lst[k][1]=time
        if duration!='':
            lst[k][2]=duration
        if name!='':
            lst[k][3]=name
        delete()
        arx=['name','date','time','duration']
        addcsv(arx)
        for i2 in lst:
            addcsv(i2)
    today = datetime.date.today()
    year2 = today.year
    month2=today.month
    return table(year2,month2)


#Εμφανιση των γεγονοτων
def emfanisi():
    dates=[]
    print(' ')
    print('=== Εμφάνιση γεγονότων ====')
    print(' ')
    etos=int(input('Εισάγετε έτος: '))
    print(' ')
    minas=int(input('Εισάγετε μήνα: '))
    lst=anazitisi()
    print(' ')
    j=0
    j2=0
    for i in lst:
        l=i[0]
        l2=int(str(l[5])+str(l[6]))
        l3=int(str(l[0])+str(l[1])+str(l[2])+str(l[3]))
        if l2==minas and l3==etos :
            print(str(j)+'.'+' '+'['+lst[j2][0]+']'+' '+'->' +' ' +'Date:'+' ' +lst[j2][1]+','+' '+'Time:'+' '+lst[j2][2]+','+' '+'Duration:'+ lst[j2][3])
            j=j+1
        j2=j2+1


#Προσθέτω στο csv
def addcsv(x):
    x2=[]
    x2.append(x)
    file=open('events.csv','a',newline='')
    writer=csv.writer(file)
    writer.writerows(x2)
    file.close()


# Iterator του csv φακελου
def anazitisi():
    f=open('events.csv','r',newline='')
    next(f)
    data = list(csv.reader(f, delimiter=","))
    f.close    
    return data  

# Μηδενιζει το φακελο csv
def delete():
    f=open('events.csv','w')
    f.truncate()
    f.close()

     
#RUNNING THE PROGRAM
if __name__ == "__main__":
    # Φτιαχνει φακελο csv στη περιπτωση που δεν υπαρχει
    if os.path.exists('events.csv'):
        f = open('events.csv','r',encoding='utf-8')
        f.close()
    else:
        f = open('events.csv','w',encoding='utf-8',newline='')
        csv_writer = writer(f)
        csv_writer.writerow('Date,Hour,Duration,Title'.split(','))
        f.close() 
    lst_star=[]
    maou_lst=anazitisi()
    if len(maou_lst)>1:
        for i in maou_lst:
            lst_star.append(i)
    today = datetime.date.today()
    year = today.year
    month=today.month
    table(year,month)
