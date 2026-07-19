import html

class QuizBrain:

    def __init__(self, q_list):
        """
        Initializes the quiz brain coordinator.
        
        Attributes:
            question_number (int): Tracks the index of the current question.
            score (int): Tracks the user's correct answers.
            question_list (list): List of Question objects to iterate through.
            current_question (Question): Holds the active Question object.
        """
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        """Checks if there are still questions remaining in the quiz bank."""
        return self.question_number < len(self.question_list)

    def next_question(self):
        """
        Retrieves the next question from the list, increments the progress index,
        and unescapes HTML entities in the question text.
        
        Returns:
            str: The formatted question string ready for the GUI display.
        """
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        
        # Parse and translate any raw HTML entity symbols (e.g., converting '&quot;' to '"')
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text}"
        # user_answer = input(f"Q.{self.question_number}: {q_text} (True/False): ")
        # self.check_answer(user_answer)

    def check_answer(self, user_answer):
        """
        Verifies the user's response against the correct answer (case-insensitive).
        
        Args:
            user_answer (str): The answer selected by the user ("True" or "False").
            
        Returns:
            bool: True if the answer is correct, False otherwise.
        """
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False