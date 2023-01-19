from django.db import models
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class post(models.Model):
    title=models.CharField(max_length=200,unique=True)
    slug=models.SlugField(max_length=200,unique=True)
    content=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)
    status=models.IntegerField(choices=STATUS,default=0)
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
