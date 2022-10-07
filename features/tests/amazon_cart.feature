# Created by hammadchaudhry at 10/6/22
Feature: Tests for amazon cart

  Scenario: User can test to see if cart is empty
    Given Open amazon page
    When Click on Cart icon
    Then Verify that the Cart is empty