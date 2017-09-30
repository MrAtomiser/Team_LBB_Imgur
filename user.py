import datetime
from comment import Comment
from reply   import Reply
from image   import Image
from image_gallery import ImageGallery

class User():
  def __init__(self, username, password, date_created, profile_image, my_images = []):
    self.username = username
    self. password = password
    self.date_created = date_created
    self.profile_image = profile_image
    self.my_images = my_images


  def create_image(self):
    title = input("What's the image title? ")
    description = input("what the description? ")
    tags = input("What are the tags? ")
    image_gallery_id = input("What gallery? ")
    score = input("Score it: ")
    new_image = Image(title,description,tags,image_gallery_id,score)
    self.my_images.append(new_image)

  def read_images(self):
    for image in self.my_images:
      print(image)






sadiq = User(username = "sadiq", password = "password", date_created="", profile_image="sadiqimage",my_images = [])
tomi = User(username = "tomi", password = "password", date_created="", profile_image="tomiimage",my_images = [])
abdul = User(username = "abdul", password = "password", date_created="", profile_image="abdulimage",my_images = [])
dare = User(username = "dare", password = "password", date_created="", profile_image="dareimage",my_images = [])
charles = User(username = "charles", password = "password", date_created="", profile_image="charlesimage",my_images = [])

sadiq.create_image()
sadiq.read_images()

