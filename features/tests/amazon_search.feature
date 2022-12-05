# Created by hammadchaudhry at 10/6/22
Feature: Tests for amazon search


  Scenario Outline: User can search for a product
    Given Open amazon page
    When Search for <product>
    Then Search results for <search_result> are shown
    Examples:
      | product                                | search_result                            |
      | coffee                                 | "coffee"                                 |
      | mug                                    | "mug"                                    |
      | dress                                  | "dress"                                  |
      | Tritan Farm to Table Pitcher on amazon | "Tritan Farm to Table Pitcher on amazon" |


  Scenario: User can add a product to the cart
    Given Open amazon page
    When Search for iPhone case
    And Click on first product
    And Click on Add to Cart button
    And Click on Cart icon
    Then Verify cart has 1 item

  Scenario: Verify there are 5 links in best seller page
    Given Open bestsellers page
    Then Verify there are 5 links