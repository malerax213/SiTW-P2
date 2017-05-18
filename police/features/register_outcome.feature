Feature: Register outcome
		In order	to	keep	track	of my outcomes
		As a user
		I	want to register an outcome together with its details

    Background:	There	is	a	registered	user
			Given Exists a user "user" with password "password"

		Scenario: Register just outcome name
			Given I login as user "user" with password "password"
		  When I register outcome
        | name                 |
        | Crime reporte        |
	   	Then I'm viewing the details page for outcome
        | name                 |
        | Crime reporte        |
		  And There are 1 outcomes
