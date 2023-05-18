# ![TheEthicalWineCellar logo](/media/tewc_logo.jpg) The English Wine Cellar 

![am I responsive] Image

# Introduction
The English Wine Cellar is an online retailer of English wines and wine accessories. They also provide wine tasting experiences to compliment their core business.

### The Emergence of the British Wine Industry
In the past, English wine was thought of as being below the standards of European wines and those from warmer climes, as England didn't have the required climate or expertise.

This has changed in recent years, partly due to customer perception and the emphasis on 'buying local' by ethically minded consumers in order to contribute to a healthy environment.

Britain's changing climate and knowledgeable winemakers has meant that the UK can now compete with their continental neighbours in regard to producing good quality wine.

However, Britain cannot, at present, produce the quantities to match those from other major wine producing regions. The lower yield and supply of British wines, means that the cost to the end consumer will be high.

The live website can be found [here](https://the-english-wine-cellar.herokuapp.com/)

# Contents
* [Planning](#planning)
* [Development](#development)
* [Marketing](#marketing)
* [Features](#features)
* [Technologies](#technologies)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)
* [Acknowledgements](#acknowledgements)

## Planning
### Business Model

The English Wine Cellar is a B2C ecommerce retailer of English wines. In addition they sell glassware and provide wine tasting experiences to complement their core product offering.

The business' target audience have the following attributes:

- Mid 30s - late 40s
- Professional
- High disposable income (money no object)
- Enjoy finer things in life
- Appreciate quality
- Repeat buyers

### Problem Statement
The number of outlets for English wines are smaller in number than the imported wines from other regions. This is due to the emergence of the home grown product being a relative new entrant to market and low quantities produced. This is not a mass market product, but quite niche in that it is defined by quality and price. Availability is limited to high end outlets and direct from the winemakers/vineyards.


### Project Objectives
- The objectives of the site is to drive sales of English wines through a B2C web application, including the provision of wine tasting experiences that can be booked online.

### User Experience (UX) Goals

### External User's Goal
- Users can purchase good quality English wines and/or book tasting experiences. They can also purchase wine accessories, such as wine glasses and decanters.

### Site Owner's Goal
- Sell English/British wines within the UK to consumers (B2C).
- Promote English wines, educate potential customers and encourage repeat business.

## Development
Journey Map - touch points:

![journey_map_touch_points](documentation_assets/images/journey_map_touch_points.PNG)
  
## User Stories Epics & Sprints


## Database Schema (ERD)

## Wireframes

## Surface
- Colour Scheme
- Typography
- Logo

## Features & Responsive Design

## Technologies

## Marketing
- SEO - keywords

## Testing & Validating

## Deployment
## Deployment

### PostgreSQL Database

<details>
    <summary></summary>

Whilst in mid-project I followed steps provided by the Code Institute to migrate the database from the Heroku version to Elephant. 

1. If using Elephant, navigate to elephantsql.com and click 'Get a managed database today'. When presented with options for differing plans, I chose the free 'Tiny Turtle' plan.
2. Select “Log in with GitHub” and authorize ElephantSQL with your selected GitHub account.
3. In the Create new team form:
    * Add a team name (your own name is fine).
    * Read and agree to the Terms of Service.
    * Select Yes for GDPR.
    * Provide your email address.
    * Click “Create Team”.
4. Your account should now be created.
5. Now you will need to create your database. Navigate to your elephantsql.com dashboard, and click "Create New Instance".
6. Set up your plan:
    * Give your plan a Name (this is commonly the name of the project).
    * Select the Tiny Turtle (Free) plan.
    * You can leave the Tags field blank.
7. Select a data center near you.
8. Then click "Review".
9. Check your details are correct and then click "Create Instance".
10. Return to the ElephantSQL dashboard and click on the database instance name for this project.
11. You will return to this projects dashboard as part of the steps to 'Deploy with Heroku' as you will need the DATABASE_URL.

</details>

### Gmail SMTP

<details>
    <summary>

Gmail SMTP has been used to send order confirmations and user contact emails in the deployed version. To use this configuration, copy and adapt the code below into your settings.py file.

```
if 'DEVELOPMENT' in os.environ:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    DEFAULT_FROM_EMAIL = '(ADD YOUR EMAIL ADDRESS)@gmail.com'
else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_USE_TLS = True
    EMAIL_PORT = 587
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_HOST_USER =  os.environ.get('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASS')
    DEFAULT_FROM_EMAIL = os.environ.get('EMAIL_HOST_USER')
```
</summary>
</details>


### Amazon Web Services (AWS) Storage

<details>
    <summary>
Considering the development of the site could require a significant volume of product images, AWS has been used as the cloud host for imagery. To implement this you will need and AWS account and to create an S3 Bucket and User Profile. Developer guidance can be followed on AWS's site.

To serve the images you will need to add the following config to your settings.py file.

```
if 'USE_AWS' in os.environ:
    # Cache control
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }
    # Bucket config
    AWS_STORAGE_BUCKET_NAME = 'the-coffee-collective'
    AWS_S3_REGION_NAME = 'eu-west-2'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    # Static and media files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'
    # Override static and media URLs in Production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}'
```
</summary>
</details>


### Stripe

<details>
    <summary></summary>

Stripe has been used to receive payments from customers. To implement you need to have an account with Stripe and follow the [documentation](https://stripe.com/docs) add incorporate the guided HTML, Python and JavaScript code. Be sure to add the secret key generated with Stripe to your Heroku Config Variables.

Once Stripe is activate you can test the checkout process with a test credit card detail provided by Stripe. Please use these details (below) and not real card details as there is no guarantee monies can be returned as this is a fictitious site.

| CARD NO             | MM / YY | CVC | Post Code |
| ------------------- | ------- | --- | --------- |
| 4242 4242 4242 4242 | 04 / 24 | 242 | 42424     |

</details>


### Deploy with Heroku

<details>
    <summary></summary>

1. Log in to Heroku at https://heroku.com - create an account if needed.
2. From the Heroku dashboard, click the Create new app button. For a new account an icon will be visible on screen to allow you to Create an app, otherwise a link to this function is located under the New dropdown menu at the top right of the screen.
3. On the Create New App page, enter a unique name for the application and select region. Then click Create app.
4. On the Application Configuration page for the new app, click on the Resources tab.
5. Next, click on Settings on the Application Configuration page and click on "Reveal Config Vars".
6. Add a new Config Var called DISABLE_COLLECTSTATIC and assign it a value of 1, and click Add to save it. Remove this when releasing for Production.
7. Add a new Config Var called SECRET_KEY and assign it a value - any random string of letters, digits and symbols, and click Add to save it.
8. Add a new Config Var called DATABASE_URL and paste in the value for your ElephantSQL database, and click Add to save it.
9. The settings.py file should be updated to use the DATABASE_URL and SECRET_KEY environment variable values as follows :

        DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}

        SECRET_KEY = os.environ.get('SECRET_KEY')

10. In Gitpod, in the project terminal window, to initialize the data model in the postgres database, run the command : python3 manage.py migrate
11. Update the requirements.txt file with all necessary supporting files by entering the command : pip freeze > requirements.txt
12. Commit and push any local changes to GitHub.
13. In order to be able to run the application on localhost, add SECRET_KEY and DATABASE_URL and their values to env.py

Connect GitHub Repo to Heroku App

1. Navigate to Application Configuration page for the application on Heroku and click on the Deploy tab.
2. Select GitHub as the Deployment Method and if prompted, confirm that you want to connect to GitHub. Enter and search for the required repository, then click on Connect to link them up..
3. Scroll down the page and choose to either Automatically Deploy each time changes are pushed to GitHub, or Manually deploy - I chose the latter for the initial deployment to watch the build and then opted for Automatic Deployment.
4. The application can be run from the Application Configuration page by clicking on the Open App button.
5. Each time you push code from your GitHub Repo it will be automatically reflected in your Heroku App.

The url for this website can be found here https://the-coffee-collective.herokuapp.com/
</details>


### Pre Production Deployment

<details>
    <summary></summary>

When you are ready to move to production, the following steps must be taken to ensure your site works correctly and is secure.

In GitPod:
1. Set DEBUG flag to False in settings.py
2. Check the following line exists in settings.py: X_FRAME_OPTIONS = 'SAMEORIGIN'
3. Update the requirements.txt file with all necessary supporting files by entering the command : pip freeze > requirements.txt
4. Commit and push code to GitHub
In the Heroku App:
5. Settings > Config Vars : Delete environment variable : DISABLE_COLLECTSTATIC
6. Deploy : Click on deploy branch
</details>

## Credits & Acknowledgements
