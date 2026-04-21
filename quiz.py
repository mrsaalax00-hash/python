
#QUIZ
print("===Welcome To Quiz===")

#User input
name = input("What's your Name? ")
print(f"Welcome!{name}")

#Score
score = 0
  

print("======================")


#Question1
print("What's the result of 5+2? ")
ans = int(input("Your Answer:"))
if ans == 7:
    print("Congradulations!")
    score +=1
else:
    print("incorrect! The Answer is 7")



print("======================")


#question 2
print("what's the result of 5*5? ")
ans = int(input("Your Answer: "))
if ans == 25:
    print("Amazing,You're right..")
    score +=1
else:
    print("incorrect! The Answer is 25")


print("======================")


#question 3
print("If,else,elif is conditonal operators 'Yes/No'")
ans = input("Your Answer: ")
if ans == "yes" or ans =="YES" or ans =="Y" or ans== "y":
    print("You're Right..")
    score +=1
else:
    print("incorrect! The answer is 'yes'...")



print("======================")


# result
print("You're Finished the Quiz")
print(f"{name},Your Total Score is: {score}out of 3")

