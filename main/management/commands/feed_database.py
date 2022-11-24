from django.core.management.base import BaseCommand
from main.models import Post
from django.contrib.auth.models import User
from django.conf import settings

import json
import os

class Command(BaseCommand):
    def handle(self, **options):
        # Create superuser
        User.objects.create_superuser(username="1", email="", password="1")

        # Getting posts from file
        file_data = open(os.path.join(settings.BASE_DIR, 'data.json'))   
        post_data_json = json.load(file_data) # deserialises it

        # Saving posts
        for post_data in post_data_json:
            url_watch = post_data["url"] 
            url_embed = post_data["url"].replace("watch?v=", "embed/")
            post = Post(title=post_data["title"], url=url_embed)
            post.save()

