# sandbox
A collection miscellaneous statistical and data-related practices

# Contents
**Files** 

**1. `chi2-practice.py`:** Using   `numpy` and `scipy`'s `stats` sub-module to perform a basic $\chi^2$ test (Pearson's test of goodness of fit).

**Sub-Directories** 

**1. `./data`**: Contains the data for the entire repo

**2. `./sqlite-practice`**: A basic SQLite database

# Setup
There's not much setup, but there's a basic virtual environment (bundle of relevant libraries). Here's how to configure that. In your terminal:

First, create the venv.

```
python3 -m venv venv
```
Then activate the venv

```
source venv/bin/activate
```

Now install the requirements
```
pip3 install -r requirements.txt
```

A quick way to test the code is to enable Python's interactive interpreter. You can run selected lines by Shift + Enter (for MacOS). That's done like this:


```
python3 # To enable the interpreter in your terminal 
exit()  # To exit
```