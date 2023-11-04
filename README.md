<h1> Budgeting App </h1> 
 
<h2>Description</h2>

A budgeting app that allows users to create new login credentials with enhanced encryption functionality. Users can input income or expense records under different categories and can easily track spending by viewing the percentage spent on each category on a pie chart.

* The pie chart below presents the data as a percentage spent on each category from the sample file cc.csv

![image](https://github.com/claireweiz/budgeting_app/blob/main/pie%20chart.png)

<h2>Skills & Tools</h2>

* Python
* Libraries include: cryptography, pandas, matplotlib

<h2>Brief Notes</h2>

The purpose of this project was to try two things: encrypt user credentials and analyse data.

I started by encrypting user credentials. After that, the encrypted data was stored to different files to ensure that no one could read the original data. In order to do this, I chose Fernet from the cryptography library for its simplicity, effectiveness and security. 

Once the user credentials have been created, the user can input expense or income data, which was then stored in a .csv file. After that, the pandas and matplotlib libraries can visualise the expense and income data entered by the user.

This was my first data analysis project using python, pandas and matplotlib. I found it very interesting to learn about the functionality of the libraries and how they work together with python. I was also excited to discover the possibilities to extend the app with more functionality. So, I have decided to extend this app in the future, budgeting app 2.0, and explore more visualisation modules and analysis models.