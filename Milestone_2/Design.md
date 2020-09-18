# Milestone 2 - Design

## --- Project Info ---------------------------------------------------------------------------------------

- [eShop Project Folder](https://github.com/Eshop-project/CS-350)
- Other roles: [Code](https://github.com/Eshop-project/CS-350/blob/master/Milestone_2/Code.md), [Requirements](), [Tests](), []()

### Milestone_2

#### Role: 

    DESIGNER

#### Goal: 

I am to work with the coder and requirements to fit a design that matches the requirements set by the client. Following, the coder will implement the desired design and hopefully have all the correct functionality previously described by said client.

## --- eShop Software Architecture --------------------------------------------------------------------

### DATA

Following the CRUD acronym, or the [CREATE | READ | UPDATE | DELETE] system, we should be able to implement a handful of authorizations to each type of data that will allow for the best user experience in the app. First let's explain the needed models and the data to accompany those models:

- User data; can be C, R, U, (D, with the exception of some information worth keeping)
#### Basic Data
    - user.username
    - user.password
    - user.type(company or personal)
    - user.name
    
#### Company Data
    - user.description
    - user.products                : EACH ELEMENT OF TABLE WILL HAVE THESE SPECIFIC COLUMN TITLES
        - products.id
        - products.url
        - products.tax
        - products.price           : PRICE
        - products.description     : DESCR.
        - products.picture         : PICTURE OF PRODUCT
        - products.type            : TYPE OF PRODUCT, i.e. food, clothing, 
    - user.address
    - user.rating
    - user.contacts
        - contacts.phone
        - contacts.email
        - contacts.socials         : SOCIAL LINKS FOR COMPANY
    - user.payment_options
        - payment_options.accepted : CREDIT OR CASH OR GIFT OR CHECK

#### Personal Data
    - user.location                : DIFFERENT FROM ADDRESS
    - user.cart                    : COLLECTION OF PRODUCTS WANTED FOR PURCHASE
    - user.past_purchases
        - past_purchases.any       : BOOLEAN, YES OR NO TO ANY PAST PURCHASES
        - past_purchases.---       : DATA THAT ACCOUNTS FOR THE PURCHASES PRODUCTS INFO
    - user.favorites               : NOT IMPORTANT
    - user.payment
        - payment.type             : CREDIT OR CASH OR GIFT OR CHECK
            - CONDITIONAL BASED ON TYPE; CAN BE THOUGHT OF AS C.C. NUMBER, C.C. EXPIRATION, CVV CODE
    - user.billing
        - billing.addresses        : LIST OF ADDRESSES, MULTIPLE
        - billing.country          : ASSUMING USA/CANADA, NOT MEANT FOR OUTSIDE OF US
        - billing.state            : ASSUMING COUNTRY IS USA
        - billing.city
        - billing.zip
    - user.address
    
- Site Data; can be C, R, U
    - socials                      : SOCIAL LINKS FOR OWNER OF SITE
    - contacts
    - about
    


### MODELS

Above would be the database schema. From the user data we could derive a few models that would access the necessary database tables. I will not specify the specific tables, because it may be ambiguous now, but will not be in the future. Also these classes listed below will have methods to account for CRUD operations.

- User 
    - Most user info.
- Product
    - Meant for getting product data such as name, picture, description, ect. Tied to company user model.
- Payment
    Model for holding payment data such as credit cards, cvv, exp. dates, ect. Tied to personal user model.
    
W


    
    
    
    
    
