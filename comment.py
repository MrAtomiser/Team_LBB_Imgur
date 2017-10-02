<<<<<<< HEAD
class Comment():
	def __init__(self, date_created, image_id, text, score):
	    self.date_created = date_created
	    self.image_id = image_id
	    self.text = text
	    self.score = score
    	
    	# print("New comment created by {}".format(self.user))
=======
# class Comment():
#   def __init__(self,user, date_created, image_id, text, score):
#     self.user = user
#     self.date_created = date_created
#     self.image_id = image_id
#     self.text = text
#     self.score = score

import time

class Comment:
  def __init__(self, message, sender_ID, points, post_ID,replies=[]):  # CommentID Needed?
    self.message = message
    self.timesent = time()
    self.sender_ID = sender_ID
    self.points = points
    self.post_ID = post_ID
    self.replies = replies

  def edit_comment(self, new_comment):
    self.new_comment = new_comment

  def vote_comment(self):
    pass

  def delete_comment(self):
    pass

  def send_comment(self):
    pass
>>>>>>> 97f4c4a35ab10fc9edf87396754e652e77676e70
