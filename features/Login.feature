Feature: Gmail login

@test
Scenario: Sing in to Gmail and click Compose
Given I sing in to Gmail
When I click on the Compose Button
Then I sign-Out from the gmail account