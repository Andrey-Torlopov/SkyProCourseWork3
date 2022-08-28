from dataclasses import dataclass

@dataclass(slots=True, order=True)
class MainPost(object):
    pk: int
    poster_name: str
    poster_avatar: str    
    pic: str
    content: str
    views_count: int
    comments_count_string: str
    is_bookmark: bool
    
    @property
    def get_dict(self):
        return {"pk": self.pk,
                "name": self.poster_name,
                "avatar": self.poster_avatar, 
                "pic": self.pic,
                "content": self.content,
                "views": self.views_count,
                "comments": self.comments_count_string,
                "is_bookmark": self.is_bookmark
                }