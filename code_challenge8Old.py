prelim = eval(input('Enter Your Prelim Grade')) 
midterm = eval(input('Enter Your Midterm Grade')) 
semi_final = eval(input('Enter Your Semi-Finals Grade')) 
final = eval(input('Enter Your Finals Grade'))  
quiz = eval(input('Enter Your Quiz Grade')) 
project = eval(input('Enter Your Project Grade')) 

grade1 = (prelim * 15) + midterm
grade2 = (midterm * 15) + semi_final
grade3 = (semi_final * 15) + final
grade4 = (final * 15) + quiz
grade5 = (quiz * 25) + project
grade6 = (project * 15)
print(grade6)
