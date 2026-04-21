
# #QUIZ
# print("===Welcome To Quiz===")

# #User input
# name = input("What's your Name? ")
# print(f"Welcome!{name}")

# #Score
# score = 0
  

# print("======================")


# #Question1
# print("What's the result of 5+2? ")
# ans = int(input("Your Answer:"))
# if ans == 7:
#     print("Congradulations!")
#     score +=1
# else:
#     print("incorrect! The Answer is 7")



# print("======================")


# #question 2
# print("what's the result of 5*5? ")
# ans = int(input("Your Answer: "))
# if ans == 25:
#     print("Amazing,You're right..")
#     score +=1
# else:
#     print("incorrect! The Answer is 25")


# print("======================")


# #question 3
# print("If,else,elif is conditonal operators 'Yes/No'")
# ans = input("Your Answer: ")
# if ans == "yes" or ans =="YES" or ans =="Y" or ans== "y":
#     print("You're Right..")
#     score +=1
# else:
#     print("incorrect! The answer is 'yes'...")



# print("======================")


# # result
# print("You're finshide the Quiz")
# print(f"{name},Your Total Score is:{score}out of 3")

# Jaabir - Simple Quiz Program
# This program asks the user questions and gives a final score.

# Greeting
name=input("enter the your name:")
print("soo dhawoow",name)
# Score variable
score=0
#comments
#uestion1
print("questione=what is html")
answer=input("enter the answer:")
# Accept: html or hypertext markup language
if answer == "markuplanguag" :
   print("correct")
   score=+1
else:
    print("incorect")
 #question2
print("question2=sheeg madaweynaha somalia:")  
answer=input("enter the answer:")
if answer== "hassan sheikh":
 print("correct") 
 score += 1
else:
   print("incorect")
   #question3
print("queation3:what is cpu?") 
answer=input("enter the answer:" )
# Accept: central processing unit
if answer=="central proccessing unit":
    print("correct") 
    score += 1
else:
   print("incorect")   
 # Final message
print("Quiz Finished!")
print(f"{name},Your Total Score is:{score}out of 3")