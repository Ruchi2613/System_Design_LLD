from AccountService import AccountService
from PostService import PostService

class Main:

    def main():
        print("----Backend Working----")

        # making obj for both the files to call there methods

        account_service_obj = AccountService()
        post_service_obj  = PostService()


        # STEP 1: USER REGISTRATION (SIGN UP)

        print("--- 1. Testing User Sign Up ---")

        account_service_obj.sign_up(
            un= 'Ruchi',
            password= 'abc1234567',
            confirm_password='abc1234567',
            email='ruchiap@gmail.com',
            phone_number="9876543210"
        )


        account_service_obj.sign_up(
                    un= 'Aditya',
                    password= 'abc678900',
                    confirm_password= 'abc678900',
                    email='aditya@gmail.com',
                    phone_number="9976543210"
                )

        account_service_obj.sign_up(
                            un= 'Parul',
                            password= 'abz678900',
                            confirm_password= 'abz678900',
                            email='parul@gmail.com',
                            phone_number="9996543210"
                        )
        print('Local DB (Users):',account_service_obj.local_db.keys())
        print('Values of User Ruchi:',account_service_obj.local_db['Ruchi'] )
        print('Values of User Aditya:',account_service_obj.local_db['Aditya'] )


        # STEP 2: Check USER SIGN IN
        account_service_obj.signIn('Ruchi','abc1234567' )

        # STEP 3: CREATE POSTS
        post1_id = post_service_obj.create_post(
        UID="Ruchi",
        content="Hello world! This is my first post.",
        title="Welcome Post",
        desc="Introductory post",
        tag="#tech",
        )

        post2_id = post_service_obj.create_post(
            UID="Aditya",
            content="Learning Python backend structures today!",
            title="Python Learning",
            desc="Coding updates",
            tag="#python",
        )

        
        post3_id = post_service_obj.create_post(
            UID="Parul",
            content="Good morning everyone!",
            title="Morning Post",
            desc="Daily update",
            tag="#life",
        )

        # STEP 4: VIEW POSTS
        print("\n--- 4. Fetching Ruchi's Profile Feed ---")

        ruchi_post = post_service_obj.get_posts_by_user('Ruchi')
        print(f"Ruchi has {len(ruchi_post)} posts:")
        for post in ruchi_post:
            print(post['content'],post['title'],post['desc'])

        aditya_post = post_service_obj.get_posts_by_user('Aditya')
        print(f"Aditya has {len(aditya_post)} posts:")
        for post in aditya_post:
            print(post['content'],post['title'],post['desc'])

        # STEP 5: LIKE & DISLIKE REACTIONS

        print("\n--- 5. Testing Reactions ---")
        liked_post_by_Aditya = post_service_obj.like_post(post1_id,'Aditya')
        print(f"Aditya liked Post: {liked_post_by_Aditya}")

        liked_post_by_Parul = post_service_obj.like_post(post1_id,'Parul')
        print(f"Parul liked Post: {liked_post_by_Parul}")


        print("DB of likes:",post_service_obj.local_like_db)
        '''
        DB of likes: 
        {'6a4ffb9f-8ac6-4447-a051-21630a192c92': {'Aditya'},
        '68ea9190-2a1f-45ce-9f9d-86d85625aa91': set(),
        '520a14b8-84b9-45c3-99a6-7dd54df61b12': set()}

        '''

    if __name__ == "__main__":
        main()
