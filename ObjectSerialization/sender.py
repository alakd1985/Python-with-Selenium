from ObjectSerialization.emp import employee
import  pickle

f = open('emp.ser','wb')
while True:
    eno = int(input('Enter Employee Number:'))
    ename = input('Enter Employee Name:')
    esal = float(input('Enter Employee Salary:'))
    eaddr = input('Enter Employee Address:')
    e = employee(eno,ename,esal,eaddr)
    pickle(e,f)
    option = input('Do you want to serialize another employee object: [Yes/No]')
    if option.lower() == 'no':
        break
print('Multiple object serializer')
