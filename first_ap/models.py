
from django.db import models
from django.shortcuts import reverse
from first_ap.utils import unique_slug_generator
from django.db.models.signals import pre_save, post_save
from django_project import settings


def update_image_name(fielpath):
	base_name = os.path.basename(fielpath)
	name, ext = os.path.splitext(base_name)
	return name, ext

def upload_image_path(instance, filename):
	new_filename = random.randint(1,986987)
	name, ext = update_image_name(filename)
	final_filename = f'{new_filename}{ext}'
	return f'products/{new_filename}/{final_filename}'

	

class First_A(models.Model):
	name = models.CharField(max_length=100, null=True, blank=True)
	age = models.IntegerField(null=True, blank=True)
	slug = models.SlugField(unique=True, blank=True)
	
	def __str__(self):
		return self.name
	
	@property
	def title(self):
		return self.name

	def get_absolute_url(self):
		return reverse('first_ap:first_a_detail', kwargs={'slug':self.slug})
		
def pre_slug_field(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)

pre_save.connect(pre_slug_field, sender=First_A)