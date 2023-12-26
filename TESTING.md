# Genstar Music Store Testing

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

[The W3C Markup Validator](https://validator.w3.org) was used to check HTML code of a webpage. 

All errors on html pages are of the same type and mostly are related for using Django in HTML code. Because of each page is an extension of Base.html, there is no usual tags in the beginning of pages, and code validator marks it as both warning and error. Most of the errors are "Bad value" errors, that points to illegal characters. This is due to using of Django synthax in href links and other HTML tags. I went through every HTML page and fixed code problems related to invalid spaces, unclosed tags and other small synthax errors that has no impact on code and page functionality.

Following errors were found on each html page:

* Base page errors

![HTML Validator index page check errors](/media/code-validation/html/base.html.png)

* Products page errors

![Products page errors](/media/code-validation/html/products.html.png)

* Product details page errors

![Product details page errors](/media/code-validation/html/product_detail.png)

* Add product page errors

![Add Product page errors](/media/code-validation/html/add_product.html.png)

* Edit product page errors

![Edit products page errors](/media/code-validation/html/edit_product.html.png)

* Products in category page errors

![Products in category page errors](/media/code-validation/html/products_in_category.html.png)

* Quantity form page errors

![Quantity form page errors](/media/code-validation/html/quantity_form_products.html.png)

* Subscribe page errors

![Subscribe page errors](/media/code-validation/html/subscribe.html.png)

* Unsubscribe page errors

![Unsubscribe page errors](/media/code-validation/html/unsubscribe.html.png)

* Wishlist page errors

![Wishlist page errors](/media/code-validation/html/wishlist.html.png)

* Shopping cart page errors

![Shopping cart page errors](/media/code-validation/html/cart.html.png)

* Checkout page errors

![Checkout page errors](/media/code-validation/html/checkout.html.png)

* Checkout success page errors

![Checkout success page errors](/media/code-validation/html/checkout_success.html.png)

* Profiles page errors

![Profiles page errors](/media/code-validation/html/profiles.html.png)

* Orders history page errors

![Orders history page errors](/media/code-validation/html/orders_history.html.png)

* Profile settings page errors

![Profile settings page errors](/media/code-validation/html/profile_settings.html.png)

* Wishlist in profile page errors

![Wishlist in profile page errors](/media/code-validation/html/wishlist_profile.html.png)


### CSS

For check of CSS in a project [The W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) was used.

There are no repetitions, comment out or double code across css files.

Each file was checked manually in [The W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) and no errors were found.


### Python

Pylint was used continuously during the development process to analyze the Python code for programming errors.

[CI Python Linter](https://pep8ci.herokuapp.com) was used to validate the Python code to validate the Python code for PEP8 requirements. Results are in a table below:


| Location | Errors / Warnings | Code Reviewed |
| --- | --- | --- |
| ./manage.py | No errors / warnings |![manage.py code reviewed image](/media/code-validation/python/genstar-music-store-manage.py.png) |
| ./settings.py | No errors / warnings |![settings.py code reviewed image](/media/code-validation/python/genstar-music-store-settings.py.png) |
| ./urls.py | No errors / warnings |![urls.py code reviewed image](/media/code-validation/python/genstar-music-store-urls.py.png) |
| ./products/admin.py | No errors / warnings |![admin.py code reviewed image](/media/code-validation/python/products-admin.py.png) |
| ./products/apps.py | No errors / warnings |![apps.py code reviewed image](/media/code-validation/python/products-apps.py.png) |
| ./products/forms.py | No errors / warnings |![forms.py code reviewed image](/media/code-validation/python/products-forms.py.png) |
| ./products/models.py | No errors / warnings |![models.py code reviewed image](/media/code-validation/python/products-models.py.png) |
| ./products/urls.py | No errors / warnings | ![urls.py code reviewed image](/media/code-validation/python/products-urls.py.png) |
| ./products/views.py | No errors / warnings |![views.py code reviewed image](/media/code-validation/python/products-views.py.png) |
| ./cart/apps.py | No errors / warnings |![apps.py code reviewed image](/media/code-validation/python/cart-apps.py.png) |
| ./cart/contexts.py | No errors / warnings |![contexts.py code reviewed image](/media/code-validation/python/cart-contexts.py.png) |
| ./cart/models.py | No errors / warnings |![models.py code reviewed image](/media/code-validation/python/cart-models.py.png) |
| ./cart/urls.py | No errors / warnings |![urls.py code reviewed image](/media/code-validation/python/cart-urls.py.png) |
| ./cart/views.py | No errors / warnings |![views.py code reviewed image](/media/code-validation/python/cart-views.py.png) |
| ./checkout/admin.py | No errors / warnings |![admin.py code reviewed image](/media/code-validation/python/checkout-admin.py.png) |
| ./checkout/apps.py | No errors / warnings |![apps.py code reviewed image](/media/code-validation/python/checkout-apps.py.png) |
| ./checkout/forms.py | No errors / warnings |![forms.py code reviewed image](/media/code-validation/python/checkout-forms.py.png) |
| ./checkout/models.py | No errors / warnings |![models.py code reviewed image](/media/code-validation/python/checkout-models.py.png) |
| ./checkout/signals.py | No errors / warnings | ![signals.py code reviewed image](/media/code-validation/python/checkout-signals.py.png) |
| ./checkout/urls.py | No errors / warnings | ![urls.py code reviewed image](/media/code-validation/python/checkout-urls.py.png) |
| ./checkout/views.py | No errors / warnings |![views.py code reviewed image](/media/code-validation/python/checkout-views.py.png) |
| ./checkout/webhook-handler.py | No errors / warnings | ![webhook-handler.py code reviewed image](/media/code-validation/python/checkout-webhook-handler.py.png) |
| ./checkout/webhooks.py | No errors / warnings | ![webhooks.py code reviewed image](/media/code-validation/python/checkout-webhooks.py.png) |
| ./profiles/admin.py | No errors / warnings |![admin.py code reviewed image](/media/code-validation/python/profiles-admin.py.png) |
| ./profiles/apps.py | No errors / warnings |![apps.py code reviewed image](/media/code-validation/python/profiles-apps.py.png) |
| ./profiles/forms.py | No errors / warnings |![forms.py code reviewed image](/media/code-validation/python/profiles-forms.py.png) |
| ./profiles/models.py | No errors / warnings |![models.py code reviewed image](/media/code-validation/python/profiles-models.py.png) |
| ./profiles/urls.py | No errors / warnings | ![urls.py code reviewed image](/media/code-validation/python/profiles-urls.py.png) |
| ./profiles/views.py | No errors / warnings |![views.py code reviewed image](/media/code-validation/python/profiles-views.py.png) |

### JavaScript

[JSHint, a JavaScript Code Validator](https://jshint.com) was used to check JS code.

No errors were found.

[Back to top ⇧](#genstar-music-store-testing)

# Accessibility

### Lighthouse Reports

Page | Lighthouse Report |
| --- | --- |
| Products | ![Products Page Lighthouse Report](/media/code-validation/lighthouse/products-page-lighthouse.png) |
| Product details | ![Product details Page Lighthouse Report](/media/code-validation/lighthouse/products-details-page-lighthouse.png) |
| Add / Edit Product | ![Add / Edit Page Lighthouse Report](/media/code-validation/lighthouse/add-edit-products-details-page-lighthouse.png) |
| Products in category | ![Products in category Page Lighthouse Report](/media/code-validation/lighthouse/products-in-category-details-page-lighthouse.png) |
| Shopping Cart !| ![Shopping Cart page Lighthouse Report](/media/code-validation/lighthouse/shopping-cart-details-page-lighthouse.png) |
| Checkout !| ![Checkout Page Lighthouse Report](/media/code-validation/lighthouse/checkout-page-lighthouse.png) |
| Order Confirmation !| ![Order Confirmation Page Lighthouse Report](/media/code-validation/lighthouse/checkout-success-page-lighthouse.png) |
| Wishlist | ![Wishlist Page Lighthouse Report](/media/code-validation/lighthouse/wishlist-page-lighthouse.png) |
| My Profile | ![My Profile Page Lighthouse Report](/media/code-validation/lighthouse/my-profile-page-lighthouse.png) |
| Orders History | ![Orders History Page Lighthouse Report](/media/code-validation/lighthouse/orders-history-page-lighthouse.png) |
| Profile Wishlist| ![Profile Wishlist Page Lighthouse Report](/media/code-validation/lighthouse/profile-wishlist-page-lighthouse.png) |
| Profile Settings | ![Profile Settings Page Lighthouse Report](/media/code-validation/lighthouse/profile-settings-page-lighthouse.png) |
| Register | ![Register Page Lighthouse Report](/media/code-validation/lighthouse/register-page-lighthouse.png) |
| Login | ![Login Page Lighthouse Report](/media/code-validation/lighthouse/login-page-lighthouse.png) |
| Logout | ![Logout Page Lighthouse Report](/media/code-validation/lighthouse/logout-page-lighthouse.png) |
| Subscribe | ![Subscribe Page Lighthouse Report](/media/code-validation/lighthouse/subscribe-page-lighthouse.png) |

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
Samsung Z Flip 5 | Android |No appearance, responsiveness nor functionality issues. | <span style="color:green">Pass</span> |
Xiaomi XT11 6.2" | Android |No appearance, responsiveness nor functionality issues. | <span style="color:green">Pass</span> |

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
        <td rowspan=28>Navigation Bar</td>
        <td rowspan=2>Main logo link</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Clicking the link redirects to the Products page.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td rowspan=2>Search input field</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Search text input works as expected</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td rowspan=2>Search button</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Clicking the button starts searching query</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td rowspan=2>My Account icon</td>
        <td rowspan=2>Not signed in customers</td>
        <td>Functionality</td>
        <td>Clicking the icon opens dropdown menu with Login and Register links.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
     <tr>
        <td>Style</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td rowspan=2>My Account icon</td>
        <td rowspan=2>Signed in customers</td>
        <td>Functionality</td>
        <td>Clicking the icon opens dropdown menu with Product Management, My Profile and Logout links </td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td rowspan=2>Wishlist icon</td>
        <td rowspan=2>Signed in customers</td>
        <td>Functionality</td>
        <td>Clicking the icon redirects to customer wishlist page.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
        <tr>
        <td>Style</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td rowspan=2>Shopping cart icon</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Clicking the icon redirects customer to shopping cart page.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td rowspan=2>Mega Menu bar</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Clicking the relative link in menu opens the relative product category.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>My Account - Register link</td>
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
        <td rowspan=2>My Account - Login link</td>
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
        <td rowspan=2>My Account - Product Management</td>
        <td rowspan=2>Signed in customer</td>
        <td>Functionality</td>
        <td>Clicking the link redirects to the Product Management Add Product page.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>My Profile link</td>
        <td rowspan=2>Signed in customers</td>
        <td>Functionality</td>
        <td>Clicking the link redirects to the My Profile page.</td>
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
        <td rowspan=0>Footer</td>
        <td rowspan=2>Email input field</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Text input field for email address.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>N/A</td>
        <td><span>N/A</span></td>
    </tr>
     <tr>
        <td rowspan=2>Subscribe button</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Clicking subscribe button submits email to subscribe for newsletters.</td>
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
        <td>Clicking the link opens Facebook business page on a separate tab.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>N/A</td>
        <td><span>N/A</span></td>
    </tr>
    <tr>
        <td rowspan=2>Website logo in footer</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Clicking the logo opens main Products page.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>N/A</td>
        <td><span>N/A</span></td>
    </tr>
    <tr>
        <td rowspan=2>Support - Unsubscribe from newsletter button</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Clicking the button unsubscribe customer from newsletter.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>N/A</td>
        <td><span>N/A</span></td>
    </tr>
</table>

#### Products page

<table>
    <tr>
        <th colspan=2>Feature</th>
        <th>Users</th>
        <th>Test</th>
        <th>Outcome</th>
        <th>Pass/Fail</th>
    </tr>
    <tr>
        <td rowspan=12>Products page</td>
        <td rowspan=2>Left/Right carousel scroll buttons</td>
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
    <tr>
        <td rowspan=2>Category buttons</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Clicking the buttons opens relative category.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effects work as expected</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>"Sort by" filter</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Allows to choose different product sorting filters.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td rowspan=2>Product cards</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Clicking the product image opens product details page.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td rowspan=2>Heart icon/button on product card</td>
        <td rowspan=2>Signed in customers</td>
        <td>Functionality</td>
        <td>Clicking the icon/button adds product to wishlist.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effects work as expected</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Save button</td>
        <td rowspan=2>Signed in customers</td>
        <td>Functionality</td>
        <td>Clicking this button adds product to wishlist and redirects to main products page.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
</table>

#### Product details page

<table>
    <tr>
        <th colspan=2>Feature</th>
        <th>Users</th>
        <th>Test</th>
        <th>Outcome</th>
        <th>Pass/Fail</th>
    </tr>
    <tr>
        <td rowspan=18>Product details</td>
        <td rowspan=2>Product image</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Clicking the product image opens product image on new tab.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td rowspan=2>Radio buttons (Rate the product)</td>
        <td rowspan=2>Signed in customers</td>
        <td>Functionality</td>
        <td>Check the relative radio button for rating the product.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td rowspan=2>Submit Rating</td>
        <td rowspan=2>Signed in customers</td>
        <td>Functionality</td>
        <td>Click the "submit rating" button to rate the product and submit checked radio button value.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td rowspan=2>Edit Product</td>
        <td rowspan=2>Admins and Staff members</td>
        <td>Functionality</td>
        <td>Clicking this button opens product editing page.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td rowspan=2>Delete Product</td>
        <td rowspan=2>Admins and Staff members</td>
        <td>Functionality</td>
        <td>Clicking this button deletes product from the website and database.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td rowspan=2>Continue Shopping button</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Clicking this button redirects customers to main products page.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td rowspan=2>Add to Cart button</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Clicking this button adds product to shopping cart and refreshes the page.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td rowspan=2>Radio buttons (Rate the product)</td>
        <td rowspan=2>Signed in customers</td>
        <td>Functionality</td>
        <td>Check the relative radio button for rating the product.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
</table>

#### Shopping cart page

<table>
    <tr>
        <th colspan=2>Feature</th>
        <th>Users</th>
        <th>Test</th>
        <th>Outcome</th>
        <th>Pass/Fail</th>
    </tr>
    <tr>
        <td rowspan=14>Shopping cart</td>
        <td rowspan=2>Product name as a link</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Clicking product name opens product details page.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>General styling</td>
        <td>Pass</td>
    </tr>
     <tr>
        <td rowspan=2>Product category as a link</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Clicking product category opens products category page.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>General styling</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td rowspan=2>Decrease/Increase quantity buttons (- and +)</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Clicking this buttons decrease or increase product quantity in value input field.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>General styling</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td rowspan=2>Update Cart button</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Clicking this button updates the cart with new product quantity values.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>General styling</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td rowspan=2>Remove button</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Clicking this button removes product item from the shopping cart.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>General styling</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td rowspan=2>Proceed to Checkout button</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Clicking this button redirects customers to Checkout page.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect works as expected</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Continue Shopping button</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Clicking this button redirects customers to main products page.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
</table>

#### Checkout page

<table>
    <tr>
        <th colspan=2>Feature</th>
        <th>Users</th>
        <th>Test</th>
        <th>Outcome</th>
        <th>Pass/Fail</th>
    </tr>
    <tr>
        <td rowspan=12>Checkout form</td>
        <td rowspan=2>Text input fields with * (required)</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Text can be entered in the field.<br>Field is required and validates input.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Placeholders</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td rowspan=2>Text input field without * (not required)</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Text can be entered in the field.<br>Field is not required and can be skipped.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Placeholders</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td rowspan=2>Payment / Card number input field</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Enter card number, expiry date and CVC code<br>Field is required and validates input.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td rowspan=2>Privacy Policy and Terms and Conditions links</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Clicking this links opens Privacy Policy or Terms and Conditions pages on new tab.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td rowspan=2>Back to Cart button</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Clicking the button redirects customer to shopping cart page.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Bootstrap button CSS</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td rowspan=2>Complete Order button</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Clicking the button completes the order and in case of success redirects customer to Order Confirmation page.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Bootstrap button CSS</td>
        <td>Pass</td>
    </tr>
</table>

#### Product Management page / Add or Edit Product (Only for Admin or Staff members)

<table>
    <tr>
        <th colspan=2>Feature</th>
        <th>Users</th>
        <th>Test</th>
        <th>Outcome</th>
        <th>Pass/Fail</th>
    </tr>
    <tr>
        <td rowspan=12>Checkout form</td>
        <td rowspan=2>Text input fields with * (required)</td>
        <td rowspan=2>Admins or Staff members</td>
        <td>Functionality</td>
        <td>Text can be entered in the field.<br>Field is required and validates input.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td rowspan=2>Text input field without * (not required)</td>
        <td rowspan=2>Admins or Staff members</td>
        <td>Functionality</td>
        <td>Text can be entered in the field.<br>Field is not required and can be skipped.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td rowspan=2>Choose file button</td>
        <td rowspan=2>Admins or Staff members</td>
        <td>Functionality</td>
        <td>Clicking the button opens explorer window to choose picture for product</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>N/A</td>
        <td>N/A/td>
    </tr>
    <tr>
        <td rowspan=2>Add/Edit Product button</td>
        <td rowspan=2>Admins or Staff members</td>
        <td>Functionality</td>
        <td>Adds product to database / Edits existing product information</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td rowspan=2>Cancel button</td>
        <td rowspan=2>Admins or Staff members</td>
        <td>Functionality</td>
        <td>Cancels adding or editing of product</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>N/A</td>
        <td>N/A</td>
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
        <td rowspan=2>Signed in customers</td>
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

#### My Profile page

<table>
    <tr>
        <th colspan=2>Feature</th>
        <th>Users</th>
        <th>Test</th>
        <th>Outcome</th>
        <th>Pass/Fail</th>
    </tr>
    <tr>
        <td rowspan=12>My Profile</td>
        <td rowspan=2>Profile main side menu link</td>
        <td rowspan=2>Signed in customers</td>
        <td>Functionality</td>
        <td>Clicking this button refreshes the page / return to My Profile page.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected when selected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Orders History side menu link</td>
        <td rowspan=2>Signed in customers</td>
        <td>Functionality</td>
        <td>Clicking this button redirects to Orders History page.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected when selected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
     <tr>
        <td rowspan=2>My wishlist side menu link</td>
        <td rowspan=2>Signed in customers</td>
        <td>Functionality</td>
        <td>Clicking this button redirects to Profile Wishlist page.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected when selected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Profile setting side menu link</td>
        <td rowspan=2>Signed in customers</td>
        <td>Functionality</td>
        <td>Clicking this button redirects to Profile Setting page.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected when selected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Logout side menu link</td>
        <td rowspan=2>Signed in customers</td>
        <td>Functionality</td>
        <td>Clicking this button redirects to Sign Out page.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td rowspan=2>View all orders button</td>
        <td rowspan=2>Signed in customers</td>
        <td>Functionality</td>
        <td>Clicking this button redirects customer to Orders History page.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Delete order button</td>
        <td rowspan=2>Signed in customers</td>
        <td>Functionality</td>
        <td>Clicking this button deletes selected order from the list and database.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Order ID link</td>
        <td rowspan=2>Signed in customers</td>
        <td>Functionality</td>
        <td>Clicking this link redirects customer to respective Order Confirmation page.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
</table>

#### Profile settings Page

<table>
    <tr>
        <th colspan=2>Feature</th>
        <th>Users</th>
        <th>Test</th>
        <th>Outcome</th>
        <th>Pass/Fail</th>
    </tr>
    <tr>
        <td rowspan=10>Profile settings Form</td>
        <td rowspan=2>Text input fields</td>
        <td rowspan=2>Signed in customers</td>
        <td>Functionality</td>
        <td>Text can be entered in the field.<br>Optional fields. Allows to be left empty.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td rowspan=2>Country selector (required)</td>
        <td rowspan=2>Signed in customers</td>
        <td>Functionality</td>
        <td>Country can be selected here.<br>Required field.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td rowspan=2>Update Profile info button</td>
        <td rowspan=2>Signed in customers</td>
        <td>Functionality</td>
        <td>Clicking the button submit the form and refreshes the page.<br>Updates user profile info if form is valid.<br>Display message if user profile is successfully updated.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
</table>

#### Wishlist / Profile wishlist page

<table>
    <tr>
        <th colspan=2>Feature</th>
        <th>Users</th>
        <th>Test</th>
        <th>Outcome</th>
        <th>Pass/Fail</th>
    </tr>
    <tr>
        <td rowspan=14>Wishlist</td>
        <td rowspan=2>Product name as a link</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Clicking product name opens product details page.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>General styling</td>
        <td>Pass</td>
    </tr>
     <tr>
        <td rowspan=2>Product category as a link</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Clicking product category opens products category page.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>General styling</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td rowspan=2>Remove button</td>
        <td rowspan=2>Signed in customers</td>
        <td>Functionality</td>
        <td>Clicking this button removes product from wishlist.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td rowspan=2>Add to Cart button</td>
        <td rowspan=2>Signed in customers</td>
        <td>Functionality</td>
        <td>Clicking this button adds product to shopping cart.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
</table>

[Back to top ⇧](#genstar-music-store-testing)