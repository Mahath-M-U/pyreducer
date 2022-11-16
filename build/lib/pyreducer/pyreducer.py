
from datetime import datetime
from typing import Any
import sys

def write_log(content: Any ,path : str = "./log.log",Fresh: bool = False) -> None:
    """Write the log to ***.txt File"""
    timeStamp = datetime.now().strftime('%d-%m-%Y:%H:%M:%S')
    if not Fresh:
        if isinstance(content,dict):
            content['timeStamp'] = timeStamp
        else:
            content = f"\n{content}, {timeStamp}"
            
        with open(f"{path}","a") as log:
            log.write(f"\n{content}")
    else:
        with open(f"{path}","w+") as log:
            width = 189
            log.write(f"\n{'#'* width}")
            log.write(f"\n\t\t :: {content} ->> {timeStamp}")
            log.write(f"\n{'#'* width}\n")

def write_log_dec(fun) -> None:
    """Write the log to ***.txt File using decorator patter"""
    try:
        log = fun()
        write_log(log)
    except Exception as e:
        exception_type, exception_object, exception_traceback = sys.exc_info()
        filename = exception_traceback.tb_frame.f_code.co_filename
        line_number = exception_traceback.tb_next.tb_lineno
        exception_info = exception_object.args[0]
        log = f"""\n '{e.__class__.__name__}' in  {filename} :\n\t {exception_info} at line number '{line_number}'"""
        write_log(log,path="./error.log")

if __name__ == "__main__":
    @write_log_dec
    def getData():
        return 1/0