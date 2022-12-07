# Created by hammadchaudhry at 12/6/22
Feature: Tests for product page

  Scenario: User can select colors
    Given Open Amazon product B07MNHBRCJ page
    Then Verify user can click through colors

  Scenario: User can go through many colors
    Given Open Amazon product B07BJKRR25 page
    Then Verify each color has been selected