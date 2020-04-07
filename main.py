# imports
from instapy import InstaPy
from instapy import smart_run

# login credentials
insta_username = ''
insta_password = ''

comments = ['Nice shot! @{}',
        'I love your profile! @{}',
        'Your feed is an inspiration :thumbsup:',
        'Just incredible :open_mouth:',
        'Looks awesome @{}',
        'Getting inspired by you @{}',
        ':raised_hands: Yes!']

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username='shakahaar1',
                  password='LaLaLand@1993X',
                  headless_browser=False)

with smart_run(session):	
  """ Activity flow """		
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
	potency_ratio=-0.5,
	delimit_by_numbers=True,
	max_followers=4000,
	min_followers=500,
	min_posts=10,

  session.set_action_delays(
	enabled=True,
	like=3,
	comment=5,
	follow=4.17,
	unfollow=28,
	story=10)

  session.set_delimit_liking(enabled=True, max_likes=250, min_likes=40)		
  session.set_do_comment(enabled=True, percentage=100)
  session.set_comments(comments, media='Photo')
  session.set_user_interact(amount=3, randomize=True, percentage=100, media='Photo')
  session.set_do_follow(enabled=True, percentage=100, times=1)
  # activity		
  session.like_by_tags(["veganbrownies"], amount=50, skip_top_posts=True, randomize=True)

  # Joining Engagement Pods
  
  