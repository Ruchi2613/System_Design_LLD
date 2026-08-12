# │   [ Post ]  ───> Text, Image URLs, Timestamp, ID            │


class Post:
    def __init__(self, post_id: str, user_id: str, image_url: str, text: str = MediaType.TEXT, created_at: str = None):
        self.post_id = post_id
        self.user_id = user_id
        self.image_url = image_url
        self.text = text
        self.timestamp = datetime.now()
        self.created_at = created_at


    def get_post_id(self):
        return self.post_id

    def get_user_id(self):
        return self.user_id
    
    def get_image_url(self):
        return self.image_url
    
    def get_text(self):
        return self.text
    
    def get_timestamp(self):
        return self.timestamp
    
    def get_created_at(self):
        return self.created_at

