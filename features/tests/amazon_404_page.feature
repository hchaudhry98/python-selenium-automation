# Created by hammadchaudhry at 12/6/22
Feature: Tests for 404 page

  Scenario: User is able to navigate to amazon blog from 404 page
    Given Open Amazon product B07SLODKFNSDKIFL page
    And Store original window
    When Click on a dog image
    And Switch to new window
    Then Verify blog is opened
    And Close blog
    And Return to original window
