#TODO: make error class that handles errors and returns it to UI (at least in textbrowser)


class ErrorIntoUI(BaseException):
    def __init__(self, error_message):
        self.error_message = error_message

    def __str__(self):
        return self.error_message