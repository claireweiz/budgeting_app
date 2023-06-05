<h1> My budget app </h1> 
 
<h2>Description</h2>
A budget app output to console with login system platform, to create account & password, encrypt password storage, and analyse expense & income by pie chart

* create an example file call 'cc.csv'
![image](https://github.com/claireweiz/budget_app/blob/main/pie%20chart.png)

<h2>Skills & Tools</h2>

* python
* Library includes: cryptography, pandas, matplotlib

<h2>Thoughts</h2>
This project is to try two things: encrypting password and analysing data. 

I started with encrypting and store username and password, while the raw file cannot be read directly. I chose Fernet from cryptography library because of it's simple and effective. Once username and password been created, the user can input expense or income and the data will be appended to csv file named by username.

And then I import pandas and matplotlib to visualise expense/income data by user input. There are a lot more visualisation and categorisation I am still exploring, so the budget app 2.0 will be creating more analysis options and categories.