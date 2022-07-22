*** Settings ***
Library  RequestsLibrary
Library  OperatingSystem
Library  SeleniumLibrary
Library  webdriver
Library  ChromeDriverManager

*** Variables ***
${url}  http://localhost:8080/
${expectedcolor}  rgba(220, 53, 69, 1)
${buttontext}  Dispense Now
${expectedtext}  Cash dispensed

*** Test Cases ***
AC1
    create session  AddData  ${url}
    ${json} =  Get file  PersonDetails.json
    ${object} =  Evaluate  json.loads("""${json}""")  json
    &{body} =  Create Dictionary  birthday=${object[0]["birthday"]}  gender=${object[0]["gender"]}  name=${object[0]["name"]}  natid=${object[0]["natid"]}  salary=${object[0]["salary"]}  tax=${object[0]["tax"]}
    ${response}=  POST On Session  AddData  /calculator/insert  json=${body}
    ${code}=  convert to string  ${response.status_code}
    should be equal  ${code}  202

AC1 fail test case
    create session  AddData  ${url}
    ${json} =  Get file  ErrorPersonDetails.json
    ${object} =  Evaluate  json.loads("""${json}""")  json
    &{body} =  Create Dictionary  birthday=${object[0]["birthday"]}  gender=${object[0]["gender"]}  name=${object[0]["name"]}  natid=${object[0]["natid"]}  salary=${object[0]["salary"]}  tax=${object[0]["tax"]}
    ${response}=  POST On Session  AddData  /calculator/insert  json=${body}
    ${code}=  convert to string  ${response.status_code}
    should be equal  ${code}  500

AC2
    create session  AddData  ${url}
    ${json} =  Get file  PersonDetails.json
    ${object} =  Evaluate  json.loads("""${json}""")  json
    FOR  ${item}  IN  @{object}
    ${birthday} =  Set variable  ${item["birthday"]}
    ${gender} =   Set variable  ${item["gender"]}
    ${name} =   Set variable  ${item["name"]}
    ${natid} =   Set variable  ${item["natid"]}
    ${salary} =   Set variable  ${item["salary"]}
    ${tax} =   Set variable  ${item["tax"]}
    &{body} =  Create Dictionary  birthday=${birthday}  gender=${gender}  name=${name}  natid=${natid}  salary=${salary}  tax=${tax}
    ${response}=  POST On Session  AddData  /calculator/insert  json=${body}
    ${code}=  convert to string  ${response.status_code}
    should be equal  ${code}  202
    END

AC3
    Set Environment Variable  webdriver.chrome.driver  chromedriver
    Open browser   ${url}  chrome
    Choose File  xpath://input[@type='file']  C:/Users/ECQ985/PycharmProjects/pythonProject/test.csv
    close browser

AC5 button color
     Set Environment Variable  webdriver.chrome.driver  chromedriver
    Open browser   ${url}  chrome
    ${elem}  Get Webelement  css=.btn-danger
    ${color}  Call Method  ${elem}  value_of_css_property  background-color
     log to console  ${color}
    Should Be True  """${color}""" == """${expectedcolor}"""
    close browser

AC5 check button text
    Set Environment Variable  webdriver.chrome.driver  chromedriver
    Open browser   ${url}  chrome
    ${button}  Get Text  xpath://a[@role='button'][2]
      log to console  ${button}
    Should Be True  """${button}""" == """${buttontext}"""
    close browser

AC5 check redirected page
     Set Environment Variable  webdriver.chrome.driver  chromedriver
    Open browser   ${url}  chrome
    Click Element  xpath://a[@role='button'][2]
    ${text}  Get Text  xpath://div[@class='display-4 font-weight-bold']
    Should Be True  """${text}""" == """${expectedtext}"""
    close browser
