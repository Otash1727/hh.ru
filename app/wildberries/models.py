from django.db import models
from django.utils.translation import gettext_lazy as _ # languages settings
from django.utils import timezone

# create the desired model
class Products(models.Model):
    name=models.CharField(_('name'),max_length=300,null=True,blank=True)
    article=models.BigIntegerField(_('article'),null=True,blank=True)
    price=models.FloatField(_('price'),null=True,blank=True)
    rating=models.FloatField(_('rating'),null=True,blank=True)
    quantity=models.IntegerField(_('quantity'),null=True,blank=True)
    searching=models.BigIntegerField(_('searching'),null=True,blank=True)
    class Meta:
        verbose_name=_('Products')
        verbose_name_plural=_('Products')

    def __str__(self):
        return self.name
    


class Accounting_Records(models.Model):
    profile_name=models.CharField(_('profile_name'),max_length=200,null=True,blank=True)
    username=models.CharField(_('username'),max_length=250,null=True,blank=True)
    user_id=models.BigIntegerField(_('user_id'),null=True,blank=True)
    created_at=models.DateTimeField(_('created_at'),default=timezone.now)
    class Meta:
        verbose_name=_('Accounting Records')
        verbose_name_plural=_('Accounting Records')
    
    def __str__(self):
        return f"{self.username}"

class User_Request_History(models.Model):
    category=models.ForeignKey(Accounting_Records,on_delete=models.CASCADE,verbose_name=_('category'))
    
    created_at=models.DateField(_('created_at'),default=timezone.now)

    class Meta:
        verbose_name=_('User Request History')
        verbose_name_plural=_('User Request Histories')
    
    def __str__(self):
        return f"{self.category.name}"