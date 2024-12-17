#Nested Conditions

#Python Filtration

name = input("Enter your name:  ")

isStudent = input("are you a student of DLL (yes/no)?  ")

if isStudent.lower() == "yes":
 yearLevel = input("What Year Level Are You?\nF = Freshmen\nSP = Sophomore\nJ = Junior\nS = Senior\nPlease Input your Year Level Here:  ")
 
 if yearLevel.lower() == "f":
  print(f"Welcome to DLL Freshmen {name}")
 elif yearLevel.lower() == "sp":
  print(f"Welcome to DLL Sophomore {name}")
 elif yearLevel.lower() == "j":
  print(f"Welcome to DLL Junior {name}")
 elif yearLevel.lower() == "s":
  print(f"Welcome to DLL Senior {name}")

else:
 print("Welcome to The System ")
