# Created by hammadchaudhry at 12/6/22
Feature: Sign in test cases

  Scenario: Sign in page can be opened from SignIn popup
    Given Open amazon page
    When Click on button from SignIn popup
    Then Verify Sign In page opened

  Scenario: Amazon users see sign in button
    Given Open amazon page
    Then Verify Sign In is clickable
    When Wait for 5 seconds
    Then Verify Sign In is clickable
    Then Verify Sign In disappears