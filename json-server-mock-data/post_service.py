# import 2 packages
import requests
import json

base_url = "http://localhost:3000"

def get_posts():
    response = requests.get(f"{base_url}/posts")
    return response.json()

# http://localhost:3000/posts?id=3
def get_post_by_id(post_id):
    response = requests.get(f"{base_url}/posts?id={post_id}")  
    return response.json()