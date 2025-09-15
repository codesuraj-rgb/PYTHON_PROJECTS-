Q1 = '''
What is the correct file extension for Python files?
A) .pyth
B) .pt
C) .py
D) .pyt
'''
Q2 = '''
Which keyword is used to define a function in Python?
A) func
B) def
C) function
D) define
'''
Q3 ='''
What data type is used to store text in Python?
A) int
B) float
C) str
D) bool
'''
Q4 = '''
Which operator is used for multiplication in Python?
A) x
B) *
C) +
D) %
'''
Q5 = '''
What is the output of print(2 ** 3) in Python?
A) 6
B) 8
C) 9
D) 5
'''
Answer = {
    "Q1": "C",
    "Q2": "B",
    "Q3": "C",
    "Q4": "B",
    "Q5": "B"
}
user_answer = {}
def ask_question():
    print(Q1)
    user_answer["Q1"] = input("enter your answer : ").upper()
    print(Q2)
    user_answer["Q2"] = input("enter your answer : ").upper()
    print(Q3)
    user_answer["Q3"] = input("enter your answer : ").upper()
    print(Q4)
    user_answer["Q4"] = input("enter your answer : ").upper()
    print(Q5)
    user_answer["Q5"] = input("enter your answer : ").upper()
    


def show_score():
    score = 0
    if user_answer["Q1"] == Answer["Q1"]:
        score += 1
   
    if user_answer["Q2"] == Answer["Q2"] :
        score += 1
   
    if user_answer["Q3"] == Answer["Q3"] :
        score += 1
  
    if user_answer["Q4"] == Answer["Q4"] :
        score += 1

    if user_answer["Q5"] == Answer["Q5"] :
        score += 1
    if score == 0:
        print("you have got all answer wrong")
    else:  
        print(f"Your total score is: {score}/5")       
ask_question()
show_score()
                           