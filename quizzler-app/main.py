from question_model import Question
from data import fetch_question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

def create_question_bank(question_data):
    """Convert raw question data into a list of Question objects."""
    return [Question(q["question"], q["correct_answer"]) for q in question_data]

# Ambil data dari API
question_data = fetch_question_data()

# Ubah jadi Question object
question_bank = create_question_bank(question_data)

# Inisialisasi quiz
quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)