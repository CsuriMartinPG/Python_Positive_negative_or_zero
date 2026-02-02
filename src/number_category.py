

"""
Production code - This is the application code that we are testing.
This module contains the business logic for categorizing numbers.
"""


def categorize_number(number):
    """
    Kategorizálja a számot pozitív, negatív vagy nulla kategóriába.
    
    Args:
        number (int vagy float): A kategorizálandó szám
        
    Returns:
        str: "Pozitív" ha a szám > 0, "Negatív" ha < 0, "Nulla" ha = 0


    TODO: Implementáld ezt a függvényt!
    Példa:
        categorize_number(5) -> "Pozitív"
        categorize_number(-3) -> "Negatív"
        categorize_number(0) -> "Nulla"
    """

    num = float(number)
    
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"
        # TODO: Írd meg az implementációt!