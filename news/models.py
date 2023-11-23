from django.db import models
from .manager import BaseModel

# Create your models here.


class Category(BaseModel):
    
    name = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.name
    

class Tags(BaseModel):
    
    name = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.name
    

class News(BaseModel):
    title = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    body = models.TextField()
    img = models.ImageField(upload_to="news")
    video = models.FileField(upload_to="videos", null=True, blank=True)
    view_count = models.BigIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="news_category")
    tags = models.ManyToManyField(Tags, related_name='news_tag')
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE, related_name="news_user")
    is_avtive = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return self.title
    
    