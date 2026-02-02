"""
Step definitions for the number category feature.
"""

# TODO: Importáld a number_category modult, amikor elkészült

from behave import given, when, then


# TODO: Írd meg a step definition-öket a feature fájlban lévő scenáriók alapján


def categorize_number(number):
    """
    Determines if a number is positive, negative, or zero.
    """
    
from behave import given, when, then
from src.number_category import categorize_number

@given('the input is "{val}"')
def step_set_input(context, val):
    context.input_value = val

@given('the number is {num}')
def step_set_number(context, num):
    context.input_value = num

@when('I ask if it is positive, negative, or zero')
def step_check_category(context):
    context.result = categorize_number(context.input_value)

@then('the answer should be "{expected_category}"')
def step_verify_result(context, expected_category):
    assert context.result == expected_category, \
        f"Várt: '{expected_category}', Kapott: '{context.result}'"
    
