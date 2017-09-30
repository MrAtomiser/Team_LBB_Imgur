import datetime
from comment import Comment
from reply   import Reply
from image   import Image
from image_gallery import ImageGallery

class User():
  def __init__(self, username, password, date_created, profile_image):
    self.username = username
    self. password = password
    self.date_created = date_created
    self.profile_image = profile_image

  def create_image(self):
    user_id = input("Who's uploading the image? ")
    title = input("What's the image title? ")
    description = input("what the description? ")
    tags = input("What are teh tags? ")
    image_gallery_id = input("What gallery? ")
    score = input("Score it")
    new_image = Image(user_id,title,description,tags,image_gallery_id,score)




sadiq = User(username = "sadiq", password = "password", date_created="", profile_image="sadiqimage")
tomi = User(username = "tomi", password = "password", date_created="", profile_image="tomiimage")
abdul = User(username = "abdul", password = "password", date_created="", profile_image="abdulimage")
dare = User(username = "dare", password = "password", date_created="", profile_image="dareimage")
charles = User(username = "charles", password = "password", date_created="", profile_image="charlesimage")

sadiq.create_image()
