
import uuid

class PostService:
    def __init__(self):
        self.post_local_db = {}
        self.local_like_db = {}
        self.local_dislike_db = {}

    def create_post(self, UID, content, title, desc, tag, created_at=None):
        if not UID or not content or not title or not desc or not tag:
            raise ValueError("All fields are required.")

        post_id = str(uuid.uuid4())
        self.post_local_db[post_id] = {
            "UID": UID,
            "content": content,
            "title": title,
            "desc": desc,
            "tag": tag,
            "created_at": created_at,
            "post_id": post_id
        }

        self.local_like_db[post_id]= set()
        self.local_dislike_db[post_id]= set()

        print("Post created successfully.")
        return True


    def view_post(self, post_id, UID):
        if post_id not in self.post_local_db:
            raise ValueError("Post ID does not exist.")

        obj_post = self.post_local_db[post_id]
        if obj_post["UID"] != UID:
            raise ValueError("Unauthorized: You are not allowed to view this post.")

        return obj_post


    def get_posts_by_user(self, target_UID):
        all_posts_target_user = []

        for post_id, post_data in self.post_local_db.items():
            if post_data["UID"] == target_UID:
                all_posts_target_user.append(post_data)

        return all_posts_target_user

    def view_all_posts(self):
        return list(self.post_local_db.values())

    def like_post(self, post_id, UID):
        # check if post not exist
        if post_id not in self.post_local_db:
            raise ValueError("Post ID does not exist.")


        # check if uid has already like the post
        if UID in self.local_like_db[post_id]:
            raise ValueError("You already liked this post") 
        
        # check if user has disliked the post
        if UID in self.local_dislike_db[post_id]:
            self.local_dislike_db[post_id].remove(UID)

        self.local_like_db[post_id].add(UID)
        return "You liked this post."
            
    def dislike_post(self, post_id, UID):
        if post_id not in self.post_local_db:
            raise ValueError("Post ID does not exist.")

        # check if uid has already dislike the post
        if UID in self.local_dislike_db[post_id]:
            raise ValueError("You already disliked this post") 
        
        # check if user has disliked the post
        if UID in self.local_like_db[post_id]:
            self.local_like_db[post_id].remove(UID)

        self.local_dislike_db[post_id].add(UID)
        return "You liked this post."