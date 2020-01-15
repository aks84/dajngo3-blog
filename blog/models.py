from django.db import models

class Author(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField()
	bio = models.TextField()

	def __str__(seft):
		return seft.name

class Category(models.Model):
	category = models.CharField(max_length=100)
	description = models.TextField()


	def __str__(seft):
		return seft.category


class Article(models.Model):
	title = models.CharField(max_length=250)
	image = models.ImageField(upload_to="static/images/")
	content = models.TextField()
	author = models.ForeignKey(Author, on_delete=models.CASCADE)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)

	def __str__(seft):
		return seft.title

