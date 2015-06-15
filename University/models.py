"""
Author: Amitayush Thakur, Sagar Grover and Abhimanyu Siwach
This file contains various models for our databases.
"""
from django.db import models



#Some Important Parameters
MAX_LEN_OF_ADDRESS=500
MAX_LEN_OF_UNIV_NAME=100
MAX_LEN_OF_CLG_NAME=100
DEFAULT_FIELD_VALUE=None


#Main class definitions

class University(models.Model):
    university_id = models.CharField(max_length=MAX_LEN_OF_UNIV_NAME,null=False,default=DEFAULT_FIELD_VALUE)
    _university_name = models.CharField(max_length=MAX_LEN_OF_UNIV_NAME,default=DEFAULT_FIELD_VALUE,null=False)
    def __str__(self):
        """ __str__()-returns the name of university"""
        return self._university_name
    def get_university_id(self):
        return self.university_id
    def get_university_name(self):
        return self.university_name
    def set_university_id(self,university_id):
        self.university_id = university_id
    def set_university_name(self,university_name):
        self.university_name = university_name
    class Meta:
        abstract=True
    
class College(University):
    def __str__(self):
        """ __str__()- returns the name of the college """
        return self.college_name
    _email = models.EmailField(null=False,default=DEFAULT_FIELD_VALUE)
    _address = models.CharField(max_length=MAX_LEN_OF_ADDRESS,default=DEFAULT_FIELD_VALUE,null=True) #Optional
    _mobile_number = models.BigIntegerField(null=True) #Optional
    college_name = models.CharField(max_length=MAX_LEN_OF_CLG_NAME,default=DEFAULT_FIELD_VALUE,null=False) #Primary key
    college_id = models.CharField(max_length=MAX_LEN_OF_CLG_NAME,null=False,default=DEFAULT_FIELD_VALUE,primary_key=True)
    def get_college_id(self):
        return self.college_id
    def get_college_name(self):
        return self.college_name
    def get_email(self):
        return self.email
    def get_mobile_number(self):
        return self.mobile_number
    def get_address(self):
        return self.address
    def update_college_id(self,new_id):
        self.college_id = new_id
    def update_college_name(self,new_name):
        self.college_name = new_name
    def update_email(self,email):
        self.email=email
    def update_mobile_number(self,number):
        self.mobile_number=number
    def update_address(self,address):
        self.address=address