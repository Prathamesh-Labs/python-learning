print("Welcome to our Quiz App")
print("powered by prathamesh_labs")
score = 0

print("\nWhat is the capital of India")
print("1. Mumbai")
print("2. Delhi")
print("3. Kolkata")
print("4. Chennai")
answer =input ("Enter your answer (1-4):")
if answer == "2":
    score +=1
    print("Correct" )
else:
            print("Better luck next time")
        
print("\nWhich language is primarily used in AI and Machine Learning")
print("1. Java")
print("2. Python")
print("3. C")
print("4. PHP")
answer = input("Enter your answer(1-4):")
if answer == "2":
    score +=1
    print("Excellent, It is the correct answer")
else:
    print("Sorry! It is a wrong answer")
    
print("\nWho is the founder of Microsoft?")
print("1. Steve Jobs")
print("2.Elon Musk") 
print("3. Bill Gates")
print("4.Nikola Tesla ")
answer = input("Enter your number(1-4):")
if answer =="3":
      score +=1
      print("Yes! That's the right answer")
else:
      print("Wrong!") 
print("\nWho is the founder of Microsoft?")
print("1.Arificial Important ")
print("2. Artificial Intelligence")
print("3. Advanced Information ")
print("4. Automated Interface")
answer = input("Enter your number(1-4):")
if answer =="2":
      score +=1
      print("Perfect answer")
else:
      print("This is a wrong answer")
print("Which planet is known as the Red Planet?")
print("1. Venus")
print("2. Jupiter")
print("3. Mars")
print("4. Saturn")
answer = input("Enter your number(1-4):")
if answer =="3":
      score +=1
      print("Yes!you have guessed the right answer")
else:
      print("You guesses the wrong answer")
if score == 5:
    print("Outstanding! Perfect Score!")
elif score >= 3:
    print("Good Job!")
else:
    print("Keep Learning and Try Again!")