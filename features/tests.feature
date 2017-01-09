Feature: Onet Weather Check

  Scenario: verify title and url
    When we visit onet homepage
    Then we should see correct url address and correct title

  Scenario: check temperatures in Poznan
    When we visit onet site
    And we select Poznan from cities list
    Then we should check the temperatures

  Scenario Outline: check temperatures in other city
    When we type <cityname> other than from list
    Then we should check the temperatures in <cityname>

    Examples: Cities
      | cityname |
      | Tczew    |
      | Gdynia   |