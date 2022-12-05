# Created by hammadchaudhry at 12/4/22
Feature: Tests for amazon main page

  Scenario: Hamburger menu is present
    Given Open amazon page
    Then Verify hamburger menu is present

  Scenario: Footer has correct amount of links
    Given Open amazon page
    Then Verify that footer has 37 links