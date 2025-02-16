# apps-takehome
Parts API takehome exercise for engineering candidates applying to the Apps team.

# Setup
First, you'll need to get the app running in your local environment.
1. Clone this repo: `git clone https://github.com/analyticsMD/apps-takehome`
2. Navigate into the folder and create your python virtual environment using [pyenv](https://github.com/pyenv/pyenv#installation): 
    1. `pyenv install 3.5.10`
    2. `pyenv virtualenv 3.5.10 takehome-env`
    3. `pyenv activate takehome-env` 
3. Install requirements: `pip install -r requirements.txt`
4. Run migrations: `./manage.py migrate`
5. Run: `./manage.py runserver`

Note: our application currently runs 3.5.10 and django 1.11 so we'll use those versions 

# Instructions
Parts Unlimited catalogs its seemingly unlimited parts, and this service is used by other teams to update various aspects of them through the existing endpoint. However, we've noticed that while we're not seeing errors, parts are not being updated as expected. As such, we'll need to fix the existing endpoint's functionality first, then develop a new view to be used that allows for CRUD operations on parts, in line with the functionality of our other views. We need you to accomplish the following tasks, and return a .zip of the project containing all changes necessary to accomplish all goals of both tasks.

## Task 1
The team has determined the following view is not working as expected, and the bug has been assigned to you to fix.

The relevant URL entry is:
`url(r'/part/(?P<part_id>\w+)', views.update_part)`

An example request that isn't working is:
`PUT /part/4 { "is_active": true }`

This returns 200, but does not update the database.

We need to troubleshoot the code and determine why it's not working.

Please do the following:
1. Determine why parts are not being updated, and fix whatever the bug is. Be sure to add a comment near your code to explain your reasoning.
2. Add a test to `test_part.py` to confirm the endpoint's proper functionality.


## Task 2
We'd like to build a new `part` view that has CRUD operations and utilizes [Django Rest Framework](https://www.django-rest-framework.org/tutorial/quickstart/).

1. Create a new view for updating Parts (keep the old endpoint and view in place) that allows for parts to be created, read, updated, and deleted, and utilizes DRF. Due to other teams' usage of the existing `part` API, we need to keep it in place until we can coordinate its sunsetting later.
2. Write tests to confirm the new view's functionality.

## Task 3
To support our Sales team, we'd like to build an endpoint that returns the 5 most common words in our part descriptions. To accomplish this, you'll need to create a new **DRF Action** that utilizes NLTK tokenization to aggregate the five most common words in the `description` field of our parts.