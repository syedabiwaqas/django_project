# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models




class Author(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    createdat = models.DateTimeField(db_column='createdAt',auto_now_add=True)  

    class Meta:
        managed = True
        db_table = 'author'


class Books(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    author = models.ForeignKey( Author,models.DO_NOTHING)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    quantity = models.IntegerField(blank=True, null=True)
    pulished_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'books'

