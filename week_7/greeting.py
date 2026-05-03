
def get_greeting(daytime):
    
    if daytime < 12:
        return "Good morning"
    elif daytime < 18:
        return "Good afternoon"
    else:
        return "Good evening"
