*** Settings ***
Resource  resource.robot
Test Setup  Input New Command

*** Keywords ***
Create User And Input New Command
    Input New Command
    Create User  kalle  kalle12345

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kella  kella12345
    Output Should Contain  New user registered

# these do not work
Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle12345
    Input New Command
    Input Credentials  kalle  kalle12345
    Output Should Contain  Username already exists

Register With Too Short Username And Valid Password
    Input Credentials  ka  kalle12345
    Output Should Contain  Username is too short

Register With Valid Username And Too Short Password
    Input Credentials  kalle  k
    Output Should Contain  Password is too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kalle  kallekalle
    Output Should Contain  Password must contain at least one number