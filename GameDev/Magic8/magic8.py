# In this project I created a python program that simulates 
# a popular fortune-telling device. This project showcases basic 
# python skills such as if and else if statements. 
# As well as the use of the python function .randint(). 


# assigning variables 

name = "Meelah"
question = " Will I ever find true love?"
answer = ""

# random generated values 
import random 

random_number = random.randint(1, 11)

print (random_number)


# Control flow 

if random_number == 1:
  answer =  "Yes, definitely"
elif random_number == 2:
  answer = "it is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you" 
elif random_number == 7:
  answer = "My suorces say no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
elif random_number == 10:
  answer = "If you wish it, it shall be so"
elif random_number == 11:
  answer = " Go ask your momma"
else:
  answer = "Error"

  #control flow for name
if (name == "") or (question == ""):
  print("You have to enter a question silly! ")
elif name == "":
  print("Asker: " + str(question))
  print("Magic 8-Ball's answer: " + str(answer))
else:
  print( str(name) + " asks: Will I ever find true love? " )
  print("Magic 8-Ball's answer: " + str(answer))
