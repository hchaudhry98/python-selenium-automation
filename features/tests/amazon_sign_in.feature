# Created by hammadchaudhry at 10/6/22
Feature: Tests for sign in

  Scenario: Logged out user sees Sign In when clicking on Orders
    Given Open amazon page
    When Click on Returns & Orders page
    Then Verify Sign In page opened