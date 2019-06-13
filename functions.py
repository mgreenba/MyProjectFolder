"""A collection of functions for doing my project."""

"""
Needed imports for the code to run
"""
import string
import random
import nltk
import time

def get_input():
    """
    This function asks user for an input message
    
    Returns
    ----------
    the message for input
    
    out_msg
    """
    
    msg = input('INPUT :\t')
    out_msg = None
    
    return msg, out_msg

def is_question(input_string):
    """
    This function determines if input 
    from user is a question
    
    Parameter
    ---------
    input_string: str
    
    Returns
    -------
    output: bool
    if it is a question mark,
    returns true, if not
    false.
    
    """
    
    if '?' in input_string:
        output = True
    else:
        output = False
    
    return output

def is_character(input_string):
    """
    function determines if input
    from user has a certain character
    
    Parameter
    ---------
    input_string: str
    
    Returns
    -------
    output: bool
    if it is a character,
    returns true, if not
    false.
    
    """
    
    if '@' in input_string:
        output = True
    
    elif '#' in input_string:
        output = True
    
    elif '$' in input_string:
        output = True
        
    elif '%' in input_string:
        output = True
    
    elif '^' in input_string:
        output = True
     
    elif '*' in input_string:
        output = True 
        
    else:
        output = False
    
    return output

def is_greeting(input_string):
    """
    function determines if input 
    from user is a greeting
    
    Parameter
    ---------
    input_string: str
    
    Returns
    -------
    output: bool
    if it is a greeting,
    returns true, if not
    false.
    
    """
    
    if 'hi' in input_string:
        output = True
    
    elif 'hello' in input_string:
        output = True
    
    elif 'greetings' in input_string:
        output = True
        
    elif 'hey' in input_string:
        output = True
    
    elif 'hola' in input_string:
        output = True
     
    elif 'yo' in input_string:
        output = True 
        
    else:
        output = False
    
    return output


def positive_user_feeling(input_string):
    """
    Function checks for the user's positive feeling
     
    Parameter
    ---------
    input_string: str
    
    Returns
    -------
    output: bool
    if it is a positive feeling,
    returns true, if not
    false.
    
    """
    if 'good' in input_string:
        output = True
    
    elif 'happy' in input_string:
        output = True
    
    elif 'great' in input_string:
        output = True
        
    elif 'well' in input_string:
        output = True
    
    elif 'blessed' in input_string:
        output = True
     
    elif 'amazing' in input_string:
        output = True 
    
    elif 'better' in input_string:
        output = True
        
    else:
        output = False
    
    return output

def neutral_user_feeling(input_string):
    """
    Function checks for the user's neutral feeling 
    
    Parameter
    ---------
    input_string: str
    
    Returns
    -------
    output: bool
    if it is a neutral feeling,
    returns true, if not
    false.
    
    """
    
    if 'okay' in input_string:
        output = True
    
    elif 'ok' in input_string:
        output = True
    
    elif 'fine' in input_string:
        output = True
        
    elif 'not bad' in input_string:
        output = True
    
    elif 'alright' in input_string:
        output = True
        
    else:
        output = False
    
    return output

def negative_user_feeling(input_string):
    """
    checks for the user's negative feeling
    
    Parameter
    ---------
    input_string: str
    
    Returns
    -------
    output: bool
    if it is a negative feeling,
    returns true, if not
    false.
    
    """
    
    if 'sad' in input_string:
        output = True
    
    elif 'tired' in input_string:
        output = True
    
    elif 'bad' in input_string:
        output = True
        
    elif 'not good' in input_string:
        output = True
    
    else:
        output = False
    
    return output

def end_chat(input_list):
    """ 
    Function identifies if user types 'quit' 
    in input and if it does it ends the chat.
    
    Parameter
    ---------
    input_list: str
    
    Returns
    -------
    output: bool
    chat: bool
    
    if user types quit, output
    returns true, chat returns false
    else if they don't type  quit,
    output returns false and chat 
    returns true.
    
    """
    
    if 'quit' in input_list:
        output = True
        chat = False
        
    else:
        output = False
        chat = True
        
    return output, chat

def print_info(name, quit = "'quit'", age = 33):
    """
    This function is made to display information about
    the chat bot before the user types any input.
    
    Parameters
    ---------
    name: str
    quit: str
    age: int
    
    Returns
    -------
    ends function with a return
       
    """
    print ("My Name is", name)
    print ("My Age is", age)
    print ("To quit type:", quit)
    
    return

def return_message(out_msg, question, character, greeting, positive_feeling, neutral_feeling, negative_feeling):
    """
    This function is made to return
    all input functions to chat, with
    custom messages.
    
    Parameters
    ---------
    out_msg: str
    question: str
    character: str
    greeting: str
    positive_feeling: str
    neutral_feeling: str
    negative_feeling: str
    
    Returns
    -------
    out_msg: str
    after it checks for a
    certain input, it returns 
    the appropriate out_msg
    
    """
    # If we don't have an output yet, but the input was a question, 
    # return msg related to it being a question
    if not out_msg and question:
        out_msg = "I don't want to answer any questions. What do you want to talk about?"
        
     # If we don't have an output yet, but the input was a character, 
    # return msg related to specifing not to use characters
    if not out_msg and character:
        out_msg = 'Please do not use any characters.'
        
    # If we don't have an output yet, but the input was a greeting, 
    # return msg related to it being a greeting
    if not out_msg and greeting:
        out_msg = random.choice(["Hello, it's nice to talk to you!", 'Nice to meet you!',  "Hey - Let's chat!"])
        
    # If we don't have an output yet, but the input was a positive feeling, 
    # return a msg to respond to positive feeling
    if not out_msg and positive_feeling:
        out_msg = "I'm glad to hear that you are feeling positive!"  
        
    # If we don't have an output yet, but the input was a neutral feeling, 
    # return a msg to respond to neutral feeling
    if not out_msg and neutral_feeling:
        out_msg = "I'm glad that you feel fine, but I hope that you feel even better soon."
     
     # If we don't have an output yet, but the input was a negative feeling, 
    # return a msg to respond to negative feeling
    if not out_msg and negative_feeling:
        out_msg = "I'm so sorry to hear that, I hope that you can feel better soon!" 

    #Catch-all to say something if msg not caught & processed so far
    if not out_msg:
        out_msg = "Please use different words to describe your feelings."
        
    return out_msg

def have_a_chat():
    
    """
    This function is the main function 
    to run our chatbot. It calls
    on the print_info function. Prints
    a text. Checks for inputs while chat
    is running and uses time sleep function. 
    Prints text ouput to signify chat bot's output
    
    Returns
    -------
    out_msg: str
    returns the output message
    for the chat.
       
    """
    
    #This calls on the printinfo function 
    print_info(name = "ChatBot" )
    
    #chatbot to introduce itself and ask user how they are feeling at the beginning
    print('How are you feeling?')
    
    chat = True

    while chat:
    #while the chat is running, chatbot is checking for all the specific inputs below.
    
        # Get input message from the user
        msg, out_msg = get_input()
        
        # Check if the input is a question
        question = is_question(msg)
        
        # Check if the input has a certain character
        character = is_character(msg)
        
        # Check if the input is a greeting
        greeting = is_greeting(msg)
        
        # Check if the input is a positive feeling
        positive_feeling = positive_user_feeling(msg)
        
        # Check if the input is a positive feeling
        neutral_feeling = neutral_user_feeling(msg)
        
        # Check if the input is a positive feeling
        negative_feeling = negative_user_feeling(msg)
        
        # Check for an end msg 
        out_msg, chat = end_chat(msg)
      
    
        # specify what to return
        out_msg = return_message(out_msg = out_msg, question = question, character = character,
                                 greeting = greeting, positive_feeling = positive_feeling, 
                                 neutral_feeling = neutral_feeling, negative_feeling = negative_feeling)
        
        # this makes the output to display a second after input, to make the chatbot seem more realistic. 
        time.sleep(1)
        
        print('OUTPUT:', out_msg)