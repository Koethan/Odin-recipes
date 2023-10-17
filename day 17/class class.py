from socket import IP_DEFAULT_MULTICAST_LOOP


# Instagram OOP example with names, ids, and follower counts

class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.followers = 0
        self.following = 0

    def follow(self, other_user):
        other_user.followers += 1
        self.following += 1

user1 = User("Ethan", "001")
user2 = User("Angela", "002")


print(user1.name)
print(user1.id)
print(user2.name)
print(user2.id)
print(user1.followers)
user1.follow(user2)
print(user1.following)
print(user2.followers)