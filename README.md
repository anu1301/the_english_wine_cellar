# ![TheEthicalWineCellar logo](/media/tewc_logo.jpg) The English Wine Cellar 

![am I responsive] Image

# Introduction
The English Wine Cellar is a B2C ecommerce retailer of English wines. In addition they sell glassware and provide wine tasting experiences to complement their core product offering.

In the past, English wine was thought of as being below the standards of European wines and those from warmer climes, as England didn't have the required climate or expertise.

All of this has changed in recent years, partly due to customer perception and the emphasis on buying local by ethically minded consumers in order to contribute to a healthy environment.

Britain's changing climate and knowledgeable winemakers has meant that the UK can now produce good wine and compete with their continental neighbours.

The live website can be found [here](https://the-english-wine-cellar.herokuapp.com/)

# Note to assessor: This is an incomplete project and the work is still in progress.

The intention was to build a site incoporating an e-commerce wine store, being the core business, a wine tasting experience offering, which would be part of the business model to increase revenue from the wine tasting and sale of wine online, as well as selling wine in store. This would allow customers to try before they bought, in-store and online. The intent was also to have repeat business, from the success of the wine tasting business.

I embarked on what I thought, an exciting and relatively straight forward project. However, the complexity of what I was trying to achieve became very apparent when I continually hit road blocks on how to apply code logic to what I was trying to achieve, not to mention the amount of times errors and broken code rendered the project useless, which took many hours and days to resolve. In the end I was too far commited and invested to have time to role back and find an easier route to completing this project on time with the requirements.

## Listed below are issues and challenges:

* Following deployment, the products and experiences created in the local environment have not been rendered in the deployed site. I attempted to dump data then loaddata (see fullDB.json file). I didn't know how to reference this in DATABASES in settings.py. Sadly, you will not see any products created in the deployed site.

* When adding experiences to sessions (it has its own sessions basket called bookings - wine glass icon) the date selected at experience detail level does not render in the sessions. This is a particulary difficult challenge which will require a lot of head scratching. There are perhaps the usage of serializers (but at the moment this is beyond my experience or knowledge). Possibly a js function could be employed - again this is at the moment beyond my capabilities.

* I tried to use the same Stripe credentials for experiences as the one for products. I created a separate booking out form, but of course I realised too late why it wasn't working. The IDs used for product level couldn't be used again and even when I changed the IDs for booking out, I realised that the access keys had IDs too. I could try and resolve this by using the same checkout form as the products, which will no doubt require an if/else statement. My other issue is if I can call two different sessions in the same def in views, i.e. two sets of dictionaries from different apps, and if so perhaps I could use an if/else statement here too.

* Please note the following:
- A commercial Facebook page has not been set up.
- Webhooks haven't been tested - honestly, I don't know how to.
- News letter/Mail Chimp hasn't been set up
- The site hasn't been tested or validated
- The Readme document hasn't been written, apart from the structure

I understand that this project is an instant fail, but I did want you to understand the challenges and difficulties I have faced whilst working on this project. However, there is much you can see of the project in the local environment.


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
### Project
- Build a site to sell English wines and provide wine tasting experiences that can be booked online

### External User's Goal
- Users can purchase good quality English wines and/or book tasting experiences. They can also purchase wine accessories, such as wine glasses and decanters.

### Site Owner's Goal
- Sell English/British wines within the UK to consumers (B2C).
- Promote English wines, educate potential customers and encourage repeat business.

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

## Credits & Acknowledgements
