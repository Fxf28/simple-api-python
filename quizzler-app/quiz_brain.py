import html

class QuizBrain:
    def __init__(self, q_list):
        """
        Initialize the QuizBrain object.

        Args:
            q_list (list): A list of Question objects containing question text and answers.
        """
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        """
        Check if there are more questions remaining in the quiz.

        Returns:
            bool: True if there are more questions left, False otherwise.
        """
        return self.question_number < len(self.question_list)

    def next_question(self):
        """
        Retrieve the next question from the question list.

        This method updates the current question and increments the question number.
        HTML entities inside the question text will be unescaped before displaying.

        Returns:
            str: The formatted question string if there are questions left, 
                 otherwise None.
        """
        if self.still_has_questions():
            self.current_question = self.question_list[self.question_number]
            self.question_number += 1
            q_text = html.unescape(self.current_question.text)
            return f"Q.{self.question_number}:\n\n{q_text}"
        return None

    def check_answer(self, user_answer):
        """
        Check if the user's answer matches the correct answer.

        Args:
            user_answer (str): The answer provided by the user.

        Returns:
            bool: True if the answer is correct, False otherwise.
        """
        if not self.current_question:
            print("No current question to check the answer against.")
            return False
        correct_answer = self.current_question.answer
        if user_answer == correct_answer:
            self.score += 1
            return True
        return False

    @property
    def current_answer(self):
        """
        Get the correct answer for the current question.

        Returns:
            str or None: The correct answer if a question is active, 
                         otherwise None.
        """
        return self.current_question.answer if self.current_question else None

    def reset(self):
        """
        Reset the quiz state.

        This will reset the question number, score, and clear the current question.
        """
        self.question_number = 0
        self.score = 0
        self.current_question = None
