Feature: Number Categorization
  As a user
  I want to know if a number is positive, negative, or zero
  So that I can make decisions based on its sign

  # Alapvető scenáriók (Basic Scenarios)
  Scenario: Positive number
    Given the number is 5
    When I ask if it is positive, negative, or zero
    Then the answer should be "Positive"

  Scenario: Negative number
    Given the number is -10
    When I ask if it is positive, negative, or zero
    Then the answer should be "Negative"

  Scenario: Zero
    Given the number is 0
    When I ask if it is positive, negative, or zero
    Then the answer should be "Zero"

  # Bónusz: Scenario Outline (Több eset egyben, tizedesekkel és nagy számokkal)
  Scenario Outline: Check various numbers
    Given the number is <number>
    When I ask if it is positive, negative, or zero
    Then the answer should be "<category>"

    Examples:
      | number      | category |
      | 3.5         | Positive |
      | -2.7        | Negative |
      | 1000000     | Positive |
      | -999999     | Negative |
      | 0.0         | Zero     |