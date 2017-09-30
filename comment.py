import datetime



class Comment():
  def __init__(user, date_created, image_id, text, score):
    self.user = user
    self.date_created = date_created
    self.image_id = image_id
    self.text = text
    self.score = score

  
