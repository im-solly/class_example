class Post:
    def __init__(self, author, content):
        self.author = author
        self.content = content
        self.shared_users = []
        self.is_private = False

    def share(self, user):
        self.shared_users.append(user)
        

class PrivatePost(Post):
    def __init__(self, author, content):
        #super().__init__()과 직접 self.* = * 해주는 것의 차이: super().을 해주지 않으면, shared_users와 같은 attribute들이 초기화되지 않아 에러가 발생할 수 있다.
        super().__init__(author, content)
#        self.author = author
#        self.content = content
        self.is_private = True
    
    # share 메소드를 호출 시 TypeError를 발생시킵니다.
    def share(self):
        super().share(self.author) #여기를 self.author로 해야할지, author로 해야할지? -> self.author로 해야한다.
#        raise TypeError("이 게시물은 private 게시물입니다.")


post1 = PrivatePost("sol", "hi")
post2 = PrivatePost("mommy", "hi2")
post1.share()
post2.share()

print(post2.shared_users)