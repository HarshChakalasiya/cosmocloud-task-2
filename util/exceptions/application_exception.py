class ApplicationException(Exception):
    def __init__(self, status_code: int = None, message: str = None):
        self.status_code = status_code
        self.message = message
