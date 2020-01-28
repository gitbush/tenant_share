# Tenant Share 

<div align="center">
    <img src="https://i.ibb.co/nPVS5nW/tenant-share-dark.png" alt="tenant-share-dark" href="https://tenantshare.herokuapp.com/" target="_blank" rel="noopener" alt="Tenant Share" aria-label="Tenant Share" border="0">
</div>

After living in various share houses throughout my early twenties in London, it's not always easy to raise maintenance issues with the landlord/property manager. Tenant Share provides a simple, collective way to communicate any issues to the landlord/property manaager. 

## Instructions

To test the functionality of this application, you will need to create both a Landlord and a Tenant account and follow the prompts to get set up.


[![Build Status](https://travis-ci.org/gitbush/tenant_share.svg?branch=master)](https://travis-ci.org/gitbush/tenant_share)


## Table of Contents
1. [UX](#ux)
    - [Goals](#goals)
        - [Visitor Goals](#visitor-goals)
        - [Business Goals](#business-goals)
    - [User Stories](#user-stories)
    - [Design Choices](#design-choices)
    - [Wireframes](#wireframes)

2. [Features](#features)
    - [Existing Features](#existing-features)
    - [Features Left to Implement](#features-left-to-implement)

3. [Information Architecture](#information-architecture)
    - [Database choice](#database-choice)
    - [Data Storage Types](#data-storage-types)

4. [Technologies Used](#technologies-used)

5. [Testing](#testing)
    - [Validators](#validators)
    - [Compatability](#compatibility)
    - [Automated testing](#automated-testing)  

6. [Deployment](#deployment)
    - [Heroku Deployment](#heroku-deployment)
    - [How to run this project locally](#how-to-run-this-project-locally)

7. [Credits](#credits)

8. [Disclaimer](#disclaimer)

----

# UX

## Goals

### Visitor Goals
The main target audience of Tenant Share is:
- Tenants living in house shares.
- Landlords or property managers.

The main goals of the target audience are:
- Tenants:
  - Have a common place to communicate any maintenance issues to my landlord/property manager. 
  - Track progress of an existing maintenance issue.
  - Able to pay towards any maintenance issues.
- Landlords/Property managers:
  - Raise or address any maintenance issues with my property.
  - Discuss details of any maintenance requests with the tenants.
- Tenant share meets these goals because:
  - Tenant Share has a clean and intuitive application to create and track maintenance issues related to the users property.
  - Tenant Share provides chat functionality independent to each maintenance issue.

### Business Goals
The business goals of Tenant Share are:
- To provide a central place to store all maintenance information about a property.
- To process payment of any outstanding costs related to a maintenance issue.
- Hold evidence of any work carried out eg. Invoices.

## User Stories

As a visitor to Tenant Share I want:
- General:
1. The website to be easy to navigate and not get in the way of the intended use. :heavy_check_mark:
2. To be able to view the website on mobile, tablet and desktop devices with a seamless transition. :heavy_check_mark:
3. All information to be laid out in a clean and easy to read way. :heavy_check_mark:

All users:

1. To create an account and be taken through the process step by step. :heavy_check_mark:
2. See details of my house including other tenants and the landlord/property manager. :heavy_check_mark:
3. To raise any maintenance issues that I may discover around the property. :heavy_check_mark:
4. To be able to discuss any maintenance issues with my fellow housemates and landlord/propety manager. :heavy_check_mark:
5. To pay for my share of any maintenance issues securely. :heavy_check_mark:
6. To see all previous history of maintenance issues and payments related to me. :heavy_check_mark:

Lanlord/Property manager:
1. To add/remove tenants to my property. :heavy_check_mark:
2. To set the cost and provide evidence of any maintenance issues. :heavy_check_mark:
3. To recieve payment from tenants for any work performed if responsibility lies with the tenant. :heavy_check_mark:
4. To update progress of a maintenance issue. :heavy_check_mark:

:heavy_check_mark: *Indicates implemented succesfully*

## Design Choices

Tenant Share was designed with a dashboard theme is mind. This provides a feeling of privacy and security to the user. The following design choices were made to achieve this:

### Fonts

- The primary font 'Proxima Nova' is especially useful for its high legibility, which makes it a good pick for easy-to-read text with a friendly tone.

### Icons

- Icons were used for navigation to keep the site clean and less cluttered.
- The icons were chosen as they clearly represent the related pages. 

## Wireframes

These wireframes were created using [Adobe.xd](https://www.adobe.com/uk/products/xd.html)

- [Maintenance Home](https://i.ibb.co/QvnY7d5/home.png)
- [Maintenance list](https://i.ibb.co/x6bTTww/maint-list.png)
- [Add Maintenance request](https://i.ibb.co/rF2g9MC/add-maint.png)
- [Maintenance Detail](https://i.ibb.co/kM7zGyL/Maintenance-request.png)
- [Payments](https://i.ibb.co/QvTcLqq/payments-list.png)
- [Checkout](https://i.ibb.co/Yjbyg4P/checkout.png)
- [Account](https://i.ibb.co/zNg8gpx/account.png)

# Features
 
## Existing Features

### Home/Register page
- The home page contains the register form. 
- If the user already has an account, they can follow the 'Already have an account? Log in.' link to the login page.
- The form includes username, first name, last name, register as, email, password and password confirm fields.
- Users must select either 'Tenant' or 'Landlord' for the regsiter as field. This will determine what is available once logged in.
- Once registered the user will be sent to the login page.
- Validation is provided for this form and the user will be notified of any invalid inputs after a submit attempt.

### Login page
- The login page is the same as the register page but with a login form.
- If a user has forgotten their password, a password reset link is provided. 
- Once logged in the user will be sent to their home page.
- Validation is provided for this form and the user will be notified of any invalid inputs after a submit attempt.

## Elements on every page
**Navbar:**

  - The navigation bar features on every page except for the register and login page as none of the menu items are available un-authorised users.
  - The navbar contains icon links to the account page as well as a logout link.
    - The icons were chosen as they clearly represent the destination. 
  - The Tenant Share logo is displayed on the right hand side if the navbar.

**Sidebar**

  - The sidebar features on every page except for the register and login page as none of the menu items are available un-authorised users.
  - The sidebar contains icon links to the maintenance home page, maintenance list page and payments page.
    - The icons were chosen as they clearly represent the destination. 
  - A profile image icon of the user is shown at the very top of the siebar.
  - The sidebar will hide and a hamburger menu shown on mobile and tablet devices.

## Maintenance Home Page

### **Your house section**
- If user is tenant:
  - Details of the users rental is shown with an image of the rental, address, the landlord/property manager and housemates being displayed.
  - If user is not assigned to a rental, there will be text advising the user to speak with their landlord who will add them onto the property.
- If user is landlord/property manager:
  - Details of the users rental is shown with an image of the rental, address, the landlord/property manager and housemates being displayed.
  - An occupancy indicator is shown how many rooms are filled.
  - The user can add a tenant onto the rental by clicking the 'Add tenant' button:
    - A form modal will be displayed with a search box.
    - The user can start typing the username of the tenant user they wish to add to the rental.
    - Once the correct user is identified and clicked the user is redirected back to the maintenance home page and the new tenant user is added.
  - The user can remove a tenant by clicking on the red 'x' above the relevant user:
    - This will show a modal to confirm the correct tenant to be removed.
    - Once confirm is clicked the user will be redirect to the maintenance home page and the user will be removed from the rental.
  - If user does not have a rental assigned, text will be displayed directing them to the account page to add a property.
  
## Maintenance list page 

### **Search form**
- A form section is provided so the user can filter maintenance issues.
- The fields to search are title contains, priority, status and paid by.
- The list of maintenance issues can also be sorted by date.

### **Maintenance requests list**
- Every maintenance issue related to the users rental can be seen as a preview.
- Information displayed is title, date raised, status, priority and an image.
- Each maintenance issue can be expanded into a detail view by clicking the 'View' button.
- Each maintenance issue can be deleted by clicking the 'Delete' button:
  - This will show a confirm modal to confirm the users action.
- The 'Add maintenance request' button will send the user to the creat maintenance request page.
- Pagination is available if maintenance requests exceed 5 per page.


## Maintenance request detail page
The user can switch between the 'Detail' and 'Messages' view of the maintenance request by clicking the slider at the top.

### **Detail view**
- Extra details not seen in the maintenance list page can be found including details, raised by, cost of any work needed, quote of work/invoice and the responsibilty of payment (either tenant or landlord)
- If the user is a landlord/property manager:
  - A further form is available in the cost section of the maintenance request.
  - The user can set the cost of any work and provide evidence such as quote or invoice.
  - Can update the status of the maintenance request eg, new, in progress, awaiting payment.

### **Messages view**
  - The messages tab is a place where the tenants and landlord/property manager can discuss anything related to the relevant maintenance issue.
  - A single form is shown where the user can type their message and once the 'Send' button is clicked all users related to the rental property will see the message.
  - The authors message is displayed in green to the left of the chat box and any replies in blue and to the right.

## Maintenance request create page
- A form is shown in the card with fields of title, details, prority and image.
- Validation is provided for this form and the user will be notified of any invalid inputs after a submit attempt.
- Once the form is submitted the user will be redirected to the detail page of the newly created maintenance request.

## Account page
- The user can see their details such as name, account mode (tenant or landlord) and their profile image.
- The 'Edit' button will show a dropdown with a form so the user can edit their profile details.
- If the user is a landlord/property manager:
  - A further property section will be shown underneath the profile section.
  - The user can add or edit thier property with details such as address, number of tenants and an image of the property.

## Payments page

### **Payments create form**
- A form is shown for users to create payments:
  - The user must select the relevant maintenance request they wish to pay towards and key in the amount to pay.
  - (The amount to pay can be finalised in the messages of the maintenance request and referenced in the cost section uploaded by the landlord.)
  - Once the 'Submit' button is clicked the outstanding payment will be added to the payments list.

### **Payments list**
- Clicking on the 'Pay' button will take the user to the checkout page for payment.
- The 'X' button can be used to remove a payment.
- Outstanding and fullfilled payments will be listed for future reference.
- Pagination is provided once the payments exceed 10 per page.

## Checkout page

### **Reference section**
- The maintenance request ID, maintenance request title and maintenance request ID will be shown in the checkout form for the users reference.

### **Checkout form**
- The checkout form contains the fields credit card number, CCV, expiry month and expiry year.
- Validation is provided for this form and the user will be notified of any invalid inputs after a submit attempt.
- On succesful payment the user will redirected to the payments page and the recently paid payment will now be showing 'Paid'.
  

## Features Left to Implement

1. **Welcome page**
    - At the moment the register page is used as the welcome page. In the future a new purpose built welcome page will be introduced. This will provide a better user experience.
2. **Message notification**
    - Given the time restraints and the learning experience I was unable to include a notification system for the maintenance request messages. At the moment the user will have to visit the messages tab to see if they have any new messages. 
3. **Scalabilty**
    - The ability to add more than one rental property to a landlord/property managers account will allow for management of multiple properties. At the moment only one property can be manage by the app.
4. **Rent payment**
    - Users will be able to pay their rent via Tenant Share. The landlord would be able to upload their rental agreement.
5. **Web sockets**
    - Currently the maintenance request chat functionality is done via AJAX and Django Rest Framework, making a call every 2 seconds to retreive new messages from the API. Although this method works for a small scale project, web sockets will provide a more efficient chat app.

# Information Architecture

## Database Choice

Given the site is built with Django, an SQLite3 database was used during development and a Postgress databased when deployed on Heroku..

All image fields are resized using PILLOW on upload by modifying the `def save()` method to save space and provide a squared image.

## Database models

### **Profile model**
- The profile model was extended from the `django.contrib.auth.models` User model.

| Field name | Validation | Field Type |
--- | --- | ---
| user |  User, on_delete=models.CASCADE | OneToOneField |
| rental | null=True, on_delete=models.SET_NULL | ForeignKey |
| register_as | null=True, on_delete=models.SET_NULL | CharField |
| profile_image | default='users/default_profile.jpg', upload_to=upload_to | ImageField |

- Profile image file name is modified to include the username on upload. Allows for a clean storage of profile images.

### **Maintenance models**
- The mainenance app includes the Rental and MaintRequest models.

**Rental model**

| Field name | Validation | Field Type |
--- | --- | ---
| address |  max_length=30 | CharField |
| postcode | max_length=30 | CharField |
| city | max_length=30 | CharField |
| no_of_tenants | | IntegerField |
| image | default='maintenance/no_image.jpg', upload_to=upload_to | ImageField |
| landlord | User, null=True, on_delete=models.SET_NULL | ImageField |

- Landlord field is updated with the current user when a property is created.
- Image file name is modified to include the username on upload. Allows for a clean storage of profile images.

**MaintRequest model**

| Field name | Validation | Field Type |
--- | --- | ---
| property_ref |  Rental, null=True, on_delete=models.SET_NULL | ForeignKey |
| author | User, null=True, on_delete=models.SET_NULL | ForeignKey |
| title | max_length=40 | CharField |
| details | | TextField |
| image | default='maintenance/no_image.jpg', upload_to='maintenance' | ImageField |
| priority | max_length=20, choices=PRIORITY_CHOICES | CharField |
| status | max_length=20, default='new', choices=STATUS_CHOICES | CharField |
| date_raised | default=timezone.now | DateTimeField |
| cost | null=True | IntegerField |
| paid_by | max_length=20, null=True, choices=PAID_BY_CHOICES | CharField |
| invoice_pdf | null=True, upload_to='maintenance', blank=True | FileField |

- Priority choices are Low, Med, High.
- Status choices are New, In-Progress, Awaiting payment or resolved.
- Paid_by choices are either Tenant or Landlord.

### **Chat models**

**ChatMessage model**

| Field name | Validation | Field Type |
--- | --- | ---
| maint_request |  MaintRequest, null=True, on_delete=models.CASCADE | ForeignKey |
| author | User, null=True, on_delete=models.SET_NULL | ForeignKey |
| message | | TextField |
| date_posted | default=timezone.now | DateTimeField |

### **Payments models**

**Payment model**

| Field name | Validation | Field Type |
--- | --- | ---
| maint_request |  MaintRequest, null=True, on_delete=models.CASCADE | ForeignKey |
| user | User, null=True, on_delete=models.SET_NULL | ForeignKey |
| amount | | IntegerFiled |
| payment_date | default=timezone.now | DateTimeField |
| is_paid | default=false | BooleanField |
| payment_token | max_length=120, null=True | CharField |

- Payment_token field is populated with the stripe_id on successful payment. Provides an extra layer of bookeeping.
  
# Technologies Used

### Tools
- [Visual Studio Code](https://code.visualstudio.com/) is the IDE used for developing this project. 
- [Django](https://www.djangoproject.com/) as python web framework for rapid development and clean design.
- [Stripe](https://stripe.com) as payment platform to validate and accept credit card payments securely.
- [Travis](https://travis-ci.org/) for continuous integration.
- [AWS S3 Bucket](https://aws.amazon.com/) to store images entered into the database.
- [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) to enable creation, configuration and management of AWS S3.
- [Coverage](https://coverage.readthedocs.io/en/v4.5.x/) to measure code coverage of python unittests.
- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) to style django forms.
- [Django Heroku](https://pypi.org/project/django-heroku/) to improve deployment of django projects on heroku.
- [Django Storages](https://django-storages.readthedocs.io/en/latest/) a collection of custom storage backends with django to work with boto3 and AWS S3.
- [django-cleanup](https://pypi.org/project/django-cleanup/) Automatically deletes files for FileField, ImageField and subclasses when the value of the field is changed. Used for image resizing. 
- [django-filter](https://django-filter.readthedocs.io/en/master/) Allows users to filter down a queryset based on a model’s fields. Used for the maintenance list and payment search forms.
- [django-rest-framework](https://www.django-rest-framework.org/) API used for maintenance request chat functionality.
-  [Gunicorn](https://pypi.org/project/gunicorn/) WSGI HTTP Server for UNIX to aid in deployment of the Django project to heroku.
- [Pillow](https://pillow.readthedocs.io/en/stable/) as python imaging library to aid in processing image files to store in database.
- [Psycopg2](https://pypi.org/project/psycopg2/) as PostgreSQL database adapter for Python.
- [Whitenoise](http://whitenoise.evans.io/en/stable/) to allows the web app to serve its own static files.
- [Imgbb](https://imgbb.com) to store all external images for this project.
- [PIP](https://pip.pypa.io/en/stable/installing/) for installation of tools needed in this project.
- [Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03) to handle version control.
- [GitHub](https://github.com/) to store and share all project code remotely. 
- [Browserstack](https://www.browserstack.com/) to test functionality on all browsers and devices.

### Databases
- [PostgreSQL](https://www.postgresql.org/) for production database, provided by heroku.
- [SQlite3](https://www.sqlite.org/index.html) for development database, provided by django.

### Libraries
- [JQuery](https://jquery.com) to simplify DOM manipulation.
- [Jasmine](https://jasmine.github.io/) to run automated tests on JavaScript and jQuery code.
- [Jasmine-jQuery](https://github.com/velesin/jasmine-jquery) to make it possible to test jQuery code using Jasmine.
- [Bootstrap](https://www.bootstrapcdn.com/) to simplify the structure of the website and make the website responsive easily.
- [FontAwesome](https://www.bootstrapcdn.com/fontawesome/) to provide icons for The House of Mouse webshop.
- [Google Fonts](https://fonts.google.com/) to style the website fonts.

### Languages
- This project uses HTML, CSS, JavaScript and Python programming languages.

## Testing

A thorough mix of automated and manual testing have gone into building the project. In addition to tests, I have validated all files against online validation sites, and checked compatibilities across various modern browsers and devices.

### Validators

**HTML**
- [W3C HTML Validator](https://validator.w3.org)
    - The remaining validation issues are all attributed to Django Templating not being recognized by W3C:
        - **Warning**: Consider adding a `lang` attribute to the `html` start tag to declare the language of this document.
        - **Error**: Non-space characters found without seeing a doctype first. Expected `<!DOCTYPE html>`.
        - **Error**: Element `head` is missing a required instance of child element `title`.
        - **Error**: Text not allowed in element ul in this context `{% for msg in chat_messages %}`
        - **Error**: Bad value `{{ msg.author.profile.profile_image.url }}` for attribute src on element img: Illegal character in path segment: `{` is not allowed.
        - **Error**: Duplicate attribute `%}`.

**CSS**
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
    - The compiled `.css` was checked and the below warnings remain:
      - `-webkit-box-shadow` is an unknown vendor extension 
      - `-webkit-transition` is an unknown vendor extension
      - `-webkit-box` is an unknown vendor extension
      - `-ms-grid` is an unknown vendor extension
      - `-ms-grid-columns` is an unknown vendor extension 
      - `-ms-flex-pack` is an unknown vendor extension
    

**JavaScript**
- [JShint](https://jshint.com/)
    - **script.js** and **checkout.js** were put through JSHint check with the below warnings:
    - **checkout.js**:
        - UNDEFINED VARIABLES:
            - `Stripe` (Stripe API)
            - `$` (jQuery)

**Python**
- [PEP8 Online](http://pep8online.com/)
    - All **32 .py** files checked.
    - Entirely **PEP8 compliant** with `*line too long (> 79 characters)*` exceptions:
        - eg. `payment_to_pay.payment_token = payment_form.cleaned_data['stripe_id']`
            

### Compatibility


To ensure a broad range of users can successfully use the site, I tested it across the 6 major browsers in both desktop and mobile configuration.

- **Chrome** (*v.75.0.3770.142*)
- **Edge** (*v.42.17134.1.0*)
- **Firefox** (*v.68.0.1*)
- **Safari** (*v.12.1.2*)
- **Opera** (*v.62.0.3331.99*)
- **Internet Explorer** (*v.11.885.17134.0*)

### Known Issues

### Automated Testing

With Django's built-in `unittest`, I built **29** tests to run against each app *views*, *urls*, *forms*, and *models*. Using the [coverage.py](https://coverage.readthedocs.io/en/v4.5.x/) test package, those 29 tests have provided an overall result of **79% test coverage**, which is within the approved minimum requirement for testing. All tests pass as '*OK*'! Most of the remaining Python that I didn't manually build tests for, are either built-in Django functionality or beyond my current python skill level. Below is a table detailing the **Coverage Report** - click to expand the dropdown menu.

<details>
<summary>CLICK HERE to expand the full <b>Coverage Report</b></summary>

| Name                                                   | Stmts | Miss | Cover |
|--------------------------------------------------------|-------|------|-------|
| ------------------------------------------------------ |       |      |       |
| chat\__init__.py                                       | 0     | 0    | 100%  |
| chat\admin.py                                          | 3     | 0    | 100%  |
| chat\api\__init__.py                                   | 0     | 0    | 100%  |
| chat\api\serializers.py                                | 9     | 0    | 100%  |
| chat\api\urls.py                                       | 6     | 0    | 100%  |
| chat\api\views.py                                      | 17    | 7    | 59%   |
| chat\apps.py                                           | 3     | 0    | 100%  |
| chat\forms.py                                          | 7     | 0    | 100%  |
| chat\models.py                                         | 11    | 0    | 100%  |
| checkout\__init__.py                                   | 0     | 0    | 100%  |
| checkout\admin.py                                      | 1     | 0    | 100%  |
| checkout\apps.py                                       | 3     | 0    | 100%  |
| checkout\forms.py                                      | 9     | 0    | 100%  |
| checkout\models.py                                     | 1     | 0    | 100%  |
| checkout\urls.py                                       | 3     | 0    | 100%  |
| checkout\views.py                                      | 29    | 20   | 31%   |
| errors\__init__.py                                     | 0     | 0    | 100%  |
| errors\admin.py                                        | 1     | 0    | 100%  |
| errors\models.py                                       | 1     | 0    | 100%  |
| errors\tests.py                                        | 1     | 0    | 100%  |
| errors\views.py                                        | 7     | 3    | 57%   |
| maintenance\__init__.py                                | 0     | 0    | 100%  |
| maintenance\admin.py                                   | 4     | 0    | 100%  |
| maintenance\api\__init__.py                            | 0     | 0    | 100%  |
| maintenance\api\serializers.py                         | 6     | 0    | 100%  |
| maintenance\api\urls.py                                | 6     | 0    | 100%  |
| maintenance\api\views.py                               | 7     | 0    | 100%  |
| maintenance\apps.py                                    | 3     | 0    | 100%  |
| maintenance\filters.py                                 | 11    | 2    | 82%   |
| maintenance\forms.py                                   | 41    | 2    | 95%   |
| maintenance\models.py                                  | 65    | 13   | 80%   |
| maintenance\urls.py                                    | 3     | 0    | 100%  |
| maintenance\views.py                                   | 74    | 7    | 91%   |
| manage.py                                              | 12    | 2    | 83%   |
| payments\__init__.py                                   | 0     | 0    | 100%  |
| payments\admin.py                                      | 3     | 0    | 100%  |
| payments\apps.py                                       | 3     | 0    | 100%  |
| payments\forms.py                                      | 12    | 0    | 100%  |
| payments\models.py                                     | 15    | 2    | 87%   |
| payments\urls.py                                       | 3     | 0    | 100%  |
| payments\views.py                                      | 27    | 5    | 81%   |
| tenant_share_project\__init__.py                       | 0     | 0    | 100%  |
| tenant_share_project\settings.py                       | 51    | 12   | 76%   |
| tenant_share_project\urls.py                           | 11    | 1    | 91%   |
| users\__init__.py                                      | 0     | 0    | 100%  |
| users\admin.py                                         | 3     | 0    | 100%  |
| users\api\__init__.py                                  | 0     | 0    | 100%  |
| users\api\serializers.py                               | 11    | 0    | 100%  |
| users\api\urls.py                                      | 6     | 0    | 100%  |
| users\api\views.py                                     | 17    | 8    | 53%   |
| users\apps.py                                          | 5     | 0    | 100%  |
| users\forms.py                                         | 25    | 0    | 100%  |
| users\models.py                                        | 31    | 8    | 74%   |
| users\signals.py                                       | 9     | 0    | 100%  |
| users\urls.py                                          | 4     | 0    | 100%  |
| users\views.py                                         | 61    | 42   | 31%   |
| utils\__init__.py                                      | 0     | 0    | 100%  |
| utils\admin.py                                         | 1     | 0    | 100%  |
| utils\functions.py                                     | 5     | 1    | 80%   |
| utils\models.py                                        | 1     | 0    | 100%  |
| utils\tests.py                                         | 1     | 0    | 100%  |
| ------------------------------------------------------ |       |      |       |
| TOTAL                                                  | 649   | 135  | 79%   |



</details>

In addition to the `Unittest`, I have used [Travis-CI](https://travis-ci.org/) to test Continuous Integration. but ultimately got it sorted with a successful *passing build* badge.
- insert badge
- *NOTE: this is a live/active badge, showing 'passing' at time of project submission!*

##### back to [top](#table-of-contents)

---

# Deployment

## How to run this project locally

To run this project on your own machine follow the instructions below:

Ensure you have the following tools: 
    - An IDE such as [Visual Studio Code](https://code.visualstudio.com/)

The following **must be installed** on your machine:
    - [PIP](https://pip.pypa.io/en/stable/installing/)
    - [Python 3](https://www.python.org/downloads/)
    - [Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03)

To allow you to access all functionality on the site locally, ensure you have created free accounts with the following services:
    - [Stripe](https://dashboard.stripe.com/register)
    - [AWS](https://aws.amazon.com/) and [set up an S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html)

### Instructions
1.  If you have Git installed on your system, you can clone the repository with the following command.
    ```
    git clone https://github.com/gitbush/tenant_share.git
    ```
    Alternatively save a copy of the github repository located at https://github.com/gitbush/tenant_share by clicking the "download zip" button at the top of the page and extracting the zip file to your chosen folder.

2. Open your preferred IDE, open a terminal session and cd into the correct location.

3. A virtual environment is recommended for the Python interpreter, Pythons built in virtual environment is perfect. Enter the command:
    ```
    python -m .venv venv
    ```  
_NOTE: The `python` part of this command and the ones in other steps below assumes  you are working with a windows operating system. Your Python command may differ depending on the operating system.

4. Activate the virtual environment .venv with the command:
    ```
    .venv\Scripts\activate 
    ```
_Again this **command may differ depending on your operating system**.

5. Install all required modules from the requirements.txt file
    ```
    pip -r requirements.txt.
    ```

6. Set up the following environment variables:

    - This projects environment variables are facilitated with pythons `dotenv` package set within a `.env` file and ignored with `.gitignore`. This allows for an easy way to edit the environment variables throughout development.   

    - Create a `.env` file at the project root level and input your environment variables: 

    ```
    # debug
    DJANGO_DEBUG = True

    # secret key
    SECRET_KEY = '<enter here>'

    # stripe 
    STRIPE_PUBLISHABLE = '<enter here>'
    STRIPE_SECRET_KEY = '<enter here>'

    # aws
    AWS_ACCESS_KEY_ID = '<enter here>'
    AWS_SECRET_ACCESS_KEY = '<enter here>'
    AWS_STORAGE_BUCKET_NAME = '<enter here>'

    # email
    EMAIL_HOST_ADDRESS = '<enter here>'
    EMAIL_HOST_PASSWORD = '<enter here>'
    ```

    - `DEBUG` is only set in the development environment and not when deployed to heroku. Debug mode will be available for development but not for deployment.

7. Migrate the admin panel models to create your database template with the terminal command
    ```
    python manage.py migrate
    ```

8.  Create your superuser to access the django admin panel and database with the following command, and then follow the steps to add your admin username and password:
    ```
    python manage.py createsuperuser
    ```

9.  You can now run the program locally with the following command: 
    ```
    python manage.py runserver
    ```

## Heroku Deployment

To deploy Tenant Share to heroku, take the following steps:

1. Update the `requirements.txt` file using the terminal command `pip freeze > requirements.txt`.

2. `git add` and `git commit` the new requirements and Procfile and then `git push` the project to GitHub.

3. Create a new app on the [Heroku website](https://dashboard.heroku.com/apps) by clicking the "New" button in your dashboard. Give it a name and set the region to whichever is applicable for your location.

4. From the heroku dashboard of your newly created application, click on "Deploy" > "Deployment method" and select GitHub.

5. Confirm the linking of the heroku app to the correct GitHub repository.
   
6. You will need to setup a Postgres database to use in deployment:
   
   1. Click on your app on your heroku dashboard and follow resources > find more add-ons > Heroku Postgres.
   2. Follow Heroku Postgres > Install Heroku Postgres > Select your app from "app to be provisioned" > Provision add-on. A Heroku Postgres database has now been created for you.
   
7. In the heroku dashboard for the application, click on         "Settings" > "Reveal Config Vars".

9.  Set the following config vars:

    | Key | Value |
    --- | ---
    AWS_ACCESS_KEY_ID | `<enter here>`
    AWS_SECRET_ACCESS_KEY | `<enter here>`
    AWS_STORAGE_BUCKET_NAME | `<enter here>`
    DATABASE_URL | `<your postgress url here>`
    SECRET_KEY | `<enter here>`
    STRIPE_PUBLISHABLE | `<enter here>`
    STRIPE_SECRET | `<enter here>`
    EMAIL_HOST_ADDRESS | `<enter here>`
    EMAIL_HOST_PASSWORD | `<enter here>`
    DISABLE_COLLECTSTATIC | '1'

10. From the command line of your local IDE:
    - set up heroku remote: 
        - `heroku git:remote -a <app name>` 
    - Migrate the database models: 
        - `heroku run python manage.py migrate`
    - Open heroku bash terminal:
      - `heroku run bash` 
    - Create your superuser account in your new database:
      - `python manage.py createsuperuser`
    - Exit heroku bash terminal:
      - `exit`

11. Once the build is complete, click the "View app" button provided on heroku.

# Credits

- Youtube tutorials that helped throughout the project:
    - [Python Django Tutorial by Corey Schafer](https://www.youtube.com/watch?v=UmljXZIypDc&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p)


## Disclaimer
The content of this website is educational purposes only.