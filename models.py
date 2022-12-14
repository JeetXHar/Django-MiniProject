# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Catalogue(models.Model):
    book_id = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=100)
    book_isbn = models.CharField(max_length=13)
    author_name = models.CharField(max_length=60)
    day_of_addition = models.DateField()
    genre = models.CharField(max_length=40, blank=True, null=True)
    edition = models.IntegerField()
    times_borrowed = models.IntegerField(blank=True, null=True)
    min_age = models.IntegerField(blank=True, null=True)
    currently_borrowed = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalogue'


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=1)
    email_address = models.CharField(max_length=30, blank=True, null=True)
    phone_number = models.CharField(max_length=10)
    home_address = models.CharField(max_length=100, blank=True, null=True)
    currently_borrowed = models.IntegerField(blank=True, null=True)
    password = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Issue(models.Model):
    issue_id = models.AutoField(primary_key=True)
    book = models.ForeignKey(Catalogue, models.DO_NOTHING)
    customer = models.ForeignKey(Customer, models.DO_NOTHING)
    staff = models.ForeignKey('Staff', models.DO_NOTHING)
    issue_date = models.DateTimeField(blank=True, null=True)
    return_by = models.DateTimeField(blank=True, null=True)
    current_status = models.IntegerField()
    fine = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'issue'


class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    staff_name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=1)
    prev_exp = models.IntegerField(blank=True, null=True)
    joining_date = models.DateField()
    phone_number = models.CharField(max_length=10)
    email_address = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'staff'


class Submissions(models.Model):
    submission_id = models.AutoField(primary_key=True)
    issue = models.ForeignKey(Issue, models.DO_NOTHING)
    staff = models.ForeignKey(Staff, models.DO_NOTHING)
    return_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'submissions'


class WorkingSchedule(models.Model):
    day_name = models.CharField(primary_key=True, max_length=9)
    staff = models.ForeignKey(Staff, models.DO_NOTHING)
    staff_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'working_schedule'
