*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input New Command

*** Test Cases ***
Register With Valid Username And Password
	Input Credentials  Ville  ville123
	Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
	Input Credentials  nalle  salasana1234
	Output Should Contain  Username is already in use

Register With Too Short Username And Valid Password
	Input Credentials  Vi  ville123
	Output Should Contain  Invalid username

Register With Valid Username And Too Short Password
	Input Credentials  Vil  ville12
	Output Should Contain  Invalid password

Register With Valid Username And Long Enough Password Containing Only Letters
	Input Credentials  Ville  villesana
	Output Should Contain  Invalid password


*** Keywords ***
Create User And Input New Command
    Create User  nalle  kalle123
    Input New Command
