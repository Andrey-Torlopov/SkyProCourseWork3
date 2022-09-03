from dataclasses import dataclass
from app.models.comment import Comment

@dataclass(slots=True, order=True)
class Post(object):
    pk: int
    poster_name: str
    poster_avatar: str    
    pic: str
    content: str
    views_count: int
    is_bookmark: bool
    comments: list
    
    @property
    def comments_dict(self):
        return list(map(lambda x: x.get_dict, self.comments))
    
    @property
    def comments_count(self):
        return len(self.comments)
    
    @property
    def comments_count_string(self):
        if self.comments_count == 0:
            return 'Нет комментариев'
        
        return f'Количество комментариев: {len(self.comments)}'
        
    @property
    def get_dict(self):
        return {"pk": self.pk,
                "name": self.poster_name,
                "avatar": self.poster_avatar, 
                "pic": self.pic,
                "content": self.content,
                "views": self.views_count,
                "comments_count_string": self.comments_count_string,
                "is_bookmark": self.is_bookmark,
                "comments": self.comments_dict,
                "comments_count": self.comments_count}
        
    @property
    def get_dict_short_text(self):
        return {"pk": self.pk,
                "name": self.poster_name,
                "avatar": self.poster_avatar, 
                "pic": self.pic,
                "content": self.content[:50],
                "views": self.views_count,
                "comments_count_string": self.comments_count_string,
                "is_bookmark": self.is_bookmark,
                "comments": self.comments_dict,
                "comments_count": self.comments_count}