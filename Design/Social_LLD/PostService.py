import uuid
from datetime import datetime
from collections import defaultdict

# Assume these are imported from your lightweight data models / enums:
# from PostData import PostData
# from Comment import Comment
# from media_type import MediaType
# from FriendshipService import FriendshipService


class PostService:
    def __init__(self, friendship_service):
        self.friendship_service = friendship_service
        
        # Storage dictionaries
        self.posts_by_id = {}                 # { post_id: PostData }
        self.user_posts = defaultdict(list)    # { user_id: [post_id, ...] }
        self.post_likes = defaultdict(set)     # { post_id: set(user_id) }
        self.post_comments = defaultdict(list) # { post_id: [Comment, ...] }

    # -------------------------------------------------------------
    # 1. CREATE POST
    # -------------------------------------------------------------
    def create_post(self, author_id: str, content: str, media_url: str = None, media_type = None) -> str:
        if not content and not media_url:
            raise ValueError("A post must contain text content or a media file.")

        post_id = str(uuid.uuid4())
        
        # Create new post object
        # Note: If your PostData constructor auto-generates post_id or timestamp, adjust accordingly.
        new_post = PostData(
            post_id=post_id,
            author_id=author_id,
            content=content,
            media_url=media_url,
            media_type=media_type,
            created_at=datetime.now()
        )

        # Store in storage maps
        self.posts_by_id[post_id] = new_post
        self.user_posts[author_id].append(post_id)

        print(f"Post {post_id} created by user {author_id}.")
        return post_id

    # -------------------------------------------------------------
    # 2. LIKE / UNLIKE POST
    # -------------------------------------------------------------
    def toggle_like(self, post_id: str, user_id: str) -> bool:
        if post_id not in self.posts_by_id:
            raise ValueError("Post not found.")

        # If user already liked the post, remove like (unlike)
        if user_id in self.post_likes[post_id]:
            self.post_likes[post_id].remove(user_id)
            print(f"User {user_id} unliked post {post_id}.")
            return False  # Status: Not liked
        else:
            self.post_likes[post_id].add(user_id)
            print(f"User {user_id} liked post {post_id}.")
            return True   # Status: Liked

    def get_like_count(self, post_id: str) -> int:
        return len(self.post_likes[post_id])

    # -------------------------------------------------------------
    # 3. ADD COMMENT
    # -------------------------------------------------------------
    def add_comment(self, post_id: str, author_id: str, text: str) -> Comment:
        if post_id not in self.posts_by_id:
            raise ValueError("Post not found.")

        if not text.strip():
            raise ValueError("Comment text cannot be empty.")

        comment_id = str(uuid.uuid4())
        
        # Create new Comment entity
        new_comment = Comment(
            comment_id=comment_id,
            post_id=post_id,
            author_id=author_id,
            text=text,
            created_at=datetime.now()
        )

        self.post_comments[post_id].append(new_comment)
        print(f"Comment added to post {post_id} by user {author_id}.")
        return new_comment

    def get_comments(self, post_id: str) -> list:
        return self.post_comments[post_id]

    # -------------------------------------------------------------
    # 4. GENERATE NEWSFEED
    # -------------------------------------------------------------
    def generate_newsfeed(self, user_id: str, limit: int = 20) -> list:
        """
        Retrieves recent posts from the user and all their friends,
        sorted chronologically (newest first).
        """
        # Step A: Get list of all friends for this user
        friends_list = self.friendship_service.get_friends_list(user_id)
        
        # Include the user's own ID so their own posts show up on their feed too
        feed_user_ids = friends_list + [user_id]

        # Step B: Gather all post_ids published by these users
        all_feed_posts = []
        for fid in feed_user_ids:
            for pid in self.user_posts[fid]:
                all_feed_posts.append(self.posts_by_id[pid])

        # Step C: Sort posts by created_at descending (newest first)
        all_feed_posts.sort(key=lambda post: post.created_at, reverse=True)

        # Step D: Return up to the requested limit
        return all_feed_posts[:limit]