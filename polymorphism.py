class User:
    def __init__(self, name):
        self.name = name


class Post:
    def __init__(self, content):
        self.content = content
        self.reactions = []
        self.positive_reactions = 0
        self.negative_reactions = 0
        
        
class Reaction:
    # 아래 코드의 빈 부분을 완성합니다.
    def __init__(self, reaction_type, post, user):
        if reaction_type not in ["LIKE", "LOVE", "HAHA", "SAD", "ANGRY", "WOW"]:
            raise ValueError
        if not isinstance(post, Post):
            raise TypeError
        if not isinstance(user, User):
            raise TypeError
        
        self.reaction_type = reaction_type
        self.post = post
        self.user = user
        self.post.reactions.append(self)


# 아래 코드의 빈 부분을 완성합니다.
class Like(Reaction):
    def __init__(self, post, user):
        super().__init__("LIKE", post, user)
        post.positive_reactions += 1


class Angry(Reaction):
    # 아래 코드의 빈 부분을 완성합니다.
    def __init__(self, post, user):
        super().__init__("ANGRY", post, user)
        post.negative_reactions += 1


# User와 Post 클래스의 인스턴스를 생성합니다.
user1 = User("Alice")
user2 = User("Bob")
post = Post("Hello, world!")

# Like 반응을 추가합니다.
like_reaction = Like(post, user1)
print(f"Post '{post.content}'에 대한 긍정적 반응 수: {post.positive_reactions}")  # 예상: 1
print(f"Post '{post.content}'에 대한 부정적 반응 수: {post.negative_reactions}")  # 예상: 0

# Angry 반응을 추가합니다.
angry_reaction = Angry(post, user2)
print(f"Post '{post.content}'에 대한 긍정적 반응 수: {post.positive_reactions}")  # 예상: 1
print(f"Post '{post.content}'에 대한 부정적 반응 수: {post.negative_reactions}")  # 예상: 1

print(post.reactions[0].post)
print(post.reactions[0].content)
print(post.reactions[0].reaction_type)