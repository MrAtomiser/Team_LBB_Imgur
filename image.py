class Image():
  def __init__(self,title, description, tags, image_gallery_id, score):
    self.title = title
    self.description = description
    self.tags = tags
    self.image_gallery_id = image_gallery_id
    self.score = score

    print("Image: {} successfully uploaded".format(title))






