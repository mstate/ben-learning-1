from datetime import datetime

class Comment:
  def __init__(comment_body):
    self.body = comment_body
    self.created_at = datetime.now()
