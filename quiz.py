print(' QUIZ TIME! :    '    )        
print('            ;  ')              
print('           :   ')              
print('           ;     ')            
print('          /          ')         
print('        o/              ')      
print('      ._/\___,             ')    
print('          \                  ') 
print('          /                   ') 
print('          `      ')

print("🎉 Welcome to the Mini Quiz Game! 🎉")
print('***You only have 3 Attempts per Question. So take your time and think carefully***')
print('***Read the question carefully. if you are wrong, that will take 1 attempt.***')
print("----------------------------------\n")

num_correct=0
questions = 7
attempts =3

#Q1
for i in range(1 , attempts +1):
    print ('1) What is 5 + 7?    (write in number!!)')                      
    answer = input('Answer:') 
    
    if not answer.isdigit():
        print(f"⚠️ Answer must be a number! Attempt {i} of {attempts}.\n")
        continue
        
    
    if answer.isdigit() and int(answer) == 12:
     print("✅ Correct!")
     print('------------------------------------\n') 
     num_correct += 1
     break
    else:
        print(f'❌ Wrong! Attempt {i} of {attempts}.\n')
    if i == attempts:
     print("❌ Wrong! The correct answer is 12.")
     print('------------------------------------\n')    
     
#Q2  
for i in range(1, attempts+1):
    print("2) What is the capital of France?") 
    answer=input("Answer:").strip().lower()
    
    if answer.isdigit():
        print(f"⚠️ Answer must be a word!Attempt {i} of {attempts}.\n")
        continue
        
    
    if answer == 'paris':
        print("✅ Correct!")
        print('------------------------------------\n') 
        num_correct += 1
        break
    else:
        print(f'❌ Wrong! Attempt {i} of {attempts}.\n')
    if i == attempts:
     print("❌ Wrong! The correct answer is Paris.")
     print('------------------------------------\n') 
     
#Q3

for i in range(1, attempts+1):
   print("3) Which of these are programming languages?     (write only A, B or C)\n")
   print("A) Python")
   print("B) CSSI")
   print("C) HTMI")     
   
   answer =(input('Choose one:')).strip().lower()
   if not answer.isalpha():
        print(f"⚠️ Answer needs to be a character (A, B, or C)! Attempt {i} of {attempts}.\n")
        continue 
   
   if  answer == 'a' or answer == 'python':
       print("✅ Correct!")
       print('------------------------------------\n') 
       num_correct += 1
       break
   else:
       print(f"❌ Wrong! Attempt {i} of {attempts}.\n")
       if i == attempts:
           print('❌ Wrong! The correct answer is A.')  
           print('------------------------------------\n') 
           
#Q4

for i in range(1, attempts+1):
    print('4) What is 12 x 5 = ?          (write in number!!)')
    answer = input('Answer: ')
    
    if not answer.isdigit():
        print(f"⚠️ Answer must be a number!Attempt {i} of {attempts}.\n")
        continue
        
    if answer.isdigit() and int(answer) == 60:
        print("✅ Correct!")
        print('------------------------------------\n') 
        num_correct += 1
        break
    else:
        print(f"❌ Wrong! Attempt {i} of {attempts}.\n")
        if i == attempts:
            print("❌ Wrong! The correct answer is 54.")
            print('------------------------------------\n') 
            
#Q5

for i in range(1, attempts + 1):
    print("5) Who wrote 'Romeo and Juliet'?\n")
    print("A) Charles Dickens")
    print("B) William shakespeare")
    print("C) Jane Austen") 
    answer = (input('Answer:')).strip().lower()
    
    if answer.isdigit():
        print(f"⚠️ Answer needs to be a character (A, B, or C)! Attempt {i} of {attempts}.\n")
        continue
    
    if answer == 'b':
        print("✅ Correct!")
        print('------------------------------------\n') 
        num_correct += 1
        break
    else:
        print(f"❌ Wrong! Attempt {i} of {attempts}.\n")
        if i == attempts:
            print("The correct answer is B.")
            print('------------------------------------\n') 
            
#Q6

for i in range(1, attempts +1):
    print("6) What is the 3rd character in the word 'Python'?")
    answer=(input('Answer:')).strip().lower()
    
    if not answer.isalpha():
        print(f"⚠️ Answer must be a word! Attempt {i} of {attempts}.\n")
        continue
    
    if answer == 't':
       print("✅ Correct!")
       print('------------------------------------\n') 
       num_correct += 1
       break
    else:
        print(f"❌ Wrong! Attempt {i} of {attempts}.\n")
        if i == attempts:
             print("❌ Wrong! The correct answer is 't'.")
             print('------------------------------------\n') 

#Q7

for i in range(1, attempts + 1):
    print("7) Which string method is used to convert text to uppercase?")
    print("A) .upper()")
    print("B) .lower()")
    print("C) .capitalize()")
    answer = input("Answer: ").strip().lower()
    
    if answer.isdigit():
        print(f"⚠️ Answer needs to be a character (A, B, or C)! Attempt {i} of {attempts}.\n")
        continue
    
    if answer == 'a':
        print("✅ Correct!\n")
        num_correct += 1
        break
    else:
        print(f"❌ Wrong! Attempt {i} of {attempts}.\n")
        if i == attempts:
            print("❌ Wrong! The correct answer is A.\n")             
       
        
    
    
    
                
            
print("----------------------------------------------------")
print(f'🎯 You got {num_correct} out of {questions} correct!') 
percent =int((num_correct / questions) * 100)
print(f"📊 Your score: {percent}%")
print("Thanks for playing! 😃")

# test comment