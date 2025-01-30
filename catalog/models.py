from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

def rename_image(instance, filename):
    """It is used to rename a uploaded image."""

    image_name = str(datetime.now().time()).replace(':', '')
    image_name = image_name.replace('.', '')
    ext = filename.split('.')[-1]
    if instance.pk:
        return f'product/{image_name}_{instance.pk}.{ext}'
    else:
        return f'product/{image_name}.{ext}'



class Category(models.Model):
    """This is the Category Django Model for the pim_category database table."""

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250)
    category_group_id = models.IntegerField(default=0)
    # include_in_menu = models.BooleanField(default=False)
    parent = models.ForeignKey('self',
                               on_delete=models.CASCADE,
                               related_name='children',
                               db_column='parent_id',
                               null=True,
                               blank=True)
    # is_active = models.BooleanField(default=False)
    # is_deleted = models.BooleanField(default=False)
    # is_featured = models.BooleanField(default=False)
    image_url = CloudinaryField('category', null=True, blank=True)
    image_alt_tag = models.CharField(max_length=160, null=True, blank=True)
    image_title = models.CharField(max_length=160, null=True, blank=True)
    canonical_url = models.CharField(max_length=500, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,
                                   on_delete=models.CASCADE,
                                   related_name='category_created',
                                   db_column='created_by')
    updated = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User,
                                   on_delete=models.CASCADE,
                                   related_name='category_updated',
                                   db_column='updated_by',
                                   null=True)

    def __str__(self):
        """Override string method and return custom data.
        
        Returns:
            str: It returns category name
        """

        return str(self.name)

    class Meta:
        """Provide database table name explicitly."""

        db_table = 'category'

class ProductBrand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250)
    image_url = CloudinaryField('brand', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,
                                      on_delete=models.CASCADE,
                                      related_name='brand_created',
                                      db_column='created_by')
    def __str__(self):
        """Override string method and return custom data.
        
        Returns:
            str: It returns category name
        """

        return str(self.name)
    class Meta:
        """Provide database table name explicitly."""

        db_table = 'product_brand'
    

class Product(models.Model):
    """This is the Product Django Model for the pim_product database table."""

    id = models.AutoField(primary_key=True)
    brand = models.ForeignKey(ProductBrand,
                              on_delete=models.CASCADE,
                              related_name='product_brand',
                              db_column='brand_id',
                              null=True,
                              blank=True)
    other_brand = models.CharField(max_length=250, null=True, blank=True)
    category = models.ForeignKey(Category,
                                on_delete=models.CASCADE,
                                related_name='pc_category',
                                null=True)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250)
    short_description = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    is_enabled = models.BooleanField(default=True)
    is_home_featured = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)
    approved_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,
                                   on_delete=models.CASCADE,
                                   related_name='product_created',
                                   db_column='created_by')
    updated = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User,
                                   on_delete=models.CASCADE,
                                   related_name='product_updated',
                                   db_column='updated_by',
                                   null=True, blank=True)

    @property
    def category_name(self):
        return self.category.name

    def __str__(self):
        """Override string method and return custom data.

        Returns:
            str: It returns product name
        """
        return str(self.name)

    class Meta:
        """Provide database table name explicitly."""

        db_table = 'product'


class ProductImages(models.Model):
    """This is the ProductImages Django Model for the product_images database table."""

    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name='product_image',
                                db_column='product_id')
    full_url = CloudinaryField('product_photos', null=True, blank=True)
    title = models.CharField(max_length=250, null=True, blank=True)
    caption = models.CharField(max_length=250, null=True, blank=True)
    order_by = models.IntegerField(default=0, null=True, blank=True) 
    is_enabled = models.BooleanField(default=True)
    is_default = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Override string method and return custom data.
        
        Returns:
            str: It returns image title
        """

        return str(self.title)

    class Meta:
        """Provide database table name explicitly."""

        db_table = 'product_images'


class ProductAttributes(models.Model):
    attribute_name = models.CharField(max_length=250, unique=True)
    is_default = models.BooleanField(default=False)

    def __str__(self):
        return self.attribute_name

    class Meta:
        db_table = 'product_attributes'
    

    
class ProductAttributeValue(models.Model):
    """This is the ProductPartAttributeValue Django Model for the 
    pim_product_attribute_value database table."""

    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product,
                                    on_delete=models.CASCADE,
                                    related_name='p_attr_val',
                                    db_column='product_id')
    attribute = models.ForeignKey(ProductAttributes,
                                  on_delete=models.CASCADE,
                                  related_name='pa_attr',
                                  db_column='attribute_id')
    attribute_value = models.CharField(max_length=200)

    order_no = models.IntegerField(default=1, null=True, blank=True)

    def __str__(self):
        """Override string method and return custom data.
        
        Returns:
            str: It returns attrinute name.
        """

        return str(self.attribute.attribute_name)

    class Meta:
        """Provide database table name explicitly."""

        db_table = 'product_attribute_value'

