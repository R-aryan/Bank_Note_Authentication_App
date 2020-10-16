# Bank Note Authentication App


- Deployed at - https://bank-na.herokuapp.com/apidocs
- Click the above link to go to the deployed website


A basic web app deployed at heroku, which classifies whether a note is fake or 
not based on certain parameters, using supervised machine learning algorithms.

The Parameters/Columns Used in the dataset are.

- [Variance](https://en.wikipedia.org/wiki/Variance)
- [Skewness](https://en.wikipedia.org/wiki/Skewness#:~:text=In%20probability%20theory%20and%20statistics,zero%2C%20negative%2C%20or%20undefined.)
- [Kurtosis](https://en.wikipedia.org/wiki/Kurtosis#:~:text=In%20probability%20theory%20and%20statistics,a%20real%2Dvalued%20random%20variable.)
- [Entropy](https://en.wikipedia.org/wiki/Entropy_(information_theory)#:~:text=In%20information%20theory%2C%20the%20entropy,A%20Mathematical%20Theory%20of%20Communication%22.)


This project is implemented end-to-end and is deployed at heroku, you can
click the link above or [click here](https://bank-na.herokuapp.com/apidocs) to visit the web app.

## Steps to run the project on local machine

- create a virtual environment and install **requirements.txt** file.
- After completing the above steps run the file **main.py** in your terminal.
- After running **main.py** you will get an url(eg- http://127.0.0.1:5000/) copy this URl and paste it to your browser.
- At the end of the URL add  **apidocs/ eg-(http://127.0.0.1:5000/apidocs)** and then pres enter.
- Your flask application is now up and running and should look something like this.
![Image of Webpage](https://github.com/R-aryan/Bank_Note_Authentication_App/blob/feature/phase-1/src/static/demo_image_1.PNG).

- Click on **GET** Method and You see a form something like this.
![Image of Form](https://github.com/R-aryan/Bank_Note_Authentication_App/blob/feature/phase-1/src/static/demo_image_2.PNG).

- Click on **Try it Out** and enter the values in the form as shown in the figure and after entering the values click on **Execute** 
![Image of Form with values](https://github.com/R-aryan/Bank_Note_Authentication_App/blob/feature/phase-1/src/static/demo_image_3.PNG).

- After clicking on **execute** you will get a result as shown in the figure.
![Image of Result](https://github.com/R-aryan/Bank_Note_Authentication_App/blob/feature/phase-1/src/static/demo_image_4.PNG).

- Similarly you can also upload a csv file and get predictions for multiple records, to do so click on the post method and it will appear as shown in the figure.
![Image of POST method](https://github.com/R-aryan/Bank_Note_Authentication_App/blob/feature/phase-1/src/static/demo_image_5.PNG).

- Upload the csv and click on **execute**.

- After clicking on **execute** you will get the following result.
![Image of Result](https://github.com/R-aryan/Bank_Note_Authentication_App/blob/feature/phase-1/src/static/demo_image_6.PNG).


## For Modelling Training.

- For model training go to the [Training Directory](https://github.com/R-aryan/Bank_Note_Authentication_App/tree/feature/phase-1/src/training), and go through the notebook. 