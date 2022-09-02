from app.models.post import Post
from app.models.comment import Comment
from app.tools.helpers import load_array_of_dictionary

class AppDAO(object):
    '''Main DAO object'''
    
    def load_posts(self):
        posts_array = load_array_of_dictionary('./static/data/posts.json')
        bookmarks_array = load_array_of_dictionary('./static/data/bookmarks.json')
        
        result = list(map(lambda x: self._make_post_from_dict(x, bookmarks_array) ,posts_array))
                
        comments_array = load_array_of_dictionary('./static/data/comments.json')
        
        comments_dictionary = self.prepeare_comments(comments_array)
        
        for item in result:
            try:
                item.comments = comments_dictionary[item.pk]
            except Exception:
                item.comments = list()
               
        return result
    
    # Helpers
    
    def _make_post_from_dict(self, dict, bookmarks):
        is_bookmark = int(dict["pk"]) in bookmarks
        return Post(
            dict["pk"], 
            dict["poster_name"], 
            dict["poster_avatar"], 
            dict["pic"], 
            dict["content"], 
            dict["views_count"],
            is_bookmark,
            None)
    
    def _make_comment_from_dict(self, dict) -> Comment:
        return Comment(
            dict["pk"],
            dict["post_id"],
            dict["commenter_name"], 
            dict["comment"])
    
    def prepeare_comments(self, comments) -> dict():
        result = dict()
        comments_list = list(map(lambda x: self._make_comment_from_dict(x), comments))
        for comment in comments_list:
            try:
                items = result[comment.post_id]
                items.append(comment)
            except Exception:
                result[comment.post_id] = [comment]                
        
        return result