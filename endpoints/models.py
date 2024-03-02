from django.db import models

"""
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.


# Create your models here.
class Account(models.Model):
    email = models.CharField(primary_key=True, max_length=255)
    account_type = models.CharField(max_length=5, blank=True, null=True)
    password = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'account'


class Admin(models.Model):
    pdf_book_sales = models.IntegerField(blank=True, null=True)
    pdf_books_count = models.IntegerField(blank=True, null=True)
    publications_count = models.IntegerField(blank=True, null=True)
    publications_sales = models.IntegerField(blank=True, null=True)
    ramayana_files_count = models.IntegerField(blank=True, null=True)
    users_count = models.IntegerField(blank=True, null=True)
    account_email = models.OneToOneField(Account, models.DO_NOTHING, db_column='account_email', primary_key=True)

    class Meta:
        managed = False
        db_table = 'admin'


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


class AuthtokenToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    created = models.DateTimeField()
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'authtoken_token'


class Category(models.Model):
    id = models.BigAutoField(primary_key=True)
    category_name = models.CharField(max_length=255, blank=True, null=True)
    image_path = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category'


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


class File(models.Model):
    id = models.BigAutoField(primary_key=True)
    file_name = models.CharField(max_length=255, blank=True, null=True)
    file_path = models.CharField(max_length=255, blank=True, null=True)
    file_type = models.CharField(max_length=255, blank=True, null=True)
    upload_date = models.DateField(blank=True, null=True)
    sub_sub_category = models.ForeignKey('SubSubCategory', models.DO_NOTHING, blank=True, null=True)
    file = models.ForeignKey('Orders', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'file'


class Gallery(models.Model):
    id = models.BigAutoField(primary_key=True)
    image_path = models.CharField(max_length=255, blank=True, null=True)
    no_of_times_opened = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gallery'


class Orders(models.Model):
    id = models.BigAutoField(primary_key=True)
    amount = models.FloatField(blank=True, null=True)
    user_email = models.ForeignKey('User', models.DO_NOTHING, db_column='user_email', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orders'


class Pdfbook(models.Model):
    id = models.BigAutoField(primary_key=True)
    amount = models.FloatField(blank=True, null=True)
    author_name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    pdf_file_path = models.CharField(max_length=255, blank=True, null=True)
    pdf_image_path = models.CharField(max_length=255, blank=True, null=True)
    pdf_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pdfbook'


class Publication(models.Model):
    id = models.BigAutoField(primary_key=True)
    amount = models.FloatField(blank=True, null=True)
    author_name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    edited_by = models.CharField(max_length=255, blank=True, null=True)
    number_of_pages = models.IntegerField(blank=True, null=True)
    publication_name = models.CharField(max_length=255, blank=True, null=True)
    year_of_publication = models.IntegerField(blank=True, null=True)
    publication = models.ForeignKey(Orders, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'publication'


class SubCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    image_path = models.CharField(max_length=255, blank=True, null=True)
    sub_category_name = models.CharField(max_length=255, blank=True, null=True)
    category = models.ForeignKey(Category, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sub_category'


class SubSubCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    image_path = models.CharField(max_length=255, blank=True, null=True)
    sub_sub_category_name = models.CharField(max_length=255, blank=True, null=True)
    sub_category = models.ForeignKey(SubCategory, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sub_sub_category'


class User(models.Model):
    address_line1 = models.CharField(max_length=255, blank=True, null=True)
    address_line2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    mobile_no = models.CharField(max_length=255, blank=True, null=True)
    pincode = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    account_email = models.OneToOneField(Account, models.DO_NOTHING, db_column='account_email', primary_key=True)

    class Meta:
        managed = False
        db_table = 'user'
"""


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    image_url = models.CharField(max_length=500, default='/no-url')  # s3 object link

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=3)  # null=True only for debugging
    image_url = models.CharField(max_length=500, default='/no-url')  # s3 object link

    def __str__(self):
        return self.name


class SubSubCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, default=9)  # null=True only for debugging
    image_url = models.CharField(max_length=500, default='/no-image-url')  # s3 object link to image
    document_url = models.CharField(max_length=500, default='/no-doc-url') # s3 object link to document

    def __str__(self):
        return self.name
