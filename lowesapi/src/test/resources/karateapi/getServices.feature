Feature: Getting all Installations and Services details

Scenario: Testing the GET ALL Lowe's Installation and Services Details
Given url 'http://localhost:3000/services'
When method GET
Then status 200 


Scenario: testing the get one User Details

Given url 'http://localhost:3000/services/3'
When method GET
Then status 200 
* match response.services.id == 3
* match response.services.service == 'Exterior Home'
Then print response

#Reading the file ExpectedOutput.json and storing same response in variable expectedResult
Given expectedResult=read('./services.json')
#Asserting the Actual Response with the Expected Response
And match response == expectedResult