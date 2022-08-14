from post import Post
title = "Great things"
body = "I have many great things to say"
post = Post(title, body)
post.addComment("You really are as great as you think you are!")
post.addComment("You suck!")
post.print()
