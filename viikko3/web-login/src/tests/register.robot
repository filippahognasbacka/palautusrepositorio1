*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Registration
    Registration Should Succeed  Welcome to Ohtu Application!

Register With Too Short Username And Valid Password
    Set Username  k
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Registration
    Registration Should Fail With Message  Username must be min. 3 characters and contain only lowercase letters


Register With Valid Username And Too Short Password
    Set Username  kalle
    Set Password  ka1
    Set Password Confirmation  ka1
    Submit Registration
    Registration Should Fail With Message  Password must be at least 8 characters

Register With Valid Username And Invalid Password
    Set Username  kalle
    Set Password  kalleeee
    Set Password Confirmation  kalleeee
    Submit Registration
    Registration Should Fail With Message  Password must contain letters and numbers

Register With Nonmatching Password And Password Confirmation
    Set Username  kalle
    Set Password  kalleee
    Set Password Confirmation  kalleeee
    Submit Registration
    Registration Should Fail With Message  Password and password confirmation don't match


Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Registration
    Registration Should Fail With Message  Username is already in use

*** Keywords ***

Submit Registration
    Click Button  Register 

Registration Should Succeed
    [Arguments]  ${message}
    Welcome Page Should Be Open
    Page Should Contain  ${message}

Registration Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page


