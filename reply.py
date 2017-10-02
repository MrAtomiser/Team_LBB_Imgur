class Reply():
  def __init__(self,comment_id, date_created, text, user_id, score):
    self.comment_id = comment_id
    self.date_created = date_created
    self.text = text
    self.user_id = user_id
    self.score = score

  def get_reply(self):
      return self.replies

  def reply_exists(self,reply_itself):
      for replys in self.replies:
          if (replys.get_reply() == reply_itself):
              return replys
          return False

  def create_reply(self, get_reply):
      self.replies.append(get_reply)
      get_reply = input("You can reply to this post here: ")

  def update_reply(self, reply, updated_text):
      if reply in self.replies:
          text = updated_text
          print("New reply is: {}".format(updated_text))

  def delete_reply(self,reply):
      if reply in self.replies:
          self.replies.remove(reply)




