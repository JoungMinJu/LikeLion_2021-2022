from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=200)
    writer=models.ForeignKey(User,on_delete=models.CASCADE)
    pub_date=models.DateTimeField()
    body=models.TextField()
    image=models.ImageField(upload_to='post/',blank=True, null=True)
    like_user_set=models.ManyToManyField(User, blank=True, related_name='likes_user_set', through='Like')
    dislike_user_set=models.ManyToManyField(User, blank=True, related_name='dislike_user_set',through='Dislike')

    def __str__(self):
        return self.title #입력한 데이터가 호출되면 제목이 대표값으로 나오게 한다.

    def summary(self):
        return self.body[:20]
    
    @property
    def like_count(self):
        return self.like_user_set.count()
    @property
    def dislike_count(self):
        return self.dislike_user_set.count()


class Comment(models.Model):
	content = models.TextField()
	writer = models.ForeignKey(User, on_delete=models.CASCADE)
	post= models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

class Like(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True) #모델이 최초 저장시에 현재날짜로 저장
    updated_at=models.DateTimeField(auto_now=True) #모델이 save될 떄마다 현재날짜로 갱신
    class Meta:
        unique_together=(('user','post'))
class Dislike(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    class Meta:
        unique_together=(('user','post'))
