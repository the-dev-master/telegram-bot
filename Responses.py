from datetime import datetime

def sample_responses(input_text, username):
    user_message = str(input_text).lower()

    if user_message in ("hello"):

        return f"Hi {username}, you passed the test!"
    
    if user_message in ("failed"):

        return f"you failed {username}"
    
    if user_message in ("time"):

        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")
        return f"Hi {username} the time is: {date_time}"


    return "wtf?" 
    
       