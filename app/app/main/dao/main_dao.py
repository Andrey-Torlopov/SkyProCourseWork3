from app.main.dao.main_post import MainPost
from app.tools.helpers import load_array_of_dictionary
from app.main.dao.main_post import MainPost


def foo():
    a = load_array_of_dictionary('./static/data/posts.json')

class MainDAO(object):

    def load_posts(self):
        posts_array = load_array_of_dictionary('./static/data/posts.json')
        bookmarks_array = load_array_of_dictionary('./static/data/bookmarks.json')
        
        result = list(map(lambda x: self.make_post_from_dict(x, bookmarks_array) ,posts_array))
        
        comments_array = load_array_of_dictionary('./static/data/comments.json')
        comments_count_dict = self.calculate_comments_count(comments_array)
        for item in result:
            try:
                count = comments_count_dict[item.pk]
                item.comments_count_string = f'Количество комментариев: {count}'
            except:
                pass
        return result
    
    # Helpers
    
    def make_post_from_dict(self, dict, bookmarks) -> MainPost:
        is_bookmark = int(dict["pk"]) in bookmarks
        return MainPost(dict["pk"], dict["poster_name"], dict["poster_avatar"], dict["pic"], dict["content"][:50], dict["views_count"], "Нет комментариев", is_bookmark)
    
    def calculate_comments_count(self, comments):
        result = dict()
        for item in comments:
            try:
                result[item["post_id"]] = result[item["post_id"]] + 1
            except:
                result[item["post_id"]] = 1
        return result
            