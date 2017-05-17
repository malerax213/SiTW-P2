Feature: Register crime
		In order	to	keep	track	of my crimes
		As a user
		I	want to register a crime together with its details

    Background:	There	is	a	registered	user
			Given Exists a user "user" with password "password"

		Scenario: Register just crime name
			Given I login as user "user" with password "password"
			When I register crime
					| name |
					| Kill |
			Then I'm viewing the details page for crime by "user"
					| name |
					| Kill |
			And There are 1 crimes
