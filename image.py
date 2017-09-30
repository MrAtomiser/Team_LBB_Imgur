class Image():
  def __init__(self,user_id, title, description, tags, image_gallery_id, score):
    self.user_id = user_id
    self.title = title
    self.description = description
    self.tags = tags
    self.image_gallery_id = image_gallery_id
    self.score = score

    print("Image:{} successfully uploaded by {}".format(title,user_id))

