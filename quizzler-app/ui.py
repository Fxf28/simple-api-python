from tkinter import Tk, Label, Canvas, PhotoImage, Button
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = "Arial"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        '''Initialize the QuizInterface with a QuizBrain instance.'''
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(
            text="Score: 0",
            font=(FONT, 20, "bold"),
            fg="white",
            bg=THEME_COLOR
        )
        self.score_label.grid(row=0, column=1, padx=20, pady=20)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150, 125,
            text="Some Question Text..",
            width=280,
            font=(FONT, 16, "italic"),
            justify="center",
            fill=THEME_COLOR
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        self.create_answer_buttons()

        self.get_next_question()
        self.window.mainloop()

    def create_answer_buttons(self):
        """Create True/False answer buttons."""
        self.true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(
            image=self.true_image,
            highlightthickness=0,
            command=self.true_pressed
        )
        self.true_button.grid(row=2, column=0, padx=20, pady=20)

        self.false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(
            image=self.false_image,
            highlightthickness=0,
            command=self.false_pressed
        )
        self.false_button.grid(row=2, column=1, padx=20, pady=20)

    def activate_button(self):
        """Activate button state."""
        self.true_button.config(state="normal")
        self.false_button.config(state="normal")

    def disable_button(self):
        """Deactivate the button state."""
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")

    def get_next_question(self):
        """Fetch the next question from the quiz."""
        self.canvas.config(bg="white")
        self.activate_button()
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text, fill=THEME_COLOR)
        else:
            self.game_over()

    def true_pressed(self):
        """Handle the True button press."""
        self.give_feedback("True")

    def false_pressed(self):
        """Handle the False button press."""
        self.give_feedback("False")

    def give_feedback(self, user_answer: str):
        """Provide feedback to the user based on their answer."""
        is_right = self.quiz.check_answer(user_answer)
        if is_right:
            self.canvas.config(bg="green")
            self.canvas.itemconfig(self.question_text, text="You're Correct", fill="white")
        else:
            self.canvas.config(bg="red")
            self.canvas.itemconfig(
                self.question_text,
                text=f"You're Wrong\nThe correct answer was: {self.quiz.current_answer}",
                fill="white"
            )
        self.score_label.config(text=f"Score: {self.quiz.score}")
        self.disable_button()
        self.window.after(1000, self.get_next_question)

    def game_over(self):
        """Handle the end of the game."""
        self.canvas.config(bg="white")
        self.canvas.itemconfig(
            self.question_text,
            text=f"Game Over!\nYour final score: {self.quiz.score}",
            fill=THEME_COLOR
        )

        if self.true_button.winfo_exists():
            self.true_button.destroy()
        if self.false_button.winfo_exists():
            self.false_button.destroy()

        self.restart_image = PhotoImage(file="images/restart.png")
        self.restart_button = Button(
            image=self.restart_image,
            highlightthickness=0,
            command=self.restart_quiz
        )
        self.restart_button.grid(row=2, column=0, columnspan=2, pady=20)

    def restart_quiz(self):
        """Handle restarting game."""
        self.quiz.reset()
        self.score_label.config(text="Score: 0")

        if hasattr(self, "restart_button") and self.restart_button.winfo_exists():
            self.restart_button.destroy()

        self.window.config(bg=THEME_COLOR)

        self.create_answer_buttons()

        self.get_next_question()
