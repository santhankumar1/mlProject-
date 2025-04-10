import sys
from logger import logging

def error_details(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message=f"Error occured in script:[{file_name}] at line number:[{exc_tb.tb_lineno}] error message:[{str(error)}]"
    return error_message
   



class CustomerException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_details(error_message,error_detail=error_detail)

        def __str__(self):
            return self.error_message
        

    
    
    
    