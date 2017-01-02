import vk_api
import random

PublID = -51016572 #enter your public id as a negative number
PostID = 726787 #enter target post id (from URL)
RepostsID = PublFollowersID = toWinners = []

vk_session = vk_api.VkApi()
try:
    vk_session.authorization()
except vk_api.AuthorizationError as error_msg:
    print(error_msg)
vk = vk_session.get_api()

PublFollowers = vk.groups.getMembers(group_id = -PublID)
Reposts = vk.wall.getReposts(owner_id = PublID, post_id = PostID, count = 1000)

for i in range(len(Reposts['profiles'])):
    RepostsID.append(Reposts['profiles'][i]['id'])
for i in range(len(PublFollowers['items'])):
    PublFollowersID.append(PublFollowers['items'][i])
for i in range(len(PublFollowersID)):
    for j in range(len(RepostsID)):
        if (RepostsID[j] == PublFollowersID[i]):
            toWinners.append(RepostsID[j])

random.seed
Winner = random.randint(0, len(toWinners) - 1)

print(toWinners[Winner])
