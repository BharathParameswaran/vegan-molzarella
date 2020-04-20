# Author: Bharath Parameswaran

from instapy import InstaPy
from instapy import smart_run
import sys

if len(sys.argv) != 3:
  print("Incorrect arguments. Usage: python main.py username password")
  exit()

# login credentials
insta_username = sys.argv[1]
insta_password = sys.argv[2]

# for each post, the following criteria determine if the post will be liked and the owner, followed
user_min_potency_ratio = 0.20 # potency_ratio = following/followers. measure of whether the user follows their followers
user_max_followers = 3000
user_min_followers = 300
user_min_posts = 10
post_min_existing_likes=40
post_max_existing_likes=400

# comment settings
enable_comments=True
# list of comments. a comment will be chosen randomly
comments = ['Nice shot! @{}',
        'I love your profile! @{}',
        'Your feed is an inspiration :thumbsup:',
        'This looks great! :D We also make easy vegan recipes, check us out :)',
		'WoW :O. Love your feed, very similar to mine :)',
		'Love the plating! Will use some of you ideas for my next plate :D',
		'Looks delicious. I also make vegan recipes quarantine simple :D. Check out my feed too!',
        'Just incredible :open_mouth:',
        'Looks awesome @{}!',
        'Getting inspired by you @{}!',
        ':raised_hands: Yes!']

# hashtags to search
hashtags = ['vegancupcakes', 'veganbrownies', 'vegandessert',
			'dairyfree', 'plantbased', 'whatveganseat',
			'thefeedfeedvegan', 'veganfoodspot', 'vegancommunity', 
			'instavegan', 'instaveganfood']

# number of posts to checkout from each of the above hashtags 
posts_to_checkout = 5

# randomly `like` other posts in the user's profile before following them. This might encourage them to follow you but would increase the script running time
interact_with_user = True
posts_to_interact_with = 2 # recommended value 1-3. Only relevant if interact_with_user is True


#-------------------------Do not edit below this line----------------------------#

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(
	username=insta_username,
	password=insta_password,
	want_check_browser=False,
	disable_image_load=True,
	headless_browser=False)

with smart_run(session):
  # general settings		
  session.set_skip_users(
  	skip_private=True,
	private_percentage=100,
	skip_no_profile_pic=True,
	no_profile_pic_percentage=100,
	skip_business=False,
	skip_non_business=False,
	business_percentage=0,
	skip_business_categories=[],
	dont_skip_business_categories=[])

  session.set_relationship_bounds(
	enabled=True,
	potency_ratio=-1 * user_min_potency_ratio,
	delimit_by_numbers=True,
	max_followers=user_max_followers,
	min_followers=user_min_followers,
	min_posts=user_min_posts)

  session.set_action_delays(
	enabled=True,
	like=5,
	comment=5,
	follow=5,
	unfollow=5,
	story=10)

  session.set_delimit_liking(enabled=True, max_likes=post_max_existing_likes, min_likes=post_min_existing_likes)		
  session.set_do_like(enabled=True, percentage=100)
  session.set_do_comment(enabled=enable_comments, percentage=50)
  session.set_comments(comments, media='Photo')
  session.set_user_interact(amount=posts_to_interact_with, randomize=True, percentage=100, media='Photo')
  session.set_mandatory_words(['#vegan', 'vegan', 'VEGAN', 'cooking', 'food'])
  # activity
  # 1. follow users based on tags and like their posts 
  session.follow_by_tags(hashtags, amount=posts_to_checkout, skip_top_posts=False, randomize=True, interact=interact_with_user)
  # 2. unfollow nonfollowers 
  session.unfollow_users(amount=20, instapy_followed_enabled=True, instapy_followed_param="nonfollowers", style="FIFO", unfollow_after=48*60*60, sleep_delay=300)
  session.end()

 
  
  