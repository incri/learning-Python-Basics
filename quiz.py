from Question import Question
question_prompts = ["How many breeds of elephant are there?\n(a) 3\n(b) 4\n(c) 6\n\n",
"How many stars are on the national flag of USA?\n(a) 32\n(b) 42\n(c) 50\n\n ", 
"As of December 2021, who has the most Instagram followers?\n(a) Cristiano Ronaldo\n(b) Dwayne Johnson\n(c) Selena Gomez\n\n",
  ]
    
questions=[
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "a"),
]
def quiz_runner(questions):
    score = 0
    for question in questions:
        answer = input (question.prompt)
        if answer == question.answer:
            score +=1
    print ("you have scored" +" "+ str(score)+" "+ "out of" +" "+ str (len (questions)) +" "+ "correct") 

quiz_runner(questions)     
            



