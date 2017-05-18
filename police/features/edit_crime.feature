Feature: Edit Crime
  In order to keep updated my previous registers about crimes
  As a user
  I want to edit a crime register I created

  Background: There are registered users and a crime by one of them
    Given Exists a user "user1" with password "password"
      | category        | persisten_id    | policeman_assignated  |
      | Robbery         | 1234            | 123456789x            |

  Scenario: Edit owned crime registry persisten_id
    Given I login as user "user1" with password "password"
    When I edit the crime with category "Robbery"
      | persisten_id    |
      | 1234            |
    Then I'm viewing the details page for crime by "user1"
      | category        | persisten_id    | policeman_assignated  |
      | Robbery         | 1234            | 123456789x            |
    And There are 1 crimes
