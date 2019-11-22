Feature: 
  As a user starting the orchd program
  I want to be reminded of the syntax
  When I try to start the command with the wrong arguments
  Or when I request help

  @wip
  Scenario: run with no arguments
    Given I have not started "orchd"
    When I run the comamnd with no arguments
    Then it prsents me with usage

  Scenario: run the command with -h
    Given I have not started "orchd"
    When I run the command with -h
    Then it presents me with usage
    
  Scenario: run the command with --help
    Given I have not started "orchd"
    When I run the command with --help
    Then it presents me with usage
