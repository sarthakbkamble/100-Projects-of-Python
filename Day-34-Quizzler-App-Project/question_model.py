class Question:

    def __init__(self, q_text, q_answer):
        """
        Initializes a new Question instance.
        
        Attributes:
            text (str): The actual text of the question.
            answer (str): The expected answer ("True" or "False").
        """
        self.text = q_text
        self.answer = q_answer