Feature: Register neighbourhoodPriority
		In order	to	keep	track	of my neighbourhoodPriority
		As a user
		I	want to register a neighbourhoodPriority together with its details

    Background:	There	is a registered user
			Given Exists a user "user" with password "password"

		Scenario: Register just neighbourhoodPriority action
			Given I login as user "user" with password "password"
		  When I register neighbourhoodPriority
		    | action       |
		    | test         |
	   	Then I'm viewing the details page for neighbourhoodPriority
		    | action      |
      	| test        |
		  And There are 1 neighbourhoodPriorities
