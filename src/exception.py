# Custom exception that I made for whenever I use Try Catch blocks it will raise a custom exception.
import sys #sys modules provide vairous functions that are used to manipulate different parts of Python runtime environment.
from src.logger import logging 
'''
Whenever an exception gets raised I want to put out my own custom message.
-exc_tb, tells us on which file the exception occurred. 
-file_name, you can find the code for this in the python docementation about handling custom exceptions.
'''
def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
    file_name, exc_tb.tb_lineno,str(error)

    )

    return error_message
'''
Custom Exception Class
'''
class CustomException(Exception):
    # Populates error message
    def __init__(self,error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message, error_detail=error_detail)
    # Prints error message
    def __str__(self):
        return self.error_message

