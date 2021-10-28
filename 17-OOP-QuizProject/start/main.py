# How do we create a class
class User:
    def __init__(self,user_id,username):
        print("New user being created...")
        self.id = user_id
        self.username = username 
        self.followers = 0
        self.following = 0

    def follow(self,user):
        self.following += 1
        user.followers += 1

# Now the class is created, we can create an object assiginng it to a variable
user_01 = User("001","Angela")
user_02 = User("002","Berto")

user_02.follow(user_01)
print(user_01.followers)

