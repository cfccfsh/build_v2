from django.db import models

# Create your models here.
from django.db import models


class Department(models.Model):
    department_name = models.CharField(max_length=50,null=True)
    parent_name = models.CharField(max_length=50,null=True)
    area = models.CharField(max_length=50,null=True)
    status = models.SmallIntegerField(null=True)
    creator = models.CharField(max_length=100,null=True)
    create_time = models.DateTimeField(null=True)
    update_time = models.DateTimeField(null=True)

    class Meta:
        db_table = 'cfg_sys_department'


class Role(models.Model):
    name = models.CharField(max_length=100,null=True)
    use_authorize = models.TextField(null=True)
    data_authorize = models.TextField(null=True)
    data_create_authorize = models.TextField(null=True)
    status = models.SmallIntegerField(null=True)
    creator = models.CharField(max_length=100,null=True)
    create_time = models.DateTimeField(null=True)
    update_time = models.DateTimeField(null=True)

    class Meta:
        db_table = 'cfg_sys_role'

class User(models.Model):
    user_name = models.CharField(max_length=50,null=True)
    user_pwd = models.CharField(max_length=50,null=True)
    real_name = models.CharField(max_length=50,null=True)
    msisdn = models.CharField(max_length=50,null=True)
    email = models.CharField(max_length=50,null=True)
    img_path = models.CharField(max_length=100,null=True)
    role_id = models.ManyToManyField(Role,null=True)
    department_id = models.OneToOneField(Department,on_delete=models.CASCADE,related_name='department')
    status = models.SmallIntegerField(null=True)
    creator = models.CharField(max_length=100,null=True)
    create_time = models.DateTimeField(null=True)
    update_time = models.DateTimeField(null=True)

    class Meta:
        db_table = 'cfg_sys_user'
