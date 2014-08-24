
Feature: Find the number of groups of '1' in given fields

    Scenario: visit the form of task2 and enter valid data - see the solution
        When we visit the form of task2 and enter valid data
        Then we see the solution for task2

    Scenario: visit the form of task2 and enter valid extreme data - see the solution
        When we visit the form of task2 and enter valid extreme data
        Then we see the solution for extreme task2
