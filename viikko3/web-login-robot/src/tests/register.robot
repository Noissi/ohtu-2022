*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  nalle
    Set Password  nalle123
    Set Password Confirmation  nalle123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ka
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Register Should Fail With Message  Invalid username

Register With Valid Username And Too Short Password
    Set Username  useruser
    Set Password  user1
    Set Password Confirmation  user1
    Submit Credentials
    Register Should Fail With Message  Invalid password

Register With Nonmatching Password And Password Confirmation
    Set Username  user123
    Set Password  salasana123
    Set Password Confirmation  salasana12
    Submit Credentials
    Register Should Fail With Message  Passwords do not match

Login After Successful Registration
    Set Username  jee
    Set Password  jeejee666
    Set Password Confirmation  jeejee666
    Submit Credentials
    Register Should Succeed
    Go To Login Page
    Set Username  jee
    Set Password  jeejee666
    Submit Login Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  jee2
    Set Password  jeejee
    Set Password Confirmation  jeejee
    Submit Credentials
    Register Should Fail With Message  Invalid password
    Go To Login Page
    Set Username  jee2
    Set Password  jeejee
    Submit Login Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Submit Login Credentials
    Click Button  Login

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Create User And Go To Register Page
    Create User  kalle  kalle123
    Go To Register Page
    Register Page Should Be Open
