import sys
import logging


def error_message_detail(error, error_detail: sys):  # type: ignore
    _, _, exc_tb = error_detail.exc_info()
    if exc_tb is None:
        return f"Error occurred with message: {str(error)}"
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    return f"Error occurred in script: {file_name} at line number: {line_number} with message: {str(error)}"


class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):  # type: ignore
        super().__init__(error_message)
        self.error_message = error_message_detail(
            error_message, error_detail=error_detail
        )

    def __str__(self):
        return self.error_message
