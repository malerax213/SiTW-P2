Feature: Edit NeighbourhoodPriority
  In order to keep updated my previous registers about neighbourhoodPriorities
  As a user
  I want to edit a neighbourhoodPriority register I created

  Background: There are registered users and a neighbourhoodPriority by one of them
    Given Exists a user "user1" with password "password"
      | action           | issue            | neighbourhood |
      | Some work has... | Yesterday sth... | NewYorkSt     |

  Scenario: Edit owned neighbourhoodPriority registry issue
    Given I login as user "user1" with password "password"
    When I edit the neighbourhoodPriority with action "Some work has..."
      | issue            |
      | Yesterday sth... |
    Then I'm viewing the details page for neighbourhoodPriority by "user1"
      | action          | issue            | neighbourhood |
      | Some work has.. | Yesterday sth... | NewYorkSt     |
    And There are 1 neighbourhoodPriorities
