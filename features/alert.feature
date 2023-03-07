@web @alert
Feature: Simple Alert
  After clicking on button alert is present

  Scenario: Test 1
    Given Open Page To Delete User
    When Click delete button
    And Accept all alerts
    Then Check Url


    # how to select features for running?
