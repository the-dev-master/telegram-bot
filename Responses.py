from datetime import datetime

def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello"):

        return "passed the test!"
    
    if user_message in ("failed"):

        return "you failed"
    
    if user_message in ("time"):

        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")
        return date_time


    return "wtf?" 
    
       