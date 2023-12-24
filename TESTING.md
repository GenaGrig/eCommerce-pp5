# GenStar Music Store Testing

[Back to the README.md file](https://github.com/GenaGrig/eCommerce-pp5/blob/main/README.md)  

[View the live website here](https://genstar-music-store-3a732f4aac46.herokuapp.com/products/)  

## Table of Contents

1. [Testing User Stories](#testing-user-stories)
2. [Code Validation](#code-validation)
3. [Accessibility](#accessibility)
4. [Tools Testing](#tools-testing)
5. [Manual Testing](#manual-testing)

# Testing User Stories

### As a Shopper, I can view list of products so that I can select some to purchase
* When customer opens website, list of products is first what is displayed. No pagination is implemented and all the products are shown on the first page. As a future feature, pagination can be implemented or an option list with products quantity on a page, with 24, 48 or all products on a page. 
### As a Shopper, I can view individual product details so that I can identify the price, description, product rating and product image
* Each product on a page is clickable and has an individual product details page with all the necessary information about the product, as name, price, quantity in stock and short and full description. Customer can set a rating for a product, add product to wishlist or cart. 
### As a Shopper, I can identify deals, special offers and discounts so that I can take advantage of special sales for purchasing
* This option is not implemented on this deployment, but will be done in one of the future versions.
### As a Shopper, I can easily view the total of my purchases at any time so that I will not spend too much or add more items to my cart to reach my budget
* For the convenience of the customer, total of purchases is shown at the top right of that page on all pages. When the cart is empty, 0.00 euro is displayed. With every new product added to cart, this sum changes and a small red circle near the total price shows how much products are in the cart. Session is saved and will be continued next time if customer closes website. 
### As a Site User, I can easily register and account so that have a personal account to view my profile and have access to extra features
* All the registration functionality is implemented on website with help of Django Auth and customers can register an account. Personal account gives access to profile pages with order history and ability to add products to wishlist.
### As a Site User, I can login or logout to/from site so that I can access my personal account information
* Customers can login and logout from website and have ability to save personal information for future purchases.
### As a Site User, I can recover my password in case I forget it so that I can recover access to my account
* This feature is a part of Django Auth and is implemented on a website. In case customer forgets the password, it can be restored from the login page.(At the moment, email sending functions are disabled, due to SMTP error on Gmail side. Solution should be found.)
### As a Site User, I can receive confirmation email after new account registering so that I can verify that my account registration was successful
* This feature was implemented in first deployments of website and confirmation email was successfully shown in workspace console. With the deployment to Heroku, confirmation email was successfully shown in Heroku logs, but when trying to send real email from Gmail postbox to customer postbox it failed, with the SmtpSenderRefused error. Solution was not found, but it will be done in future. 
### As a Site User, I can have personalized user profile so that I can view my order history, order confirmations and save my payment and shipping information
* This is implemented on a website. When customer has created account on a website, access to My Profile pages is granted. Customer has access to orders history, can click on the last order number and see all the order information. Personal information can be saved on a website and used for future purchases. 
### As a Shopper, I can sort the list of all available products so that I can identify the best-rated, best priced and categorically sorted products
* Sorting option is implemented on a main products page and on category pages. Customer can sort products by different options in both ascending and descending order.
### As a Shopper, I can sort specific category of product so that I can find best-rated, best-priced product in specific category, or sort the products by name in specific category
* Sort option in categories is implemented and customer can sort products in categories with the same options as on the main products page. 
### As a Shopper, I can sort multiple categories of products simultaneously so that I can find the best-priced or best-rated products across broad categories
* This feature is partly implemented and more work on its development will be done to assign several categories to a product. Sorting in categories is implemented, sorting in multiple categories is implemented partly, as products belong to several categories by default. Customer can get access to multiple categories sorting with the help of breadcrumbs that show all the categories product is related to.
### As a Shopper, I can search for a product by name or description so that I can find a specific product I would like to purchase
* Searching feature is implemented and search bar is located in the top of the every page, so customer can search products from every page. 
### As a Shopper, I can easily see what I have searched for and the number of results so that I can quickly decide whether the product I want is available
* After search query, customer will see the search results page, with all the relevant products and a number of products found by the search word in product names or descriptions. 
### As a Shopper, I can select quantity of a product when purchasing it so that I can ensure I do not accidentally select the wrong product quantity
* This option is implemented on a product details page and in the shopping cart. Therefore, if customer has one quantity selected when added to shopping cart from product details page, it could be changed in the shopping cart by selecting new quantity and clicking Update Cart button.
### As a Shopper, I can view items in my shopping cart to be purchased so that I can identify the total cost of my purchase and all items I will receive
* Shopping cart page is very informative and contains all the necessary information about products. Customer can see the list of products with the small product image, name, category, quantity of product (with ability to change it in shopping cart), price of products and a button to remove product from cart if customer will not buy it. On the right side of the page information about price, tax, delivery cost and grand total is displayed.
### As a Shopper, I can adjust the quantity of individual items in my shopping cart so that I can easily make changes to my purchase before checkout
* In shopping cart, quantity of products can be changed for each product. Customer can enter new product quantity by clicking plus or minus buttons and click the Update Cart button.
### As a Shopper, I can easily enter my payment information so that check out quickly and with no difficulties
* Checkout page is made for best user experience and contains many tips for customer information input fields. In case of error or empty required fields, error will be displayed and customer will be redirected to checkout page again. In case of wrong credit card information, error will be displayed to customer. 
### As a Shopper, I can feel my personal and payment information is safe and secure so that I can confidently provide the needed information to make a purchase
* All the information provided is saved in database and is not accessible for other customers, only for admins or staff members that has access to it. No credit card information is saved on a website or database, so the purchase is going on safe and secure via Stripe. Only information about customer credentials and shipping info can be saved on a website and customer has an option for not saving it by unchecking "Save this address" box. 
### As a Shopper, I can view an order confirmation after checkout so that I can verify that I have not made any mistakes when purchased products
* After successful payment, order confirmation page is displayed to user, with all the details of purchase - list of products, personal information, shipping info and all the prices and totals. The most important, order id is shown on this page as a reference for customer and customer support in case something goes wrong with the delivery. 
### As a Shopper, I can receive an order confirmation email after checking out so that I can keep the confirmation of what I have purchased for my records and order following
* This feature was implemented in first deployments of website and order confirmation email was successfully shown in workspace console. With the deployment to Heroku, order confirmation email was successfully shown in Heroku logs, but when trying to send real email from Gmail postbox to customer postbox it failed, with the SmtpSenderRefused error. Solution was not found, but it will be done in future. 
### As a Store Owner, I can add new products, so that new added products will be displayed on a products page
* Add new product are implemented in both front and back-end. All personal who has specific access, can add new products from admin panel or directly from website, by choosing product management link in My Account dropdown menu. It is easier to do from admin panel, as there are Summernote editor implemented for easier description entering (with HTML tags and other formatting options).
### As a Store Owner, I can edit/update a product so that I can change product prices, descriptions, images and other product criteria
* Edit/Update products option is implemented both in admin panel and on website. To quickly edit product from the website, there is an Edit Product button on each product details page. By clicking on it, staff member will be redirected to product management page with all product information already filled in. Updating the necessary information and clicking Edit Product button, will update product information.
### As a Store Owner, I can delete a product so that I can remove items that are no longer for sale/out of stock
* Store owner/staff members can delete products from admin panel or from the product details page clicking the Delete Product page. I mentioned that as future feature confirmation modal would be implemented for security reasons, so the product cannot be deleted accidentally. 
### As a Site User, I can add my personal profile image so that I can click it instead and open my profile menu
* This option was not implemented at this deployment version as it is not viable right now and does not need in MVP (minimum viable product). It was mentioned in future features, can be done and implemented in future deployments of project.
### As a Site User, I can sign in using social networks so that I can have multiple choices for signing in from different platforms
* This option was not implemented at this deployment version because of lack of knowledge and time. This feature increases user experience and allows login to site with existing social media account. It was mentioned in future features, will be done and implemented in future deployments of project.
### As a Shopper, I can see real number of desired product in stock so that I am sure my product is available and I can order it right now
* This feature is a part of Product model and show real product quantities in stock. When other customers buy some products, its quantity in stock changes after updating the page, so other customers will see actual product stock quantities or that the product they desire is out of stock. 

[Back to top ⇧](#genstar-music-store-testing)

# Code Validation

### HTML

[The W3C Markup Validator](https://validator.w3.org) was used to check HTML side of a webpage. Following errors were found:


* Index page errors

![HTML Validator index page check errors](/media/screenshots/testing/html-index-check-errors.PNG)

* Index page errors fixed
    * Errors were fixed by changing failed tags to correct and deleting failed attribute

![HTML Validator index page check fixed](/media/screenshots/testing/html-index-check-fixed.PNG)

* Contact page errors

![Contact page errors](/media/screenshots/testing/html-contact-check-errors.PNG)

* Contact page errors fixed
    * Error was fixed by deleting wrong attribute

![Contact page errors fixed](/media/screenshots/testing/html-contact-check-fix.PNG)

#### All other pages were error free. Some pages html validator was unable to check, giving following error:

![Checking page error 500](/media/screenshots/testing/checking-page-error-500.PNG)

### CSS

For check of CSS in a project [The W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) was used.

There are four CSS files in my project, main is style.css, containing all general styling for the project and overriding most of Bootstrap default CSS. Booking.css, membership.css and workout.css were made to override default Bootstrap CSS in specific files, as there were problem with CSS override when adding to main style.css file. No attempts to join all CSS files in one were successful, as design broke and only discard of changes helped to restore it. 

There are no repetitions, comment out or double code across all css files.

Each file was checked manually in [The W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) and no errors were found.

![No errors in CSS files](/media/screenshots/testing/css-check.PNG)

### Python

Pylint was used continuously during the development process to analyze the Python code for programming errors.

[CI Python Linter](https://pep8ci.herokuapp.com) was used to validate the Python code to validate the Python code for PEP8 requirements. Results are in a table below:


| Location | Errors / Warnings | Code Reviewed |
| --- | --- | --- |
| ./fitness/admin.py | No errors / warnings |![admin.py code reviewed image](/media/screenshots/testing/fitness-admin-py-clean.PNG) |
| ./fitness/apps.py | No errors / warnings |![apps.py code reviewed image](/media/screenshots/testing/fitness-apps-py-clean.PNG) |
| ./fitness/forms.py | ![forms.py errors/warnings image](/media/screenshots/testing/fitness-forms-py-errors.PNG) | ![forms.py code reviewed image](/media/screenshots/testing/booking-forms-py-clear.PNG) |
| ./fitness/models.py | ![models.py errors/warnings image](/media/screenshots/testing/fitness-models-py-errors.PNG) | ![models.py code reviewed image](/media/screenshots/testing/fitness-models-py-clean.PNG) |
| ./fitness/urls.py | No errors / warnings | ![urls.py code reviewed image](/media/screenshots/testing/fitness-urls-py-clean.PNG) |
| ./fitness/views.py | ![views.py errors/warnings image](/media/screenshots/testing/fitness-views-py-errors.PNG) | ![views.py code reviewed image](/media/screenshots/testing/fitness-views-py-clean.PNG) |
| ./booking/admin.py | No errors / warnings |![admin.py code reviewed image](/media/screenshots/testing/booking-admin-py-clear.PNG) |
| ./booking/apps.py | No errors / warnings |![apps.py code reviewed image](/media/screenshots/testing/booking-apps-py-clear.PNG) |
| ./booking/forms.py | ![forms.py errors/warnings image](/media/screenshots/testing/booking-forms-py-errors.PNG) | ![forms.py code reviewed image](/media/screenshots/testing/booking-forms-py-clear.PNG) |
| ./booking/models.py | ![models.py errors/warnings image](/media/screenshots/testing/booking-models-py-errors.PNG) | ![models.py code reviewed image](/media/screenshots/testing/booking-models-py-clear.PNG) |
| ./booking/urls.py | ![urls.py errors/warnings image](/media/screenshots/testing/booking-urls-py-errors.PNG) | ![urls.py code reviewed image](/media/screenshots/testing/booking-urls-py-clear.PNG) |
| ./booking/views.py | ![views.py errors/warnings image](/media/screenshots/testing/booking-views-py-errors.PNG) | ![views.py code reviewed image](/media/screenshots/testing/booking-views-py-clear.PNG) |

### JavaScript

[JSHint, a JavaScript Code Validator](https://jshint.com) was used to check JS code.

No errors were found.

[Back to top ⇧](#genstar-music-store-testing)

# Accessibility

### Lighthouse Reports

Page | Lighthouse Report |
| --- | --- |
| Home | ![Home Page Lighthouse Report](/media/screenshots/testing/lighthouse/index-lighthouse-report.PNG) |
| Membership | ![Membership Page Lighthouse Report](/media/screenshots/testing/lighthouse/membership-lighthouse-report.PNG) |
| Workouts | ![Workouts Page Lighthouse Report](/media/screenshots/testing/lighthouse/workouts-lighthouse-report.PNG) |
| Register | ![Register Page Lighthouse Report](/media/screenshots/testing/lighthouse/register-lighthouse-report.PNG) |
| Login | ![Login Page Lighthouse Report](/media/screenshots/testing/lighthouse/login-lighthouse-report.PNG) |
| Logout | ![Logout Page Lighthouse Report](/media/screenshots/testing/lighthouse/logout-lighthouse-report.PNG) |
| PT !| ![Personal Trainer Page Lighthouse Report](/media/screenshots/testing/lighthouse/personal-trainer-lighthouse-report.PNG) |
| Contact Us | ![Contact Page Lighthouse Report](/media/screenshots/testing/lighthouse/contact-lighthouse-report.PNG) |
| Terms and Conditions | ![Terms and Conditions Page Lighthouse Report](/media/screenshots/testing/lighthouse/terms-and-conditions-lighthouse-report.PNG) |
| Privacy Policy | ![Privacy Policy Page Lighthouse Report](/media/screenshots/testing/lighthouse/privacy-policy-lighthouse-report.PNG) |
| My Profile | ![My Profile Page Lighthouse Report](/media/screenshots/testing/lighthouse/user-profile-lighthouse-report.PNG) |
| Update Profile | ![Update Profile Page Lighthouse Report](/media/screenshots/testing/lighthouse/update-profile-lighthouse-report.PNG) |
| Staff Panel | ![Staff Panel Page Lighthouse Report](/media/screenshots/testing/lighthouse/staff-panel-lighthouse-report.PNG) |
| Book Workout | ![Book Workout Page Lighthouse Report](/media/screenshots/testing/lighthouse/booking1-lighthouse-report.PNG) |
| Book Workout Submit| ![Book Workout Page Lighthouse Report](/media/screenshots/testing/lighthouse/booking2-lighthouse-report.PNG) |

[Back to top ⇧](#genstar-music-store-testing)

# Tools Testing

### [Chrome DevTools](https://developer.chrome.com/docs/devtools/)

Chrome DevTools was used during the development process to test, explore and modify HTML elements and CSS styles used in the project.


### Responsiveness

* Chrome DevTools was used to test responsiveness in different screen sizes during the development process.


## Manual Testing

### Browser Compatibility

Browser | Outcome | Pass/Fail | 
--- | --- | --- |
Google Chrome | No appearance, responsiveness nor functionality issues.| <span style="color:green">Pass</span> |
Opera | No appearance, responsiveness nor functionality issues. | <span style="color:green">Pass</span> |
Mozilla Firefox | No appearance, responsiveness nor functionality issues.| <span style="color:green">Pass</span> |
Microsoft Edge | No appearance, responsiveness nor functionality issues. | <span style="color:green">Pass</span> |


### Device Compatibility

Device | Operative System |Outcome | Pass/Fail
--- | --- | --- | --- |
MSI Katana 15.6" | Windows 11 | No appearance, responsiveness nor functionality issues. | <span style="color:green">Pass</span> |
Asus Rog Strix Desktop 27" | Windows 10 | No appearance, responsiveness nor functionality issues. | <span style="color:green">Pass</span> |
Lenovo Pad | Android | No appearance, responsiveness nor functionality issues. | <span style="color:green">Pass</span> |
Samsung S21 6.2" | Android |No appearance, responsiveness nor functionality issues. | <span style="color:green">Pass</span> |
Nokia S7 Plus 6.0" | Android |No appearance, responsiveness nor functionality issues. | <span style="color:green">Pass</span> |

### Test results

#### General

<table>
    <tr>
        <th colspan=2>Feature</th>
        <th>Users</th>
        <th>Test</th>
        <th>Outcome</th>
        <th>Pass/Fail</th>
    </tr>
    <tr>
        <td rowspan=32>Navigation Bar</td>
        <td rowspan=2>Main logo link</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Clicking the link redirects to the Home page.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td rowspan=2>Home link</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Clicking the link redirects to the Home page.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Membership link</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Clicking the link redirects to the Membership page.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Workouts link</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Clicking the link redirects to the Workouts page.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
     <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>PT link</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Clicking the link redirects to the PT page.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Contact Us link</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Clicking the link redirects to the Contact page.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
        <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Terms of Use dropdown menu</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Clicking the link opens dropdown menu with two links - Terms and Conditions and Privacy Policy.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Terms and Conditions link</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Clicking the link opens Terms and Conditions page.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Privacy Policy</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Clicking the link opens Privacy Policy page.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Register link</td>
        <td rowspan=2>Unregistered</td>
        <td>Functionality</td>
        <td>Clicking the link redirects to the Register page.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Login link</td>
        <td rowspan=2>Unregistered</td>
        <td>Functionality</td>
        <td>Clicking the link redirects to the Sign In page.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Book Workout link</td>
        <td rowspan=2>Registered</td>
        <td>Functionality</td>
        <td>Clicking the link redirects to the Book Workout page.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>User Profile link</td>
        <td rowspan=2>Registered</td>
        <td>Functionality</td>
        <td>Clicking the link redirects to the User Profile page.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Staff panel link</td>
        <td rowspan=2>Admins or stagg members</td>
        <td>Functionality</td>
        <td>Clicking the link redirects to the Staff Panel page.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Logout link</td>
        <td rowspan=2>Registered</td>
        <td>Functionality</td>
        <td>Clicking the link redirects to the Sign Out page.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Hamburger Menu button </td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Clicking the button toggle navigation menu.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Responsive navigation menu on smaller screens.<br>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=10>Footer</td>
        <td rowspan=2>Email link</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Clicking the Email link opens email sending program.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>N/A</td>
        <td><span>N/A</span></td>
    </tr>
    <tr>
        <td rowspan=2>Facebook icon</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Clicking the link open Facebook page on a separate tab.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>N/A</td>
        <td><span>N/A</span></td>
    </tr>
    <tr>
        <td rowspan=2>Instagram icon</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Clicking the link open Instagram page on a separate tab.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>N/A</td>
        <td><span>N/A</span></td>
    </tr>
    <tr>
        <td rowspan=2>Twitter icon</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Clicking the link open Twitter page on a separate tab.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>N/A</td>
        <td><span>N/A</span></td>
    </tr>
</table>

#### Home page

<table>
    <tr>
        <th colspan=2>Feature</th>
        <th>Users</th>
        <th>Test</th>
        <th>Outcome</th>
        <th>Pass/Fail</th>
    </tr>
    <tr>
        <td rowspan=2>Carousel</td>
        <td rowspan=2>Left/Right scroll buttons</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Clicking the Left/Rights scroll button slides images.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
</table>

#### Membership page

<table>
    <tr>
        <th colspan=2>Feature</th>
        <th>Users</th>
        <th>Test</th>
        <th>Outcome</th>
        <th>Pass/Fail</th>
    </tr>
    <tr>
        <td rowspan=2>Membership button</td>
        <td rowspan=2>Buy membership buttons</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Clicking the Buy membership button redirect user to Contact Us page.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Bootstrap button CSS</td>
        <td>Pass</td>
    </tr>
</table>

#### Workouts page

<table>
    <tr>
        <th colspan=2>Feature</th>
        <th>Users</th>
        <th>Test</th>
        <th>Outcome</th>
        <th>Pass/Fail</th>
    </tr>
    <tr>
        <td rowspan=2>Accordion</td>
        <td rowspan=2>Accordion slides</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Clicking each accordion slide should open its content and close previous.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>General styling</td>
        <td>Pass</td>
    </tr>
</table>

#### Personal Trainer page

<table>
    <tr>
        <th colspan=2>Feature</th>
        <th>Users</th>
        <th>Test</th>
        <th>Outcome</th>
        <th>Pass/Fail</th>
    </tr>
    <tr>
        <td rowspan=10>Contact form</td>
        <td rowspan=2>Name input</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Text can be entered in the field.<br>Field is required and validates input.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Focus effect working as expected.</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td rowspan=2>Email input</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Text can be entered in the field.<br>Field is required and validates input text as email.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Focus effect working as expected.</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td rowspan=2>Select subject</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Text can be entered in the field.<br>Field is optional and no subject can be chosen.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td rowspan=2>Message</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Text can be entered in the field.<br>Field is required and validates input.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Focus effect working as expected.</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td rowspan=2>Send button</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Clicking the button submits this form and shows returned form data from CI to confirm that form works and submits data to back-end.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Bootstrap button CSS</td>
        <td>Pass</td>
    </tr>
</table>

#### Contact Us page

<table>
    <tr>
        <th colspan=2>Feature</th>
        <th>Users</th>
        <th>Test</th>
        <th>Outcome</th>
        <th>Pass/Fail</th>
    </tr>
    <tr>
        <td rowspan=2>Google maps API</td>
        <td rowspan=2>Google maps</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Google maps embedded to page and shows map with chosen location.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Responsive design on all screen sizes.</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td rowspan=10>Contact form</td>
        <td rowspan=2>Name input</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Text can be entered in the field.<br>Field is required and validates input.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Focus effect working as expected.</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td rowspan=2>Email input</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Text can be entered in the field.<br>Field is required and validates input text as email.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Focus effect working as expected.</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td rowspan=2>Select subject</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Text can be entered in the field.<br>Field is optional and no subject can be chosen.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td rowspan=2>Message</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Text can be entered in the field.<br>Field is required and validates input.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Focus effect working as expected.</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td rowspan=2>Submit button</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Clicking the button submits this form and shows returned form data from CI to confirm that form works and submits data to back-end</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Bootstrap button CSS</td>
        <td>Pass</td>
    </tr>
</table>

#### Register Page

<table>
    <tr>
        <th colspan=2>Feature</th>
        <th>Users</th>
        <th>Test</th>
        <th>Outcome</th>
        <th>Pass/Fail</th>
    </tr>
    <tr>
        <td rowspan=10>Register New Account</td>
        <td rowspan=2>Username input</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Text can be entered in the field.<br>Field validates input to be present.<br>Display message if the username already exists.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Focus effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>E-mail input</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Text can be entered in the field.<br>Field validates input to be present.<br>Validate input is an email address.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Focus effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Password input</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Text can be entered in the field.<br>Field validates input to be present.<br>Validate input is a valid password.<br>Display message if password is not valid.<br>Display message if both passwords are not equal.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Focus effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Password Repeat input</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Text can be entered in the field.<br>Field validates input to be present.<br>Validate input is a valid password<br>Display message if password is not valid<br>Display message if both passwords are not equal</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Focus effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Sign Up button</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Clicking the button submit the form and redirects to the User Profile page.<br>Create user if form is valid.<br>Display message if user is successfully created.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
</table>


#### Login Page

<table>
    <tr>
        <th colspan=2>Feature</th>
        <th>Users</th>
        <th>Test</th>
        <th>Outcome</th>
        <th>Pass/Fail</th>
    </tr>
    <tr>
        <td rowspan=6>Sign In Form</td>
        <td rowspan=2>Username input</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
         <td>Text can be entered in the field.<br>Field validates input to be present.<br>Display message if the user name and/or password are not correct.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Focus effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Password input</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Text can be entered in the field.<br>Field validates input to be present.<br>Display message if the user name and/or password are not correct.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Focus effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Sign In button</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Clicking the button authenticates the user and redirect to the User Profile page.<br>Display message if credentials are not valid.<br>Display message if user login successfully.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
</table>


#### Logout Page

<table>
    <tr>
        <th colspan=2>Feature</th>
        <th>Users</th>
        <th>Test</th>
        <th>Outcome</th>
        <th>Pass/Fail</th>
    </tr>
    <tr>
        <td rowspan=2>Sign Out Page</td>
        <td rowspan=2>Sign Out button</td>
        <td rowspan=2>Registered</td>
        <td>Functionality</td>
        <td>Clicking the button sign out the user and redirect to the Home page.<br>Display message if user logout successfully.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
</table>

#### User Profile page

<table>
    <tr>
        <th colspan=2>Feature</th>
        <th>Users</th>
        <th>Test</th>
        <th>Outcome</th>
        <th>Pass/Fail</th>
    </tr>
    <tr>
        <td rowspan=8>Page Buttons</td>
        <td rowspan=2>Edit Profile button</td>
        <td rowspan=2>Registered</td>
        <td>Functionality</td>
        <td>Clicking Edit Profile button redirects to Edit Profile page.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Book Workout button</td>
        <td rowspan=2>Registered</td>
        <td>Functionality</td>
        <td>Clicking Book Workout button redirects to Book Workout page.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
     <tr>
        <td rowspan=2>Edit Workout icon/button</td>
        <td rowspan=2>Registered</td>
        <td>Functionality</td>
        <td>Clicking Edit Workout button redirects to Edit Workout page.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td rowspan=2>Delete Workout icon/button</td>
        <td rowspan=2>Registered</td>
        <td>Functionality</td>
        <td>Clicking Delete Workout button opens confirmation modal.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td rowspan=4>Delete confirmation modal</td>
        <td rowspan=2>Cancel button</td>
        <td rowspan=2>Registered</td>
        <td>Functionality</td>
        <td>Clicking Cancel button cancels deleting of workout and closes modal.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Delete button</td>
        <td rowspan=2>Registered</td>
        <td>Functionality</td>
        <td>Clicking Delete workout button delete selected workout and closes the modal.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
</table>

#### Update Profile Page

<table>
    <tr>
        <th colspan=2>Feature</th>
        <th>Users</th>
        <th>Test</th>
        <th>Outcome</th>
        <th>Pass/Fail</th>
    </tr>
    <tr>
        <td rowspan=10>Update Profile Form</td>
        <td rowspan=2>First name input</td>
        <td rowspan=2>Registered</td>
        <td>Functionality</td>
        <td>Text can be entered in the field.<br>Optional field. Allows to be left empty.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td rowspan=2>Last name input</td>
        <td rowspan=2>Registered</td>
        <td>Functionality</td>
        <td>Text can be entered in the field.<br>Optional field. Allows to be left empty.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td rowspan=2>Username input</td>
        <td rowspan=2>Registered</td>
        <td>Functionality</td>
        <td>Text can be entered in the field.<br>Field validates input to be present.<br>Validate input is a valid username.<br>Display message if username is not valid.<br></td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Focus effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>E-mail input</td>
        <td rowspan=2>Registered</td>
        <td>Functionality</td>
        <td>Text can be entered in the field.<br>Optional field. Allows to be left empty.<br>Validate input is an email address.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td rowspan=2>Update Profile button</td>
        <td rowspan=2>Registered</td>
        <td>Functionality</td>
        <td>Clicking the button submit the form and redirects to the User Profile page.<br>Updates user profile info if form is valid.<br>Display message if user profile is successfully updated.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
</table>

#### Staff Panel page

<table>
    <tr>
        <th colspan=2>Feature</th>
        <th>Users</th>
        <th>Test</th>
        <th>Outcome</th>
        <th>Pass/Fail</th>
    </tr>
    <tr>
        <td rowspan=2>Search Bar</td>
        <td rowspan=2>Input field</td>
        <td rowspan=2>Admins or staff members</td>
        <td>Functionality</td>
        <td>Placeholder "Search Booking" shows as expected.<br>Text can be entered in the field.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td rowspan=2>Delete icon/button</td>
        <td rowspan=2>Delete Workout icon/button</td>
        <td rowspan=2>Admins or staff members</td>
        <td>Functionality</td>
        <td>Clicking Delete Workout button opens confirmation modal.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td rowspan=4>Delete confirmation modal</td>
        <td rowspan=2>Cancel button</td>
        <td rowspan=2>Admins or staff members</td>
        <td>Functionality</td>
        <td>Clicking Cancel button cancels deleting of workout and closes modal.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Delete button</td>
        <td rowspan=2>Admins or staff members</td>
        <td>Functionality</td>
        <td>Clicking Delete workout button delete selected workout and closes the modal.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
</table>

#### Book Workout page

<table>
    <tr>
        <th colspan=2>Feature</th>
        <th>Users</th>
        <th>Test</th>
        <th>Outcome</th>
        <th>Pass/Fail</th>
    </tr>
    <tr>
        <td rowspan=4>Select element</td>
        <td rowspan=2>Workout selector</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Clicking on "Select Workout" selector all bookable workouts shows up.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td rowspan=2>Date selector</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Clicking on "Select Date" selector, Datepicker calender shows up.<br>Placeholder "Select Date" shows as expected.<br>Field validates input to be present.<br>Display message if date is not valid.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Custom CSS</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=4>Online Booking page buttons</td>
        <td rowspan=2>Continue button</td>
        <td rowspan=2>Registered</td>
        <td>Functionality</td>
        <td>Clicking the button redirects user to Booking submit page.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Back button</td>
        <td rowspan=2>Registered</td>
        <td>Functionality</td>
        <td>Clicking the Back button cancels the booking process and redirects user to User Profile page.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
</table>

#### Book Workout Submit page

<table>
    <tr>
        <th colspan=2>Feature</th>
        <th>Users</th>
        <th>Test</th>
        <th>Outcome</th>
        <th>Pass/Fail</th>
    </tr>
    <tr>
        <td rowspan=2>Select element</td>
        <td rowspan=2>Time selector</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Clicking on "Time" selector all bookable times shows up.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td rowspan=4>Online Booking page buttons</td>
        <td rowspan=2>Book Workout button</td>
        <td rowspan=2>Registered</td>
        <td>Functionality</td>
        <td>Clicking the button saves the booking and redirects user to User Profile page.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Back button</td>
        <td rowspan=2>Registered</td>
        <td>Functionality</td>
        <td>Clicking the Back button redirects user to previous Booking workout page.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
</table>

[Back to top ⇧](#genstar-music-store-testing)