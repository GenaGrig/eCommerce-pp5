Desktop | Mobile |
--- | --- |
![Desktop Home Page image](/media/screenshots/desktop/main-page-desktop.png) | ![Mobile Home Page image ](/media/screenshots/mobile/main-page-mobile.jpg) |


# Genstar Music Store

Genstar Music Store (later in a document just GMS for better use) is a musical instrument store, where customers can but different musical instruments from most famous brands online. There is also a big variety of other tools for producers, sound engineers and stage technicians for recording, live performances and lighting on stage or other places. 

GMS allows customers to buy instruments online and get them delivered by 3-5 days. Customers can buy anonimously or with created account. Creating account gives customers preferences, such as wishlist, saving data for future purchases and my profile page with orders history.  

You can visit the deployed website here - [Genstar Music Store](https://genstar-music-store-3a732f4aac46.herokuapp.com/products/).

GitHub repository you can find here - [GitHub repo](https://github.com/GenaGrig/eCommerce-pp5.git).

## Table of contents

1. [User Experience (UX)](#user-experience-ux)
    1. [Strategy](#strategy)
        1. [Project Goals](#project-goals)
        2. [User Stories](#user-stories)
        3. [Strategy Table](#strategy-table)
    2. [Scope](#scope)
    3. [Structure](#structure)
    4. [Surface](#surface)
2. [Features](#features)
    1. [Main features](#main-features)
    2. [Products Page](#products-page)
    3. [Product Details Page](#product-details-page)
    4. [Menu](#menu)
    5. [Categories Page](#categories-page)
    6. [Shopping Cart Page](#shopping-cart-page)
    7. [Checkout Page](#checkout-page)
    8. [Profile Pages](#profile-pages)
    9. [Update Profile Page](#update-profile-page)
    10. [Wishlist](#wishlist)
    11. [Product Management Page](#product-management-page)
    12. [Authentication Pages](#authentication-pages)
    13. [Terms of Use and Privacy Policy Pages](#terms-of-use-and-privacy-policy-pages)
3. [Technologies Used](#technologies-used)
    1. [Languages Used](#languages-used)
    2. [Libraries and Frameworks](#languages-and-frameworks)
    3. [Packages / Dependencies Installed](#packages--dependencies-installed)
    4. [Database Management](#database-management)
    5. [Tools and Programs](#tools-and-programs)
4. [Testing](#testing)
    1. [Go to TESTING.md](https://github.com/GenaGrig/eCommerce-pp5/blob/main/TESTING.md)
5. [Deployment](#deployment)
6. [Credits](#credits)
7. [Known Bugs](#known-bugs)
8. [Acknowledgements](#acknowledgements)

***

# User Experience (UX)

### Strategy

#### Project goals

* Website uses modern techniques and frameworks to be attractive to user
* Color palette and contrast is used in such way that site elements do not stick out or disappear behind
* Responsive design makes the website accessible on different devices and screen sizes
* Navigation panel is easy to use and navigate, names and categories are descriptive
* Structure of website is easy to understand and navigate
* Site users are able to register an account to use extra services
* Site users are able to login to their accounts to use extra services
* Site users are able to logout from their accounts to secure their private information and order details
* Site admins can add, edit or delete products both from admin panel or via user interface on product management page
* Site users are able to edit their profiles after creating account and save personal info if they wish
* Site users can leave ratings to products they purchase (login required)
* Site users has their own wishlist to save products they want to buy (login required)
* Site users has their own profile page with pesonal information, wishlist and orders history (login required)
* Website uses pop-up messages that follows actions made by the users

#### User Stories

* As a Shopper I can view list of products so that I can select some to purchase
* As a Shopper I can view individual product details so that I can identify the price, description, product rating, product image
* As a Shopper I can identify deals, special offers and discounts so that I can take advantage of special sales for purchasing
* As a Shopper I can easily view the total of my purchases at any time so that I will not spend too much or add more items to my cart to reach my budget
* As a Site User I can easily register and account so that have a personal account to view my profile and have access to extra features
* As a Site User I can login or logout to/from site so that I can access my personal account information
* As a Site User I can recover my password in case I forget it so that I can recover access to my account
* As a Site User I can receive confirmation email after new account registering so that I can verify that my account registration was successful
* As a Site User I can have personalized user profile so that I can view my order history, order confirmations and save my payment and shipping information
* As a Shopper I can sort the list of all available products so that I can identify the best rated, best priced and categorically sorted products
* As a Shopper I can sort specific category of product so that I can find best-rated, best-priced product in specific category, or sort the products by name in specific category
* As a Shopper I can sort multiple categories of products simultaneously so that I can find the best-priced or best-rated products across broad categories
* As a Shopper I can search for a product by name or description so that I can find a specific product I would like to purchase
* As a Shopper I can easily see what I've searched for and the number of results so that I can quickly decide whether the product I want is available
* As a Shopper I can select quantity of a product when purchasing it so that I can ensure I do not accidentally select the wrong product quantity
* As a Shopper I can view items in my basket to be purchased so that I can identify the total cost of my purchase and all items I will receive
* As a Shopper I can adjust the quantity of individual items in my bag so that I can easily make changes to my purchase before checkout
* As a Shopper I can easily enter my payment information so that check out quickly and with no difficulties
* As a Shopper I can feel my personal and payment information is safe and secure so that I can confidently provide the needed information to make a purchase
* As a Shopper I can view an order confirmation after checkout so that I can verify that I have not made any mistakes when purchased products
* As a Shopper I can receive an order confirmation email after checking out so that I can keep the confirmation of what I've purchased for my records and order following
* As a Store Owner I can add a product so that I can add new items to store
* As a Store Owner I can edit/update a product so that I can change product prices, descriptions, images and other product criteria
* As a Store Owner I can delete a product so that I can remove items that are no longer for sale/out of stock
* As a Site User I can add my personal profile image so that I can click it instead and open my profile menu
* As a Site User I can sign in using social networks so that I can have multiple choices for signing in from different platforms
* As a Shopper I can see real number of desired product in stock so that I am sure my product is available and I can order it right now

At the start of the project user stories looked like this:

![Screenshot of user stories at the start on GitHub](/media/screenshots/desktop/user-stories-project-start.png)

### Week 1
![Screenshot of user stories at the start on GitHub](/media/screenshots/desktop/user-stories-week-1.png)

### Week 2
![Screenshot of user stories at the start on GitHub](/media/screenshots/desktop/user-stories-week-2.png)

### Week 3
![Screenshot of user stories at the start on GitHub](/media/screenshots/desktop/user-stories-week-3.png)

### Week 4
![Screenshot of user stories at the start on GitHub](/media/screenshots/desktop/user-stories-week-4.png)

### Finals
![Screenshot of user stories at the start on GitHub](/media/screenshots/desktop/user-stories-week-finals.png)

### Extra features - undone
![Screenshot of user stories at the start on GitHub](/media/screenshots/desktop/user-stories-undone-future.png)

#### Strategy Table

Opportunity / Problem | Importance | Viability / Feasibility
--- | --- | ---
Responsive design | 5 | 5
Account registration | 5 | 5
Social media signup | 1 | 0
Profile page | 5 | 5
Profile image | 1 | 0
Wishlist | 4 | 4
Add, edit and delete products| 5 | 5
Ability to search/filter for products | 4 | 3
Special offers | 3 | 2
Order payment and confirmation | 5 | 5
**Total** | **38** | **34**

### Scope

Based on strategy table, not all the features will be implemented in the first deployment of the project and some of the features will not be implemented at all, because of their difficulties or its necessity at this stage. The main goal was to make a MVP (minimum viable product), so the user can have fully functional web site and make all the necessary manipulations mentioned in user stories.

#### Features that will not be implemented at this stage
* Social media signup
* Profile image
* Special offers and discounts
* Coupons

### Skeleton

#### Wireframes

[Balsamiq](https://balsamiq.com/) has been used to showcase the appearance of the site and display the placement of the different elements whitin the pages.

Page | Desktop Version | Mobile Version
--- | --- | ---
Home page | ![Desktop home page image](/media/wireframes/home-page-desktop.png) | ![Mobile home page image](/media/wireframes/home-page-mobile.png)
Membership | ![Desktop membership wireframe image](/media/wireframes/membership-page-desktop.png) | ![Mobile membership wireframe image](/media/wireframes/membership-page-mobile.png)
Workouts | ![Desktop workouts wireframe image](/media/wireframes/workouts-page-desktop.png) | ![Mobile workouts wireframe image](/media/wireframes/workouts-page-mobile.png)
PT | ![Desktop personal trainer wireframe image](/media/wireframes/pt-page-desktop.png) | ![Mobile personal trainer wireframe image](/media/wireframes/pt-page-mobile.png)
Contact Us | ![Desktop contact page wireframe image](/media/wireframes/contact-page-desktop.png) | ![Mobile contact page wireframe image](/media/wireframes/contact-page-mobile.png)
Login page | ![Desktop login wireframe image](/media/wireframes/login-page-desktop.png) | ![Mobile login wireframe image](/media/wireframes/login-page-mobile.png)
Register page | ![Desktop register new user wireframe image](/media/wireframes/register-page-desktop.png) | ![Mobile register new user wireframe image](/media/wireframes/register-page-mobile.png)
User profile / User signed in | ![Desktop user profile wireframe image](/media/wireframes/user-panel-desktop.png) | ![Mobile user profile wireframe image](/media/wireframes/user-panel-mobile.png)
Staff page / Admin or staff members signed in | ![Desktop staff panel wireframe image](/media/wireframes/staff-panel-desktop.png) | ![Mobile staff panel wireframe image](/media/wireframes/staff-panel-mobile.png)
Booking page / User signed in | ![Desktop booking wireframe image](/media/wireframes/book-workout-desktop.png) | ![Mobile booking wireframe image](/media/wireframes/book-workout-mobile.png)
Booking submit / User signed in | ![Desktop booking submit wireframe image](/media/wireframes/booking-submit-desktop.png) | ![Mobile booking submit wireframe image](/media/wireframes/booking-submit-mobile.png)
Logout page / User signed in | ![Desktop logout wireframe image](/media/wireframes/logout-desktop.png) | ![Mobile logout wireframe image](/media/wireframes/logout-mobile.png)

### Structure

![Structure of the Genstar Fitness website](/media/screenshots/desktop/genstar-fitness-structure.png)

### Surface

#### Color palette

Color scheme of blue(#0126fa) for navigation bar background, light blue(#47a9ff) for footer and some container page elements background and white(#ffffff) for text color on a blue or light blue background. These colors are used throughout the website and create together mild color palette for user eyes to make the UI and UX smoother.

![Screenshot of color palette for website](/media/screenshots/desktop/color-palette.PNG)

#### Fonts

No extra fonts we used on this website. All fonts are default by Bootstrap. There is no difficulties to read the text written used by this fonts.

[Back to top ⇧](#genstar-music-store)

# Features

### Main features

The website is made using the responsive design in mind, as not only desktop PC or laptop users will be visiting it. Website runs smoothly on tablets and phones as well and supports different screen sizes.

The website is done as a classical e-commerce store with products on main page and all neccessary information on each product card. Below I will go through main website elements in details.

#### Header with not authenticated user

![Screenshot of header with user not autheticated](/media/screenshots/desktop/header-not-auth-desktop.png)

Header with no authenticated user consist of three main parts:

* Logo, clickable, that returns customer to main page
* Search bar, where customer can search products or categories
* Two icons/buttons - My Account with Login and Register buttons in dropdown menu; and Cart button which show sum of products already in cart, quantity of products in cart and if clicked move customer to current cart.

#### Header when user is authenticated

![Screenshot of header with user not autheticated](/media/screenshots/desktop/header-user-auth-desktop.png)

Header when user is authenticated differs, consist of three main parts, but has more elements:

* Logo, clickable, that returns customer to main page
* Search bar, where customer can search products or categories
* Three icons/buttons: 
    - My Account with dropdown, where if user is administrator, store owner or staff member there is a Product Management button, for adding, editing or deleting product. Otherwise there is just a My Profile and Logout buttons.
    - Wishlist button that leads customer to its wishlist.
    - Cart button which show sum of products already in cart, quantity of products in cart and if clicked move customer to current cart.

#### Navigation bar

Navigation bar is presented as a categories list in closed state and with mouse over it opens with sub-categories for each parent category.

* Main navigation bar in closed state

![Screenshot of main navigation bar which is closed](/media/screenshots/desktop/navigation-panel-closed-desktop.png)

* Main navigation bar in opened state

![Screenshot of main navigation bar which is open](/media/screenshots/desktop/navigation-panel-open-desktop.png)

Navigation bar does not change if the user is logged in or logged out, it contains only information about products.

#### Footer

![Screenshot of footer in desktop view](/media/screenshots/desktop/footer-desktop.png)

Footer has three main areas:
- area with grey background where Subscription form to newsletters is located on the left and social media buttons on the right
- main area with logo and different links grouped by categories. Right now not all links are clickable, because it is not suitable for MVP and will take a huge amount of extra time to fix all links working and filled with respektive information. Down on the right customer can find language selector and back to top button. Language selector is a future feature to be implemented if the website will become international.

#### Toasts and other helpful messages

Toasts working as flash messages that supports most of users actions and are quite flexible for containing different information and display success, warning or error messages.

* Simple success toast to show customer successful sign in. 

![Screenshot of flash message after sign in](/media/screenshots/desktop/success-toast-login-desktop.png)

* In this toast I added buttons for customer to view its cart to edit it or go directly to chechout.

![Screenshot of flash message after adding product in cart](/media/screenshots/desktop/success-toast-add-to-cart-desktop.png)

### Mobile menu

Each menu category has is a dropdown, containing sub-categories related to its parent category.

Menu without authentication | Menu with authentication |
--- | --- |
![Screenshot of Menu without authentication](/media/screenshots/mobile/mobile-menu-not-auth.jpg) | ![Screenshot of Menu with authentication ](/media/screenshots/mobile/mobile-menu-user-auth.jpg) |


[Back to top ⇧](#genstar-music-store)

### Home page
Desktop | Mobile |
--- | --- |
![Desktop Home Page image](/media/screenshots/desktop/main-page-desktop.png) | ![Mobile Home Page image ](/media/screenshots/mobile/main-page-mobile-res.jpg) |

Main page has one major element that is carousel that contains three slides with photos and captions with informative text on them to give to users some basic information about fitness club. It does not scroll automatically, only when user scrolls for the first time, slides start to scroll. However, when the mouse is over the slide, automatic scroll stops. 

### Membership page
Desktop | Mobile |
--- | --- |
![Desktop Membership Page image](/media/screenshots/desktop/membership-page-desktop.png) | ![Mobile Membership Page image ](/media/screenshots/mobile/membership-page-mobile-res.jpg) |

Membership page has information about different membership types and which preferences each type gives. There are three types of membership, such as Standard, Student and All Inclusive, each with its own benefits. The button "Buy membership" should link to checkout page, but for now it redirects to Contact Us page, as payment module is not necessary in this project and hard to implement. 
* As a future option, membership role will affect booking opportunities, as some membership roles contains exclusive offers
* As a future change, workouts can book only fitness club members (now it can do everyone, who has an active account) or those who have free pass or onetime payment

### Workouts page
Desktop | Mobile |
--- | --- |
![Desktop Workouts Page image](/media/screenshots/desktop/workouts-page-desktop.png) | ![Mobile Workouts Page image ](/media/screenshots/mobile/workouts-page-mobile-res.jpg) |

Workouts page contains all available at the moment workouts that can be booked after user is logged in. The main section is made with a Bootstrap component called 'Accordion'. Each workout in accordion list opens one at a time, closing the previously opened to save space on different screen sizes, especially phones and skip extra scrolling. As a future option, a small book active workout button can be added below each workout description.  

### PT page
Desktop | Mobile |
--- | --- |
![Desktop Personal Trainer Page image](/media/screenshots/desktop/personal-trainer-page-desktop.png) | ![Mobile Personal Trainer Page image ](/media/screenshots/mobile/personal-trainer-page-mobile-res.jpg) |

Personal trainers' page has general information about who are personal trainers and with what questions they can help with. Page contains a contact form for the questions regarding personal training, where user can choose a category that suits to users question or leave it as general question. Right now submitting the personal trainers contact form leads to return of dump form page from Code Institute, to confirm that everything was done correctly and data was submitted to back-end. As a future feature, sending emails with submission of this form will be implemented.

### Contact page
Desktop | Mobile |
--- | --- |
![Desktop Contact Page image](/media/screenshots/desktop/contact-page-desktop.PNG) | ![Mobile Contact Page image ](/media/screenshots/mobile/contact-page-mobile-res.jpg) |

Contact page contains two general elements, Google map and contact form. It contains also a general contact information, but as it duplicates with footer, it is made just for good-looking symmetry. 

Google maps API is responsive and change its size according to screen size. Two containers with contact information and form are also responsive and all elements on a page has a column structure on small screen sizes. 

Right now submitting the contact form leads to return of dump form page from Code Institute, to confirm that everything was done correctly and data was submitted to back-end. As a future feature, sending emails with submission of this form will be implemented.

### Terms of Use pages

This section is necessary, because fitness club needs to protect its rights on a website and information its contains. The first document 'Terms and Conditions' contains general rules and regulations for the use of Genstar Fitness's website. By accessing the website user accepts terms and conditions automatically, otherwise user needs to leave website.

Privacy Policy/GDPR is a document that secures visitors privacy. As the website collects and stores users information, this document provides description of which information is collected and how it is used. 

#### Terms and Conditions
Desktop | Mobile |
--- | --- |
![Desktop Terms and Conditions Page image](/media/screenshots/desktop/terms-and-conditions-desktop.png) | ![Mobile Terms and Conditions Page image ](/media/screenshots/mobile/terms-and-conditions-mobile-res.jpg) |

#### Privacy Policy/GDPR
Desktop | Mobile |
--- | --- |
![Desktop Privacy Policy Page image](/media/screenshots/desktop/private-policy-desktop.png) | ![Mobile Privacy Policy Page image ](/media/screenshots/mobile/privacy-policy-mobile-res.jpg) |

### Profile page
Desktop | Mobile |
--- | --- |
![Desktop User Profile Page image](/media/screenshots/desktop/user-profile-page-desktop.png) | ![Mobile User Profile Page image ](/media/screenshots/mobile/user-profile-new.jpg) |

User profile page consists of two major parts - User Info and My Bookings.
* User Info contains information about user as first and last name, username and email. An Edit Profile button  allows users to change their data. By default first and last name are empty, so user needs to enter them by editing profile. As a future feature, more fields to user profile will be added. 

* My Bookings part allows user to see all reserved bookings and edit or delete them. Here all the CRUD functionality is implemented. User can create a booking, see all bookings made, update bookings and delete them. Edit and delete buttons are shown as icons, because this design is much more comfortable on small screens, such as phones. 

#### Delete Workout Confirmation Modal

Desktop | Mobile |
--- | --- |
![Desktop Delete Booking Confirmation Modal image](/media/screenshots/desktop/confirm-delete-modal-desktop.PNG) | ![Mobile Delete Booking Confirmation Modal image ](/media/screenshots/mobile/delete-booking-confirmation-mobile-res.jpg) |

This is an extended feature for user convenience and to be sure, that user will not delete booking accidentally. The same feature is realized on staff panel for the same reason.

### Update profile page
Desktop | Mobile |
--- | --- |
![Desktop Update Profile Page image](/media/screenshots/desktop/update-profile-form-desktop.PNG) | ![Mobile Update Profile Page image ](/media/screenshots/mobile/update-profile-mobile-res.jpg) |

This page allows user to update profile and change such information as first and last name (empty by default), username and email. As a future feature, change of password and some extra fields can be added.

### Booking pages
Desktop | Mobile |
--- | --- |
![Desktop Booking Page image](/media/screenshots/desktop/booking-page-desktop.PNG) | ![Mobile Booking Page image ](/media/screenshots/mobile/booking-page-mobile-res.jpg) |

On this booking page user selects workout type and date in pop-up calendar. When done, user need to click on continue to proceed to next page or back to return to user profile page. 

Desktop | Mobile |
--- | --- |
![Desktop Booking Time Page image](/media/screenshots/desktop/booking-time-page-desktop.PNG) | ![Mobile Booking Time Page image ](/media/screenshots/mobile/booking-time-select-mobile-res.jpg) |

On this page user need to select time for chosen workout. When done, user clicks on "Book Workout" to confirm and save booking, or "Back" to go back to previous page and change workout or date.

* This booking section has many improvement possibilities that can be added in the future. For example:
    * Schedule for each workout with exact dates and time that repeats every week
    * Make all booking process on a single page to reduce clicking and pages count
    * Add workout booking for non-member of fitness club as a free pass or onetime payment (requires payment system and functionality)

### Staff panel page
Desktop | Mobile |
--- | --- |
![Desktop Staff Panel Page image](/media/screenshots/desktop/staff-panel-page-desktop.png) | ![Mobile Staff Panel Page image ](/media/screenshots/mobile/staff-panel-new.jpg) |

Staff panel is made only for admins and staff members. On this panel, staff members can see all the bookings made by users and filter them by different values. 


### Authentication pages

#### Register New Account

Desktop | Mobile |
--- | --- |
![Desktop Register Account image](/media/screenshots/desktop/register-account-page-desktop.PNG) | ![Mobile Register Account Page image ](/media/screenshots/mobile/register-accont-mobile-res.jpg) |

Register New Account form contains three required fields that should be filled to register new user and save users' information to database. Each field has a little description below, to help the user enter correct information and avoid mistakes. After this procedure, user is available to log in to website at any time. After registration user is redirected to users' profile page directly, without need to sign in. If user already has an account and opened register account page by mistake, there is a direct link to sing in page in header or on navigation bar.

#### Sign In page

Desktop | Mobile |
--- | --- |
![Desktop Sign In Page image](/media/screenshots/desktop/sign-ip-desktop.PNG) | ![Mobile Sign In Page image ](/media/screenshots/mobile/sign-in-page-mobile-res.jpg) |

Sign In page has just to field to be filled as Username and Password, which user entered when registered new account. There is a checkbox "Remember me" to store user information as cookie. Below that, a "Forgot password" link redirects user to a password reset page, where user needs to enter email address and get a link to change password. 

#### Sign Out

Desktop | Mobile |
--- | --- |
![Desktop Sign Out Page image](/media/screenshots/desktop/sign-out-page-desktop.png) | ![Mobile Sign Out Page image ](/media/screenshots/mobile/sign-out-page-mobile-res.jpg) |

Sign Out page is quite simple and contains only one button - "Sign Out". At this stage, action can be reverted and user can go back to other pages without signing out. As a future feature, this page can be changed to modal with the same functionality.

### Future features

Some features where mentioned directly in page description, but let's summarize them in this section:

* Membership. Membership role will affect booking opportunities, as some membership roles contains exclusive offers
* Membership. Only fitness club members can book workouts (now it can do everyone, who has an active account), those who have free pass, or onetime payment (requires payment system on a website)
* Workout. Schedule for each workout with fixed days and times
* Personal Trainer. Possibility to book a personal trainer session both free and for a fixed price
* Personal Trainer and Contact pages contact forms should send messages to user emails
* Update profile should be able to change password. Several field with information should be available to update, such as address, city, country and telephone number
* Booking. All booking process on one page
* Booking. Booking for non-members for free (testing pass) or fixed price
* Register form with more information, such as first and last name and telephone number
* Sign out function as a modal, to skip the separate sign out page. 

[Back to top ⇧](#genstar-fitness)

# Technologies Used

### Languages Used

* [HTML5](https://en.wikipedia.org/wiki/HTML)
* [CSS3](https://en.wikipedia.org/wiki/CSS)
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language))


### Libraries and Frameworks

* [Django](https://www.djangoproject.com/)   
    * Django was used as web framework.
   
* [Bootstrap 5](https://getbootstrap.com/)  
    * Bootstrap 5 was used throughout the website to help with styling and responsiveness.

* [Font Awesome](https://fontawesome.com)  
    * Font Awesome was used throughout the website to add icons for aesthetic and UX purposes. 


### Packages / Dependencies Installed

* [Django Allauth](https://django-allauth.readthedocs.io/en/latest/)  
    * Django Allauth was used for user authentication, registration, and account management.

* [Django Crispy Form](https://django-crispy-forms.readthedocs.io/en/latest/)   
    * Django Crispy Form was used to control the rendering of the forms. 
 
* [Gunicorn](https://gunicorn.org/)  
    * Gunicorn was used as Python WSGI HTTP Server for UNIX to support the deployment of Django application.  

* [Cloudinary](https://cloudinary.com/)
    * Cloudinary has been used as image management solution

### Database Management
* [ElephantSQL](https://www.elephantsql.com/)   
    * ElephantSQL as a Service database was used in production, as a service based on PostgreSQL.


### Tools and Programs

* [Git](https://git-scm.com)  
    * Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub. 

* [GitPod](https://gitpod.io/)
     * GitPod was used for writing code, committing, and then pushing to GitHub.

* [GitHub](https://github.com)  
    * GitHub was used to store the projects code after being pushed from Git. 

* [Heroku](https://www.heroku.com)   
    * Heroku was used to deploy the website.

* [Am I Responsive](ami.responsivedesign.is)  
    * Am I Responsive was used to preview the website across a variety of popular devices.

* [Coolors](https://coolors.co)  
    * Coolors was used to create a color scheme for the website.

* [Chrome DevTools](https://developer.chrome.com/docs/devtools/)
    * Chrome DevTools was used during development process for code review and to test responsiveness.

* [W3C Markup Validator](https://validator.w3.org/)
    * W3C Markup Validator was used to validate the HTML code.

* [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
    * W3C CSS Validator was used to validate the CSS code.

* [JSHint](https://jshint.com/) 
    * The JSHints JavaScript Code Quality Tool was used to validate the site's JavaScript code.

* [Google Maps](https://www.google.com/maps)
    * Google maps API to embed google map with location on a website.

* [Terms and Conditions generator](https://www.termsandconditionsgenerator.com)
    * Terms and Conditions generator was used to create an agreement between website and user for protection of GenStar Fitness website rights

* [Privacy Policy generator](https://www.termsfeed.com/privacy-policy-generator/)
    * Privacy Policy generator was used to create a document describing which information GenStar Fitness website collects and stores and how it secures users privacy

[Back to top ⇧](#genstar-fitness)

# Testing

The testing is available in separate file [TESTING.md](https://github.com/GenaGrig/genstar-fitness/blob/main/TESTING.md)

# Deployment

This project was developed using a [GitPod](https://gitpod.io/) workspace. The code was committed to [Git](https://git-scm.com/) and pushed to [GitHub](https://github.com/") using the terminal.

### Deploying on Heroku
To deploy this page to Heroku from its GitHub repository, the following steps were taken:

1. Create the Heroku App:
    - Select "Create new app" in Heroku.
    - Choose a name for your app and select the location.

2. Attach the Postgres database:
    - Open [ElephantSQL](https://www.elephantsql.com/) website and create free account
    - Click on green button Create New Instance
    - Select Name of the project and plan Tiny Turtle (Free), click on continue
    - Select your region, click on Review
    - Check all information and click on Create instance
    - Click on your instance in the list to open its details
    - Copy database URL in URL field
    - Open your Heroku project
    - Open Settings tab and click on Reveal Config Vars
    - In a field Key add DATABASE_URL
    - In a field VALUE add postgres URL from ElephantSql created instance
    - Click on ADD to finish the process

3. Prepare the environment and settings.py file:
    * In the Settings tab, click on Reveal Config Vars and copy the URL next to DATABASE_URL.
    * In your GitPod workspace, create an env.py file in the main directory. 
    * Add the DATABASE_URL value and your chosen SECRET_KEY value to the env.py file.
    * Add the SECRET_KEY value to the Config Vars in Heroku.
    * Update the settings.py file to import the env file and add the SECRETKEY and DATABASE_URL file paths.
    * Update the Config Vars with the Cloudinary URL, adding into the settings.py file also.
    * In settings.py add the following sections:
        * Cloudinary to the INSTALLED_APPS list
        * STATICFILE_STORAGE
        * STATICFILES_DIRS
        * STATIC_ROOT
        * MEDIA_URL
        * DEFAULT_FILE_STORAGE
        * TEMPLATES_DIR
        * Update DIRS in TEMPLATES with TEMPLATES_DIR
        * Update ALLOWED_HOSTS with ['app_name.heroku.com', 'localhost']

4. Store Static and Media files in Cloudinary and Deploy to Heroku:
    - Create three directories in the main directory: media, static and templates.
    - Create a file named "Procfile" in the main directory and add the following:
        - web: gunicorn project-name.wsgi
    - Go to Deploy tab on Heroku and connect to the GitHub, then to the required repository.
    Click on Deploy Branch and wait for the build to load. When the build is complete, the app can be opened through Heroku.

### Forking the Repository
By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log into [GitHub](https://github.com/login) or [create an account](https://github.com/join).
2. Locate the [GitHub Repository](https://github.com/GenaGrig/genstar-fitness.git).
3. At the top of the repository, on the right side of the page, select "Fork"
4. You should now have a copy of the original repository in your GitHub account.

### Creating a Clone
How to run this project locally:
1. Install the [GitPod Browser](https://www.gitpod.io/docs/browser-extension/ "Link to Gitpod Browser extension download") Extension for Chrome.
2. After installation, restart the browser.
3. Log into [GitHub](https://github.com/login "Link to GitHub login page") or [create an account](https://github.com/join "Link to GitHub create account page").
2. Locate the [GitHub Repository](https://github.com/GenaGrig/genstar-fitness.git).
5. Click the green "GitPod" button in the top right corner of the repository.
This will trigger a new GitPod workspace to be created from the code in GitHub where you can work locally.

How to run this project within a local IDE, such as VSCode:

1. Log into [GitHub](https://github.com/login) or [create an account](https://github.com/join).
2. Locate the [GitHub Repository](https://github.com/GenaGrig/genstar-fitness.git).
3. Under the repository name, click "Clone or download".
4. In the Clone with HTTPs section, copy the clone URL for the repository.
5. In your local IDE, open the terminal.
6. Change the current working directory to the location where you want the cloned directory to be made.
7. Type 'git clone', and then paste the URL you copied in Step 3.
```
git clone https://github.com/GenaGrig/genstar-fitness.git
```
8. Press Enter. Your local clone will be created.

Further reading and troubleshooting on cloning a repository from GitHub [here](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository)

[Back to top ⇧](#genstar-fitness)

# Credits

This resources were used as a help to create [GenStar Fitness](https://genstar-fitness-and-gym-0d51dc3aa6d0.herokuapp.com/) website:

### Content
* Website content was written by the developer
* README file was written with help of following documents:
    * Code Institute [README template](https://github.com/Code-Institute-Solutions/readme-template)
    * GitHubs [Basic writing and formatting syntax](https://docs.github.com/ru/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#headings)
    * Hints and some structure of README files from existing projects from other CI students
    * [josswe26 code-buddy project readme](https://github.com/josswe26/code-buddy.git) as a perfect example how readme file should look like. Some parts were taken from this Readme file.

### Media

* [New register user form tutorial](https://www.youtube.com/watch?v=JeTGxvFnAaU&list=TLPQMDYwODIwMjOuesC_k1wr0A&index=1)
* [Update user profile tutorial](https://www.youtube.com/watch?v=F5kTZdi_c5k)
* [Fix problem with updating user profile, username already exists](https://www.appsloveworld.com/django/100/94/django-user-account-update-ignore-user-with-this-username-already-exists)
* [Booking system tutorial](https://blog.devgenius.io/django-tutorial-on-how-to-create-a-booking-system-for-a-health-clinic-9b1920fc2b78)
* [Booking system tutorial video guide](https://youtu.be/s5xbtuo9pR0?si=x7hmhprUzVnpzoAJ)
* [404 image was taken here](https://pxhere.com/ru/photo/1380359)

### Code

* [Code Institutes' Slack channel](www.slack.com) was used to get help from its students in resolving code problems and questions
* [Bootstrap 5](https://getbootstrap.com/) website was used very often to fix the problems with different elements and get responsive design work
* Some of code functions was written with help of [GitHub Copilot](https://github.com/features/copilot)

[Back to top ⇧](#genstar-fitness)

# Known Bugs

* Booking of workouts is available to everyone who has registered account; membership role does not work and affect booking opportunities for now
* Both contact forms at PT and Contact pages does not work and do not send emails. All the tries to get it work failed. Developer does not have necessary skills to fix it right now, but promise to fix it in the future, after getting skills to fix this bug.

# Acknowledgements

* I want to thank my mentor Marcel Mulders for very good feedback and very useful advices that made my project complete and interesting. Very good ideas from my mentor that was implemented and made project look more solid.
* I want to thank members in our Code Institute Slack community for giving feedback and showing their own projects that was inspiring in different ways.

[Back to top ⇧](#genstar-fitness)