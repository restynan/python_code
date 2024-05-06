class CustomError(Exception):
    """
    Exception raised when a specific error is needed
    """
    def __init__(self, message, code):
        super().__init__(f"{message}  with error code {code}")
        self.code = code


error = CustomError("test", 400)
print(error.__doc__)
raise CustomError("OUCH! An error happened", 500)

#try :
#except
#finally  or else

