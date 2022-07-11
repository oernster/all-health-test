# all-health-test v1.01

Run pre-requisites...

Install git.

Clone the repo.

Install python3.

Install virtualenv.

Enter command: virtualenv venv.

Enter command: source venv/bin/activate or the equivalent on windows if not using a linux box.

Enter command: pip3 install -r requirements.txt

Enter command: uvicorn main:app --reload

Go to http://127.0.0.1:8000 on your favourite browser.  Further instructions there.

# High level requirements:
Use the http://fixer.io/ API to ingest currency rates.

Provide a CLI which when executed will ingest the data from the 3rd party API. Store the currency rates data in a Database.

Provide a HTTP API which can be used to retrieve the currency rates for a given date. Technical requirements:

Write code as you normally would write for deployment to a production environment. Use Python version 3.8 or above.

Use Django/Flask/FastAPI web framework for the HTTP API.

Provide instructions on how to install and run the application.

NOT implemented...

Document (in a text/markdown file) how you could go about deploying & monitoring the application.


If you ran out of time on any of the high level requirements, write down which you specifically did not yet implement.

Try to spend no more than 4 hours on the exercise. Submit a pull request with your code or send it directly via email.

 
