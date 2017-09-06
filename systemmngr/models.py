from django.db import models

# Create your models here.
class Menu(models.Model):
    IS_ONLY_CENTER = (
        ('1', 'yes'),
        ('2', 'no'),
    )
    MENU_TYPE = (
        ('folder', 'folder'),
        ('text', 'text'),
    )
    sysid = models.BigIntegerField(unique=True)
    name = models.CharField(max_length=200)
    functionregid = models.IntegerField(blank=True, null=True)
    grade = models.IntegerField()
    ordeno = models.BooleanField()
    parentid = models.IntegerField()
    url = models.CharField(max_length=200, blank=True, null=True)
    icon = models.CharField(max_length=200, blank=True, null=True)
    parameter = models.CharField(max_length=200, blank=True, null=True)
    createtime = models.DateField(auto_now=True)
    updatetine = models.DateField(auto_now_add=True)
    isonlycenter = models.CharField(choices=IS_ONLY_CENTER, default='1', max_length=1)
    type = models.CharField(choices=MENU_TYPE, default='folder', max_length=10)

class Menupermission(models.Model):
    roleid = models.BigIntegerField()
    meunid = models.BigIntegerField()
    orgid = models.IntegerField()
    create_time = models.DateField(auto_now=True)
    update_time = models.DateField(auto_now_add=True)

class Role(models.Model):
    name = models.CharField(unique=True, max_length=50)
    describes = models.CharField(max_length=100, blank=True, null=True)
    createtime = models.DateField(auto_now=True)
    updatetime = models.DateField(auto_now_add=True)
    orgid_display = models.CharField(max_length=225, blank=True, null=True)
    
    def __unicode__(self):
        return self.name

class Userrole(models.Model):
    userid =  models.BigIntegerField()
    roleid = models.BigIntegerField()
    createtime = models.DateField(auto_now=True)
    updatetime = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return 'roleid-{}-userid-{}'.format(self.roleid, self.userid)
    
    
class Userinfo(models.Model):
    STATUS_CHOICES = (('1', 'normal'),
                      ('2', 'suoding'),
                      ('3', 'colod'),
                      ('4', 'cancel'))
    code = models.CharField(max_length=30 , blank=True, null=True)
    name = models.CharField(max_length=30 , blank=True, null=True)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=10, blank=True, null=True)
    idcard = models.CharField(max_length=10, blank=True, null=True)
    password = models.CharField(max_length=200)
   # ismultipoint = models.SmallIntegerField(max_length=1)
    status = models.CharField(choices=STATUS_CHOICES, default=1, max_length=1)
    createtime = models.DateField(auto_now=True)
    updatetime = models.DateField(auto_now_add=True)
    isfirstlogin = models.IntegerField(blank=True, null=True)
    updatepassword =  models.DateField(auto_now_add=True)
    freezedate = models.DateField(blank=True, null=True)
    lastlogin = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.email


