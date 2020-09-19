

"""
USER MODEL SHOULD HAVE A NUMBER OF ELEMENTS:
-   user.username
-   user.password
-   user.email
-   user.name       i.e, full name
-   user.type       i.e, (company, ind_user)

Custom User model is needed, from here we can implement different types of elements or parameters.

Get's complicated, but better to user custom the using base.

----------------------------------------------------------------------------------|

PRODUCT MODEL SHOULD HAVE FOLLOWING:
-   product.name
-   product.price
-   product.picture
-   product.description
-   product.rating              -- hard to tell if this is absolutly needed.

FROM HERE WE CAN ADD INDEPENDENT INFO

PERMISSION ONLY GIVEN TO COMPANY ACCOUNT

----------------------------------------------------------------------------------|

--tbd

"""

from django.db import models
from django.contrib.auth.models import User


class NewUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)




