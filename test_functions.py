"""
Test for my functions.

"""

from functions import (is_character, is_greeting, positive_user_feeling)

##
##

def test_is_character():
    """
    this is the test cell function to check if 
    the function is_character works properly
    
    """
    assert callable(is_character)
    assert isinstance(is_character('@'), bool)
    assert is_character('@') == True
    
    assert isinstance(is_character('#'), bool)
    assert is_character('#') == True
    
    assert isinstance(is_character('$'), bool)
    assert is_character('$') == True
    
    assert isinstance(is_character('%'), bool)
    assert is_character('%') == True
    
    assert isinstance(is_character('^'), bool)
    assert is_character('^') == True
    
    assert isinstance(is_character('*'), bool)
    assert is_character('*') == True
    
    assert isinstance(is_character('.'), bool)
    assert is_character('.') == False
    
    assert callable(is_character)
    
def test_is_greeting():
    """
    this is the test cell function to check if 
    the function is_greeting works properly
    
    """
    assert callable(is_greeting)
    assert isinstance(is_greeting('hi'), bool)
    assert is_greeting('hi') == True
    
    assert isinstance(is_greeting('hello'), bool)
    assert is_greeting('hello') == True
    
    assert isinstance(is_greeting('greetings'), bool)
    assert is_greeting('greetings') == True
    
    assert isinstance(is_greeting('hey'), bool)
    assert is_greeting('hey') == True
    
    assert isinstance(is_greeting('hola'), bool)
    assert is_greeting('hola') == True
    
    assert isinstance(is_greeting('yo'), bool)
    assert is_greeting('yo') == True
    
    assert isinstance(is_greeting('bye'), bool)
    assert is_greeting('bye') == False
    
    assert callable(is_greeting)

def test_positive_user_feeling():
    """
    this is the test cell function to check if
    the function positive_user_feeling works properly
    
    """
    assert callable(positive_user_feeling)
    assert isinstance(positive_user_feeling('good'), bool)
    assert positive_user_feeling('good') == True
    
    assert isinstance(positive_user_feeling('happy'), bool)
    assert positive_user_feeling('happy') == True
    
    assert isinstance(positive_user_feeling('great'), bool)
    assert positive_user_feeling('great') == True
    
    assert isinstance(positive_user_feeling('well'), bool)
    assert positive_user_feeling('well') == True
    
    assert isinstance(positive_user_feeling('blessed'), bool)
    assert positive_user_feeling('blessed') == True
    
    assert isinstance(positive_user_feeling('amazing'), bool)
    assert positive_user_feeling('amazing') == True
    
    assert isinstance(positive_user_feeling('better'), bool)
    assert positive_user_feeling('better') == True
    
    assert isinstance(positive_user_feeling('dog'), bool)
    assert positive_user_feeling('dog') == False
    
    assert callable(positive_user_feeling)    
