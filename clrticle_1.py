class Review:
    title = ''
    content = ''
    user = ''
    
    def __init__(self, content=content,title=title,user=user):
        self.content = content
        self.title = title
        self.user = user
        
        
review1 = Review(title="인생영화입니다.", content="아무래도 이 영화는 좋아요", user="김철수")
review2 = Review(title="아무래도 이 영화는 좋아요", content="아무래도 이 영화는 좋아요", user="김철수")
review3 = Review(title="아무래도 이 영화는 좋아요", content="아무래도 이 영화는 좋아요", user="김철수")

print(review1.title,review1.content,review1.user)
print(review2.title,review2.content,review2.user)

