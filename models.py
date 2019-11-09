from django.db import models

# Create your models here.

class Type(models.Model):

	name = models.CharField('Nome', max_length=100)
	slug = models.SlugField('Identificador', max_length=100)

	created = models.DateTimeField('Criado em', auto_now_add=True)
	modified = models.DateTimeField('Modificado em', auto_now=True)

	class Meta:
		verbose_name = 'Tipo'
		verbose_name_plural = 'Tipos'
		ordering = ['name']

	def __str__(self):
		return self.name

class Product(models.Model):

	name = models.CharField('Nome', max_length=100)
	slug = models.SlugField('Identificador', max_length=100)
	tipo = models.ForeignKey('catalog.Type', verbose_name='Tipo', on_delete='cascade')
	price = models.DecimalField('Preço', decimal_places=2, max_digits=5)
	description = models.TextField('Descrição', blank=True)
	producer = models.ForeignKey('catalog.Producer', verbose_name='Produtora', on_delete='cascade')
	quant = models.IntegerField('Quantidade')
	medida = models.CharField('Medida', max_length=5)

	created = models.DateTimeField('Criado em', auto_now_add=True)
	modified = models.DateTimeField('Modificado em', auto_now=True)
	
	class Meta:
		verbose_name = 'Produto'
		verbose_name_plural = 'Produtos'
		ordering = ['name']

	def __str__(self):
		return self.name

class Producer(models.Model):

	name = models.CharField('Nome', max_length=100)
	slug = models.SlugField('Identificador', max_length=100)
	region = models.CharField('Região', max_length=100)

	created = models.DateTimeField('Criado em', auto_now_add=True)
	modified = models.DateTimeField('Modificado em', auto_now=True)

	class Meta:
		verbose_name = 'Produtora'
		verbose_name_plural = 'Produtoras'
		ordering = ['name']

	def __str__(self):
		return self.name