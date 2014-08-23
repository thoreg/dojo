
Feature: Find the shortest earliest range in a text which contains all given words

    Scenario: visit the form and enter valid data - see the solution
        When we visit the form and enter valid data
        Then we see the solution

    Scenario: visit the form and enter invalid data - see the error message
        When we visit the form and enter invalid data
        Then we see the error message