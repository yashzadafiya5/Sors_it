from django.db import models
from PIL import Image
from ckeditor_uploader.fields import RichTextUploadingField 
from django.urls import reverse
from django.template.defaultfilters import slugify 

# Create your models here.

class Blog(models.Model):
    main_image=models.ImageField(upload_to='blog_images')
    title=models.CharField(max_length=180)
    description=RichTextUploadingField()
    publish_date=models.DateField()
    slug = models.SlugField(null=False, unique=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

        img = Image.open(self.main_image.path)
        width, height = img.size
        new_height = int(width * 9 / 16)
        img = img.resize((width, new_height), Image.ANTIALIAS)
        img.save(self.main_image.path)
        
    def get_absolute_url(self):
        return reverse('blog_home:blog detail', kwargs={"slug": self.slug})
    

