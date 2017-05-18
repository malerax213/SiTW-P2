Feature: Edit Outcome
  In order to keep updated my previous registers about outcomes
  As a user
  I want to edit an outcome register I created

  Background: There are registered users and an outcome by one of them
    Given Exists a user "user1" with password "password"
      | code        | name        | associated_crime |
      | 1234        | Working     | Robbery          |

  Scenario: Edit owned outcome registry name
    Given I login as user "user1" with password "password"
    When I edit the outcome with code "1234"
      | name    |
      | Working |
    Then I'm viewing the details page for outcome by "user1"
      | code        | name        | associated_crime |
      | 1234        | Working     | Robbery          |
    And There are 1 outcomes
