# apps-takehome
Parts API takehome exercise for engineering candidates applying to the Apps team.

# Setup
First, you'll need to get the app running in your local environment.
1. Clone this repo.
2. Navigate into the folder and create your python virtual environment using [pyenv](https://github.com/pyenv/pyenv#installation): 
  1. `pyenv install 3.5.10`
  2. `pyenv virtualenv 3.5.10 takehome-env`
  3. `pyenv activate takehome-env` 
3. Install requirements: `pip install -r requirements.txt`
4. Pre-populate the db: `sqlite3 db.sqlite3 < parts_create.sql`
5. Run: `./manage.py runserver`

Note: our application currently runs 3.5.10 and django 1.11 so we'll use those versions 

# Instructions
Parts Unlimited has a problem - a certain endpoint is throwing errors in production. The application is Django, most of it in Django-Rest-Framework. 

## Task 1
The team has determined the following view is not working as expected, and the bug has been assigned to you to fix.

The relevant URL entry is:
`url(r'/part/(?P<part_id>\w+)', views.update_part)`

An example request that isn't working is:
`PUT /part/4 { "is_active": true }`

This returns 200, but does not update the database.

We need to troubleshoot the code and determine why it's not working.

Please do the following:
1. Determine why the database is not updating and fix it. Be sure to add a comment near your code to explain your reasoning.
2. Add a test to `test_part.py` to confirm the endpoint's proper functionality.
3. Determine why the API incorrectly returns a 200 and fix it.


## Task 2
We'd like the update_parts view to leverage django-rest-framework. Please  this view. You may use the Widget view definition as an example. You'll need to do the following:

1. Create a new django model for Part matching its current structure in the database.
  - If possible, please port the existing part data into the new ORM table as part of the new Part migration.
2. Create a new view for updating Parts (keep the old endpoint and view in place).
3. Write tests to confirm the new view's functionality.
