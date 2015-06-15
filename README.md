ProfBrew
========

Rating Professors

Note For Developers
====================
Use the following conventions for naming th variables:

-> Use '_' seperated variables naming for naming local variables. Use camel casing for naming of the classes.

-> Use 4 spaces for indentation and not tab spacing(if you use tab spacing then make sure that you make appropriate changes in the IDE before compiling the code.)

-> For making the vairables private append '_' before the variable name.

-> For the database use MySql. Name the database as 'profbrew'. Change the ProfBrew/settings.py make the following changes:

     DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.mysql',
          'NAME': 'profbrew',
          'USERNAME': '....', # Your MySql Username here
          'PASSWORD':'*****',  #Your Password Here
      }
    }

-> For commenting and docunmentation. Follow the folloing convention:
     
     class Users(models.Model):
     """
        Users()- Extends Django's pre-implimented User class. 
        The User class is meant for storing the details of the users into database and keep track of the users.
     """
     def __init__(self):
        #To add to the database
        """
            _username -> private field and is the primary key.
            name -> has the name of the person. It is public.
            _password -> private and encrypted.
            _email -> private field and has valid email address.
            user_type -> has the user type and is public.
            _mobile_number -> private and is the only optional field
        """
        self._username = models.CharField(primary_key=True,max_length=MAX_LEN_OF_USERNAME)  #Primary Key
        self.name = models.CharField(max_length=MAX_LEN_OF_NAME)
        self._password = models.CharField(max_length=MAX_LEN_OF_PASSWORD)
        self.user_type = models.CharField(max_length=10,choices=USER_TYPE,default=USER_TYPE.VISITOR)
        self._email = models.EmailField;
        self._mobile_number = models.BigIntegerField  #Optional Field
        self._date_joined = models.DateTimeField
      ...............
      ...............

-> Use """ for commenting because it can be used to generate 'docstring' i.e __doc__(). Also read about docstrings.

-> Read the following tutorial on using git: http://www.slideshare.net/nilaybinjola/git-basic-crash-course?utm_source=slideshow02&utm_medium=ssemail&utm_campaign=share_slideshow_loggedout

-> Follow the following convention to write the commit message:
   
   git commit -m "Changed '[file_location]';'[changes_made]'"
   
-> Keep commiting important chages and maintain the proper commit history by using the proper commit messages.
