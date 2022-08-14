class Post:
  def __init__(self, title, body):
    self.body = body
    self.title = title
    self.comments = []

  def print(self):
    print(self.title)
    print(self.body)
    print("Comments:")
    print("\n".join(self.comments))

  def addComment(self, passed_comment):
    comment = Comment(passed_comment)
    self.comments.append(comment)