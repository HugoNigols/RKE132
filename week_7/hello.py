
from greeting import get_greeting

def say_hello(daytime, first_name):
    
    greeting = get_greeting(daytime)

    print(f"{greeting}, {first_name}!")
