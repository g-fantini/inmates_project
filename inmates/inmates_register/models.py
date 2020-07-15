from django.db import models
from django.utils.html import format_html

class InMate(models.Model):
    """A class used to represent an inmate
    
    Methods
    -------
    history_link():
        Returns the link to the history page for the specific inmate
        
    edit_link()
       Returns the link to edit the inmate info
        
    """
    inmate_name= models.CharField(max_length=100)
    inmate_surname= models.CharField(max_length=100)
    date_of_birth= models.DateField()
    cell_num= models.CharField(max_length=10)
    intake_time= models.DateTimeField()
    
    def history_link (self):
        """
        Returns the link to the history page for the specific inmate
        
        Returns
        ------
        String
        '<a href ="/admin/inmates_register/history/?inmate_id__id__exact={}">{}</a>'
        """
        return format_html(
            '<a href ="/admin/inmates_register/history/?inmate_id__id__exact={}">{}</a>',
            self.id,
            str(self)
        )
    
    def edit_link(self):
        """
        Returns the link to edit the inmate info
        
        Returns
        ------
        String
        '<a href ="/admin/inmates_register/inmate/{}/change/">{}</a>'
        """
        return format_html(
            '<a href ="/admin/inmates_register/inmate/{}/change/">{}</a>',
            self.id,
            "Edit"
        )
    
    def __str__(self):
        """
        Returns a string representation of the class, in the format:
        Name Surname CellNum
        
        Returns
        ------
        String
        Name Surname CellNum
        """
        return self.inmate_name + " " + self.inmate_surname + " (" + self.cell_num + ")"
        
class History(models.Model):
    """A class used to represent an History
    """
    LOCATIONS = [("CL","Cell"),("GR","Garden"),("CF","Cafeteria"),("SH","Shower"),("KT","Kitchen")]
    time = models.DateTimeField()
    location = models.CharField(max_length=15, choices=LOCATIONS)
    inmate = models.ForeignKey(InMate, related_name='locations', on_delete=models.CASCADE)
    
    