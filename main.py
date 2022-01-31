THEME_COLOR = "#375362"
FONT=("Arial",15,"italic")
from tkinter import *

from quiz_brain import QuizBrain


class Quizinterface:
    def __init__(self,quizbrain:QuizBrain):
        self.window= Tk()
        self.score=0
        self.quiz=quizbrain

        self.set()
        self.label=Label(text=f"Score: {self.score}",bg=THEME_COLOR,fg="white",pady=20)
        self.label.grid(row=0,column=1)
        # self.menu = StringVar()
        # self.menu.set("Any")
        # self.drop= OptionMenu(self.window,self.menu,"Any","Entertainment:Films","Science & Nature","General knowledge")
        # self.drop.grid(row=0,column=0)
        # self.bsub=Button(highlightthickness=0,command=self.chosenCategory)
        # self.bsub.grid(row=3,column=0)
        self.canvas = Canvas(width="300", height="250", highlightthickness=0,bg="white")
        self.question_text=self.canvas.create_text(150,125,text="Some text",fill=THEME_COLOR,
                                                   font=FONT,width=200)

        self.canvas.grid(row=1, column=0, columnspan=2,pady=50)

        self.tick_image = PhotoImage(file="images/true.png")
        self.correct = Button(image=self.tick_image, highlightthickness=0,command=self.trueAnswered)
        self.correct.grid(column=0, row=2,pady=50)
        cross_image = PhotoImage(file="images/false.png")
        self.wrong = Button(image=cross_image, highlightthickness=0,command=self.falseAnswered)
        self.wrong.grid(row=2, column=1,pady=50)
        self.get_next()
        self.window.mainloop()


    def set(self):
        self.window.title("Quiz App")
        self.window.config(bg=THEME_COLOR,padx=20, pady=20)

    def get_next(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.qtext=self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=self.qtext)


    def falseAnswered(self):
        is_right = self.quiz.check_answer("false")
        print(is_right)
        self.feedback(is_right)
        #self.get_next()

    def trueAnswered(self):
        is_right=self.quiz.check_answer("True")
        print(is_right)
        self.feedback(is_right)


    # def check(self,is_right):
    #     if is_right==True:
    #         self.score+=1
    #         print(self.score)
    #
    #         self.feedback()
    #     else:
    #         self.feedback(False)

    def feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next)

    # def chosenCategory(self):
    #     choice=self.menu.get()
    #     if(choice=="Entertainment"):
    #         id=
