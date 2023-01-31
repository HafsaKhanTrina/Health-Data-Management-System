import colorama
from colorama import Fore,Back,Style
a_string="Welcome to the homepage of smart Healthcard"
new_string= a_string.center(180,".")

print( '\033[1m' +Fore.RED + new_string+ '\033[0m')




from tabulate import tabulate

table_data=[['ID','Gender','Last update'],
            ['1901','Male','25.10.2022'],
            ['1902','male','2.11.2022'],
            ['1903','male','18.12.2022'],
            ['1904','Female','12.01.2023'],
            ['1907','Male','12.01.2023'],
            ['1908','Female','12.01.2023'],
            ['1105','Female','12.01.2023'],
            ['1102','male','26.01.2013']]
dis=input("Do you want see the patient list:")
if dis=="yes":
   print(tabulate(table_data,headers="firstrow",tablefmt="fancy_grid"))
else:
    print("\n")
while True:

    id=int(input("Enter your patient ID:"))
    if id =="quit":
      break
    elif id ==1901:
         print('\033[1m' +Fore.GREEN +"Name:Md. Ilias Uddin,Age:52"+ '\033[0m')
         report = int(input("Which file you want to open:\n1.medicine/Prescription\n2.pathology\n3.Parmanent disease:\n"))
         if report == 1:
             print("Medicine Details/Prescription")
             file1 = open("Md Ilias Uddin.txt", mode='r')
             data = file1.read()
             print(data)
             file1.close()
             edition = int(input("Do you want to edit the file.If you,than select 1:\n"))
             if edition == 1:
                 fd = open("Md Ilias Uddin.txt", 'a')
                 txt = input("Enter the text:")
                 txt = txt + '.\n'
                 fd.write(txt)
                 fd.close()
             else:
                 print("\n")
         elif report == 2:
             print("Pathology report")
             import os

             os.startfile('"D:\\practice of cespython project\\id1904\\pathology report1904"')
         elif report == 3:
             print("Parmanent Disease")
             file1 = open("1901 parament disease.txt", mode='r')
             data = file1.read()
             print(data)
             file1.close()
             edition = int(input("Do you want to edit the file.If you,than select 1:\n"))
             if edition == 1:
                 fd = open("1901 parament disease.txt", 'a')
                 txt = input("Enter the text:")
                 txt = txt + '\n'
                 fd.write(txt)
                 fd.close()
             else:
                 print("\n")
         else:
             print("Invalid")













    elif id==1902:
          print('\033[1m' +Fore.GREEN +"Name:Asraf,Age:12"+ '\033[0m')
          report = int(input("Which file you want to open:\n1.medicine/Prescription\n2.pathology\n3.Parmanent disease:\n"))
          if report == 1:
              print("Medicine Details/Prescription")
              file1 = open("Asraf.txt", mode='r')
              data = file1.read()
              print(data)
              file1.close()
              edition = int(input("Do you want to edit the file.If you,than select 1:\n"))
              if edition == 1:
                  fd = open("Asraf.txt", 'a')
                  txt = input("Enter the text:")
                  txt = txt + '\n'
                  fd.write(txt)
                  fd.close()
              else:
                  print("\n")
          elif report == 2:
              print("Pathology report")
              import os

              os.startfile('"D:\\practice of cespython project\\asraf pathology.pdf"')
          elif report == 3:
              print("Disease")
              file1 = open("asrafdiseases.txt", mode='r')
              data = file1.read()
              print(data)
              file1.close()
              edition = int(input("Do you want to edit the file.If you,than select 1:\n"))
              if edition == 1:
                  fd = open("asrafdiseases.txt", 'a')
                  txt = input("Enter the text:")
                  txt = txt + '\n'
                  fd.write(txt)
                  fd.close()
              else:
                  print("\n")
          else:
              print("Invalid")









    elif id==1903:
         print('\033[1m' +Fore.BLUE +"Name:Anas,Age:12"+ '\033[0m')
         report = int(
             input("Which file you want to open:\n1.medicine/Prescription\n2.pathology\n3.Disease:\n"))
         if report == 1:
             print("Medicine Details/Prescription")
             file1 = open("Anas.txt", mode='r')
             data = file1.read()
             print(data)
             file1.close()
             edition = int(input("Do you want to edit the file.If you,than select 1:\n"))
             if edition == 1:
                 fd = open("Asraf.txt", 'a')
                 txt = input("Enter the text:")
                 txt = txt + '\n'
                 fd.write(txt)
                 fd.close()
             else:
                 print("\n")
         elif report == 2:
             print("Pathology report")
             import os

             os.startfile("asraf pathology.pdf")
         elif report == 3:
             print(" Disease")
             file1 = open("anas1diseases.txt", mode='r')
             data = file1.read()
             print(data)
             file1.close()
             edition = int(input("Do you want to edit the file.If you,than select 1:\n"))
             if edition == 1:
                 fd = open("anas1diseases.txt", 'a')
                 txt = input("Enter the text:")
                 txt = txt + '\n'
                 fd.write(txt)
                 fd.close()
             else:
                 print("\n")
         else:
             print("Invalid")





    elif id==1904:
         print('\033[1m' +Fore.MAGENTA +"Name:Papia Akter,Age:24"+ '\033[0m')
         report = int(input("Which file you want to open:\n1.medicine/Prescription\n2.pathology\n3.Parmanent disease:\n"))
         if report == 1:
            print("Medicine Details/Prescription")
            file1 = open("Papia Akter.txt", mode='r')
            data = file1.read()
            print(data)
            file1.close()
            edition = int(input("Do you want to edit the file.If you,than select 1:\n"))
            if edition == 1:
                fd = open("Papia Akter.txt", 'a')
                txt = input("Enter the text:")
                txt = txt + '\n'
                fd.write(txt)
                fd.close()
            else:
                print("\n")
         elif report == 2:
              print("Pathology report")
              import os

              os.startfile('"D:\\practice of cespython project\\id1904\\pathology report1904"')
         elif report == 3:
              print("Parmanent Disease")
              file1 = open("permanent diseases 1904.txt", mode='r')
              data = file1.read()
              print(data)
              file1.close()
              edition = int(input("Do you want to edit the file.If you,than select 1:\n"))
              if edition == 1:
                  fd = open("permanent diseases 1904.txt", 'a')
                  txt = input("Enter the text:")
                  txt = txt + '\n'
                  fd.write(txt)
                  fd.close()
              else:
                  print("\n")
         else:
             print("Invalid")






    elif id==1907:
         print('\033[1m' +Fore.MAGENTA +"Name:sadia,Age:22"+ '\033[0m')
         report = int(input("Which file you want to open:\n1.medicine/Prescription\n2.pathology\n3.Parmanent disease:\n"))
         if report == 1:
             print("Medicine Details/Prescription")
             file1 = open("1906 prescription.txt", mode='r')
             data = file1.read()
             print(data)
             file1.close()
             edition = int(input("Do you want to edit the file.If you,than select 1:\n"))
             if edition == 1:
                 fd = open("1907 prescription.txt", 'a')
                 txt = input("Enter the text:")
                 txt = txt + '\n'
                 fd.write(txt)
                 fd.close()
             else:
                 print("\n")
         elif report == 2:
              print("Pathology report")
              import os

              os.startfile('"D:\practice of cespython project\id1907"')
         elif report == 3:
              print("Parmanent Disease")
              file1 = open("1907 parmanent diseases.txt", mode='r')
              data = file1.read()
              print(data)
              file1.close()
              edition = int(input("Do you want to edit the file.If you,than select 1:\n"))
              if edition == 1:
                  fd = open("1907 parmanent diseases.txt", 'a')
                  txt = input("Enter the text:")
                  txt = txt + '\n'
                  fd.write(txt)
                  fd.close()
              else:
                  print("\n")

         else:
              print("Invalid")








    elif id==1105:
          print('\033[1m' +Fore.MAGENTA +"Name:Najiba,Age:17"+ '\033[0m')
          report = int(input("Which file you want to open:\n1.medicine/Prescription\n2.pathology\n3.Parmanent disease:\n"))
          if report == 1:
              print("Medicine Details/Prescription")
              file1 = open("1105 prescription.txt", mode='r')
              data = file1.read()
              print(data)
              file1.close()
              edition = int(input("Do you want to edit the file.If you,than select 1:\n"))
              if edition == 1:
                  fd = open("1105 prescription.txt", 'a')
                  txt = input("Enter the text:")
                  txt = txt + '\n'
                  fd.write(txt)
                  fd.close()
              else:
                  print("\n")
          elif report == 2:
               print("Pathology report")
               import os

               os.startfile('"C:\\Users\\88017\\Downloads\\MS Najiba 1105 pathology report.pdf"')
          elif report == 3:
               print("Parmanent Disease")
               file1 = open("1105 pamanent diseases.txt", mode='r')
               data = file1.read()
               print(data)
               file1.close()
               edition = int(input("Do you want to edit the file.If you,than select 1:\n"))
               if edition == 1:
                   fd = open("1105 pamanent diseases.txt", 'a')
                   txt = input("Enter the text:")
                   txt = txt + '\n'
                   fd.write(txt)
                   fd.close()
               else:
                   print("\n")
          else:
               print("Invalid")




    elif id == 1908:
         print('\033[1m' +Fore.MAGENTA +"Name:Neha,Age:22"+ '\033[0m')
         report = int(input("Which file you want to open:\n 1.medicine/Prescription\n2.pathology\n3.Parmanent disease:"))
         if report == 1:
             print("Medicine Details/Prescription")
             file1 = open("1908 prescription.txt", mode='r')
             data = file1.read()
             print(data)
             file1.close()
             edition = int(input("Do you want to edit the file.If you,than select 1:\n"))
             if edition == 1:
                 fd = open("1908 prescription.txt", 'a')
                 txt = input("Enter the text:")
                 txt = txt + '\n'
                 fd.write(txt)
                 fd.close()
             else:
                 print("\n")
         elif report == 2:
              print("Pathology report")
              import os

              os.startfile('"D:\\practice of cespython project\\1908 pathology report.pdf"')
         elif report == 3:
              print("Parmanent Disease")
              #reading file
              file1 = open("1908 parmanet dissease.txt", mode='r')
              data = file1.read()
              print(data)
              file1.close()
              edition = int(input("Do you want to edit the file.If you,than select 1:\n"))
              if edition == 1:
                  #edit file
                  fd = open("1908 parmanet dissease.txt", 'a')
                  txt = input("Enter the text:")
                  txt = txt + '\n'
                  fd.write(txt)
                  fd.close()
              else:
                  print("\n")

         else:
             print("Invalid")
    else:
        print("Invalid")