# Author: Bharath Parameswaran

from instapy import InstaPy
from instapy import smart_run

# login credentials
insta_username = 'shakahaar1'
insta_password = 'LaLaLand@1993X'

# for each post, the following criteria determine if the post will be liked and the owner, followed
user_potency_ratio = -0.33 # potency_ratio = -1 * following/followers. measure of whether the user follows their followers
user_max_followers = 4000
user_min_followers = 500
user_min_posts = 10
post_min_existing_likes=40
post_max_existing_likes=250

# comment settings
enable_comments=True
# list of comments. a comment will be chosen randomly
comments = ['Nice shot! @{}',
        'I love your profile! @{}',
        'Your feed is an inspiration :thumbsup:',
        'Just incredible :open_mouth:',
        'Looks awesome @{}!',
        'Getting inspired by you @{}!',
        ':raised_hands: Yes!']

# hashtags to search
hashtags = ['vegancupcakes', 'veganbrownies', 'vegandessert',
			'dairyfree', 'plantbased', 'whatveganseat',
			'thefeedfeedvegan', 'veganfoodspot', 'vegancommunity']

# number of images to checkout from the above hashtags (NOTE: This isn't the total number of posts that will be liked)
images_to_checkout = 50

#-------------------------Do not edit anything below this line----------------------------#

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
	potency_ratio=user_potency_ratio,
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
  session.set_do_comment(enabled=enable_comments, percentage=100)
  session.set_comments(comments, media='Photo')
  session.set_user_interact(amount=3, randomize=True, percentage=100, media='Photo')
  session.set_do_follow(enabled=True, percentage=100, times=1)
  # activity
  # 1. like posts from hashtags, comment and follows the user
  session.like_by_tags(hashtags, amount=images_to_checkout, skip_top_posts=False, randomize=True)
  # 2. unfollow nonfollowers 
  session.unfollow_users(amount=20, instapy_followed_enabled=True, instapy_followed_param="nonfollowers", style="FIFO", unfollow_after=48*60*60, sleep_delay=300)
  session.end()

 
  
  