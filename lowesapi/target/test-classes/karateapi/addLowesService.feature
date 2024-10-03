Feature: Creating Lowe's Installation & Service Details
 
Scenario: Testing the POST call for Installation & Service Creation
  
Given url 'http://localhost:3000/services'
And request { "service": "Exterior Home", "product": "Gutters", "city": "Arlington Heights", "zipcode": "60005" }
When method POST
Then status 200
* match response.service == "Exterior Home"
* match response.product == "Gutters"
* match response.city == "Arlington Heights"
* match response.zipcode == "60005"
* print response

Scenario: Testing the POST call for Installation & Services with missing fields
Given url 'http://localhost:3000/services'
And request { "service": "Appliances", "product": ,"city": "Northbrook", "zipcode": }
When method POST
Then status 400
* match response.error == "Product, city, and zipcode are required."