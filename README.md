# Tests & Code Coverage in Python
This project demonstrates the difference ways to test a python code and check the code and test coverage.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for testing purposes.

#### Prerequisite (best practices)
Create a python virtual environment and install dependencies from requirements.txt.
```
# create a virtual environment.
python -m venv venv

# activate.
source venv/bin/activate

# install dependencies.
pip install -r requirements.txt
```

#### Test modules used
 1. unittest
 2. pytest
 3. coverage (checks code coverage)
 4. pytest-cov (checks test coverage)

#### Commands to run tests
 1. unittest
    
    This is perhaps the easiest way to test your code.
    
    Run `python -m unittest test_app.py` to test app.py.
    
 2. pytest
    
    pytest shows the progress of the test cases. Run `pytest -v` to see the output. 

 3. coverage
 
    This module checks the code coverage in the source file. In this example, we have defined two functions in app.py, fibonacci and factorial. We haven't invoked these functions in app.py and hence the code is not covered.
    ```
    # run coverage on the source file to generate coverage report.
    coverage run app.py
   
    # display the coverage report.
    coverage report
   
    # look at the missing code coverage from app.py.
    coverage report --show-missing
   
    # generate report in HTML to view in browser.
    coverage html
    ```
    You can see from the HTML report that the missing lines of code are actually the function bodies.
 
 4. pytest-cov
 
    Using pytest-cov module we can check the test coverage which is actually meaningful to us. We want to make sure that our test cases cover 100% (almost) of the source code.
    ```
    # run the following command to check the test coverage.
    pytest --cov=app
   
    # to generate test coverage report in HTML.
    pytest --cov=app --cov-report=html
    ```

#### Finally
Simply run `deactivate` to end the python virtual environment.