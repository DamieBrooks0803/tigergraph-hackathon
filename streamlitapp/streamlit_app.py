import pandas as pd
from pandas import DataFrame
import streamlit as st
import streamlit.components.v1 as components
import base64

st.set_page_config(page_title="Consider a new view A Graph Solution by Damie Brooks", page_icon="", layout="wide")

#allow the user to select a topic
add_selectbox = st.sidebar.selectbox(
    "Select a topic to view diverse perspectives.",
    ("", "Cryptocurrency", "War", "Antiwork")
)
st.sidebar.markdown("""<div class='sidebarinfo'><p>In today's hyper-digital world, algorithms determine what we see. Narratives are forced upon us into an echo chambers.</p><p><b><i>Confirmation bias</i></b> is the concept that when we see something that reinforces our current thinking we are more likely to believe this new input as truth.</p></div>""", unsafe_allow_html=True)
st.sidebar.markdown("""<div class='sidebarinfo2'><p>For this Tiger Graph challenge, we extract post listings from Reddit across the entire community. We apply <b>similarity</b> and <b>sentiment</b> analysis to look for patterns.</p><p>Using these findings, we can run <b>custom graph queries and traversals</b> across our graph solution to suggest other posts that are relevant but different in their mood or subreddit community.</p><p>Offering diverse and alternative perspectives can break confirmation bias and <b>foster critical thinking</b> - allowing users to think for themselves.</p></div>""", unsafe_allow_html=True)
st.sidebar.markdown("""<div class='sidebarinfo3'><p>Learn more <a href='https://www.linkedin.com/in/damiebrooks0803/' target='_blank'>about me.</a></div>""", unsafe_allow_html=True)

def loadinstyle():
	stylecontent = '''
	<style>
		body, .css-nlntq9, h1, h2, h3{
			font-family: Tahoma, sans-serif !important;
			}
		h1 {text-transform: uppercase;}
		h2 {text-transform: capitalize;}
		h3 {text-transform: lowercase;}
		.sampleheadline{
			font-weight: bold;
			font-size: 1.5em;
			font-style: italic;
		}
		element.style{display: block !important;}
		.sampleheading{
			font-size: 1.8em;
			font-weight: bold;
    			color: #2e5894;
		}
		.postcard{
			background-color: #003366;
			width: 300px;
		}
		.samplePost{
			background-color: black;
			padding-right: 50px;
		}
		.sampleicon{
			height: 100px;
			width: 100px;
			padding: 50 50 50 50;
		}
		.sidebarinfo{
			background-color: #add8e6;
			height: 300px;
			color: #666666;
			border-radius: 15px;
			padding-left: 15px;
			padding-right: 15px;
			padding-top: 30px;
			margin-top: 50px;
		}
		.sidebarinfo2{
			background-color: #add8e6;
			height: 500px;
			border-radius: 15px;
			padding-left: 15px;
			padding-right: 15px;
			padding-top: 30px;
			margin-top: 50px;
			color: #666666;
		}
		.sidebarinfo3{
			padding-left: 15px;
			padding-top: 30px;
			color: #666666;
		}
		.postcard{
			background-color: #003366 !important;
			border-radius: 20px;
			padding-left: 12px;
			padding-top: 12px;
			padding-bottom: 12px;
			color: white;
			height: 250px;
			padding-right: 15px;
		}
		.postcard a{
			color: #f2f2f2;
		}
		#samplePost{
			width: 95%;
		}
		.suggestioheading{
			font-size: 20px;
			font-weight: bold;
			padding-top: 20px;
			padding-bottom: 10px;
		}		
	</style>
	'''
	st.markdown(stylecontent, unsafe_allow_html=True)
	return
loadinstyle()
#set the image for the post user avatar
def get_base64_of_bin_file(bin_file):
	with open(bin_file, 'rb') as f:
		data = f.read()
	return base64.b64encode(data).decode()	
def set_png_as_page_bg(png_file):
	bin_str = get_base64_of_bin_file(png_file)
	page_bg_img = '''
	<style>
	.sampleicon {
		background-image: url("data:image/png;base64,%s");
		 background-size: cover;
		 height: 145px;
		 width: 143px;
	}
	</style>
	''' % bin_str
	st.markdown(page_bg_img, unsafe_allow_html=True)
	return
def set_png_as_page_bg2(png_file):
	bin_str = get_base64_of_bin_file(png_file)
	page_bg_img = '''
	<style>
	.samplesentiment {
		background-image: url("data:image/png;base64,%s") !important;
		 background-size: cover;
		 height: 40px;
		 width: 40px;
	}
	</style>
	''' % bin_str
	st.markdown(page_bg_img, unsafe_allow_html=True)
	return	
#dynamic content div containers for each post by topic
def set_conpost_container(selection):
	if selection == 'War':
		myfirstpost = """<div id='myconPost1' class='postcard'><div id='headline1'>Bloodthirst in this subreddit is making me sick.
					</div><br><br><br><br><br><a href='https://www.reddit.com/r/UkraineWarVideoReport/comments/tdjufi/bloodthirst_in_this_subreddit_is_making_me_sick/'>View Post</a>
					</div>"""
	if selection == 'Cryptocurrency':
		myfirstpost = """<div id='myconPost1' class='postcard'><div id='headline1'>Everyone was for decentralisation until Russia wanted to sell Gas for bitcoin 
		now people around this sub are crying about it with comments like I would rather lose money and the price tanks than Russia making money... 
					</div><br><a href='https://www.reddit.com/r/CryptoCurrency/comments/tniwhf/everyone_was_for_decentralisation_until_russia/'>View Post</a>
					</div>"""
	if selection == 'Antiwork':
		myfirstpost = """<div id='myconPost1' class='postcard'><div id='headline1'>Reminder, if you're anti-woke, you're anti-worker 
					</div><br><br><br><br><br><a href='https://www.reddit.com/r/antiwork/comments/tp02kt/reminder_if_youre_antiwoke_youre_antiworker/'>View Post</a>
					</div>"""
	return myfirstpost
def set_conpost_container2(selection):
	if selection == 'War':
		mysecondpost = """<div id='myconPost2' class='postcard'><div id='headline1'>NATO official Twitter account finally deleted tweet mistakenly showcasing Ukranian woman with Nazi black sun symbol after Nazis in Ukraine started trending.
		 The tweet was intended to show support for Ukranian women...
					</div><br><a href='https://www.reddit.com/r/UkraineWarVideoReport/comments/t9ucvw/nato_official_twitter_account_finally_deleted/'>View Post</a>
					</div>"""
	if selection == 'Cryptocurrency':
		mysecondpost = """<div id='myconPost2' class='postcard'><div id='headline1'>I underestimated Crypto Reddit.
					</div><br><br><br><br><br><br><a href='https://www.reddit.com/r/CryptoCurrency/comments/sw0y2d/i_underestimated_crypto_reddit/'>View Post</a>
					</div>"""
	if selection == 'Antiwork':
		mysecondpost = """<div id='myconPost2' class='postcard'><div id='headline1'>Minimum Wage Should Be $55-80 per hour.
					</div><br><br><br><br><br><a href='https://www.reddit.com/r/antiwork/comments/t4c6a8/minimum_wage_should_be_5580_per_hour/'>View Post</a>
					</div>"""
	return mysecondpost
def set_conpost_container3(selection):
	if selection == 'War':
		mythirdpost = """<div id='myconPost3' class='postcard'><div id='headline1'>Demonstration against NATO took place in Greece.
					</div><br><br><br><br><br><a href='https://www.reddit.com/r/UkraineWarVideoReport/comments/t7kep2/demonstration_against_nato_took_place_in_greece/'>View Post</a>
					</div>"""
	if selection == 'Cryptocurrency':
		mythirdpost = """<div id='myconPost3' class='postcard'><div id='headline1'>The world should cut Russia off from SWIFT and crypto by cutting internet access. Can't turn to crypto if they can't access the internet. 
					</div><br><br><br><a href='https://www.reddit.com/r/CryptoCurrency/comments/t049ia/the_world_should_cut_russia_off_from_swift_and'>View Post</a>
					</div>"""
	if selection == 'Antiwork':
		mythirdpost = """<div id='myconPost1' class='postcard'><div id='headline1'>You can't be anti-work and pro-cop. 
					</div><br><br><br><br><br><br><a href='https://www.reddit.com/r/antiwork/comments/texq1p/you_cant_be_anti_work_and_pro_cop/'>View Post</a>
					</div>"""
	return mythirdpost		
def set_moodpost_container(selection):
	if selection == 'War':
		myfirstpost = """<div id='mymoodPost1' class='postcard'><div id='headline1'>At the Polish border, volunteers are working hard to make sure Ukrainian kids are happy as well as safe.
					</div><br><br><br><br><a href='https://www.reddit.com/r/UkraineWarVideoReport/comments/teo3ww/at_the_polish_border_volunteers_are_working_hard/'>View Post</a>
					</div>"""
	if selection == 'Cryptocurrency':
		myfirstpost = """<div id='mymoodPost1' class='postcard'><div id='headline2'>Alex Bornyako - Ukraine's deputy minister of digital transformation the national 
		bank is not fully operating, crypto is helping to perform fast transfers to make it very quick and get results almost immediately...
					</div><br><a href='https://www.reddit.com/r/CryptoCurrency/comments/tedkmi/alex_bornyakov_ukraines_deputy_minister_of/'>View Post</a>
					</div>"""
	if selection == 'Antiwork':
		myfirstpost = """<div id='mymoodPost1' class='postcard'><div id='headline2'>Got told I'm committing wage theft for clocking in when boss calls me for hour long meetings.
					</div><br><br><br><br><a href='https://www.reddit.com/r/antiwork/comments/teqv3r/got_told_im_committing_wage_theft_for_clocking_in/'>View Post</a>
					</div>"""
	return myfirstpost
def set_moodpost_container2(selection):
	if selection == 'War':
		mysecondpost = """<div id='mymoodPost2' class='postcard'><div id='headline1'>French activist Pierre Avner broke into the villa of Putin's daughter Alta Mira in the French city of Biarritz changed the locks and announced that the villa was ready to accept Ukrainian refugees. 
					</div><br><a href='https://www.reddit.com/r/UkraineWarVideoReport/comments/tdowiv/french_activist_pierre_avner_broke_into_the_villa/'>View Post</a>
					</div>"""
	if selection == 'Cryptocurrency':
		mysecondpost = """<div id='mymoodPost2' class='postcard'><div id='headline2'>Saying Bitcoin won't do a 100x isnt FUD,  it's just being realistic  
					</div><br><br><br><br><br><a href='https://www.reddit.com/r/CryptoCurrency/comments/t92nmp/saying_bitcoin_wont_do_a_100x_isnt_fud_its_just/'>View Post</a>
					</div>"""
	if selection == 'Antiwork':
		mysecondpost = """<div id='mymoodPost2' class='postcard'><div id='headline2'>Is this dood serious? LOL
					</div><br><br><br><br><br><br><a href='https://www.reddit.com/r/antiwork/comments/tvzrn9/is_this_dood_serious_lol/'>View Post</a>
					</div>"""
	return mysecondpost
def set_moodpost_container3(selection):
	if selection == 'War':
		mythirdpost = """<div id='mymoodPost3' class='postcard'><div id='headline1'>Ukranians playing with their new toy from the US MK 19 belt fed 40mm Grenade Launcher 
					</div><br><br><br><br><a href='https://www.reddit.com/r/UkraineWarVideoReport/comments/tvf3xw/ukraniand_playing_with_their_new_toy_from_the_us/'>View Post</a>
					</div>"""
	if selection == 'Cryptocurrency':
		mythirdpost = """<div id='mymoodPost3' class='postcard'><div id='headline2'>Nano is in fact too good to be true. Please don't tell your loved ones to buy it. Blaring security flaws and other issues inside this thread. 
					</div><br><br><br><a href='https://www.reddit.com/r/CryptoCurrency/comments/tpdyv8/nano_is_in_fact_too_good_to_be_true_please_dont/'>View Post</a>
					</div>"""
	if selection == 'Antiwork':
		mythirdpost = """<div id='mymoodPost3' class='postcard'><div id='headline2'>Women should be given PTO for heavy periods. Do you agree? 
					</div><br><br><br><br><br><a href='https://www.reddit.com/r/antiwork/comments/tk8lzi/women_should_be_given_pto_for_heavy_periods_do/'>View Post</a>
					</div>"""
	return mythirdpost	
def set_obspost_container(selection):
	if selection == 'War':
		myfirstpost = """<div id='myconPost1' class='postcard'><div id='headline1'>Aftermath of the strike on the shopping mall in Kiev firefighters rescue a person from under the rubble 
					</div><br><br><br><br><a href='https://www.reddit.com/r/UkraineWarVideoReport/comments/tiycil/aftermath_of_the_strike_on_the_shopping_mall_in/'>View Post</a>
					</div>"""
	if selection == 'Cryptocurrency':
		myfirstpost = """<div id='myobsPost1' class='postcard'><div id='headline1'>My first dip in crypto. Any tips and tricks I should look out for?  
					</div><br><br><br><br><br><a href='https://www.reddit.com/r/CryptoCurrency/comments/tkumic/my_first_dip_in_crypto_any_tips_and_tricks_i/'>View Post</a>
					</div>"""
	if selection == 'Antiwork':
		myfirstpost = """<div id='myobsPost1' class='postcard'><div id='headline3'>The level of apathy at my work is astounding.
					</div><br><br><br><br><br><a href='https://www.reddit.com/r/antiwork/comments/tkuz1i/the_level_of_apathy_at_my_work_is_astounding/'>View Post</a>
					</div>"""
	return myfirstpost
def set_obspost_container2(selection):
	if selection == 'War':
		mysecondpost = """<div id='myobsPost2' class='postcard'><div id='headline2'>A lot of fire after a very powerful explosion in the Kiev region 
					</div><br><br><br><br><br><a href='https://www.reddit.com/r/UkraineWarVideoReport/comments/tmuxoz/a_lot_of_fire_after_a_very_powerful_explosion_in/'>View Post</a>
					</div>"""
	if selection == 'Cryptocurrency':
		mysecondpost = """<div id='myobsPost2' class='postcard'><div id='headline2'>Help Ukraine and get a tax deduction, 27 charities that accept crypto donations 
					</div><br><br><br><br><a href='https://www.reddit.com/r/CryptoCurrency/comments/tpdyv8/nano_is_in_fact_too_good_to_be_true_please_dont/'>View Post</a>
					</div>"""
	if selection == 'Antiwork':
		mysecondpost = """<div id='myobsPost2' class='postcard'><div id='headline3'>My time off request to see my dying grandpa was denied so we can showcase our amazing store.
					</div><br><br><br><br><a href='https://www.reddit.com/r/antiwork/comments/tiyffo/my_time_off_request_to_see_my_dying_grandpa_was/'>View Post</a>
					</div>"""
	return mysecondpost
def set_obspost_container3(selection):
	if selection == 'War':
		mythirdpost = """<div id='myobsPost3' class='postcard'><div id='headline3'>Russia uses underwater tanks in Ukraine 
					</div><br><br><br><br><br><a href='https://www.reddit.com/r/UkraineWarVideoReport/comments/tmux0y/russia_uses_underwater_tanks_in_ukraine/'>View Post</a>
					</div>"""
	if selection == 'Cryptocurrency':
		mythirdpost = """<div id='myobsPost3' class='postcard'><div id='headline3'>How crypto and blockchain projects are driving forward a new era of tech 
					</div><br><br><br><br><br><a href='https://www.reddit.com/r/CryptoCurrency/comments/tga1sd/how_crypto_and_blockchain_projects_are_driving/'>View Post</a>
					</div>"""
	if selection == 'Antiwork':
		mythirdpost = """<div id='myobsPost3' class='postcard'><div id='headline3'>The next email I send isn't to my former executive director, it is to a strategically chosen press outlet.
					</div><br><br><br><br><a href='https://www.reddit.com/r/antiwork/comments/tiymmo/the_next_email_i_send_isnt_to_my_former_executive/'>View Post</a>
					</div>"""	
	return mythirdpost				
def my_widget(key):
	#add a custom author image for each category type based on selection
	if key == 'War':
		set_png_as_page_bg('images/bear.png')
	if key == "Cryptocurrency":
		set_png_as_page_bg('images/tiger.png')
	if key == "Antiwork":
		set_png_as_page_bg('images/elephant.png')						
	return 
if add_selectbox: 
	my_widget(add_selectbox)
def fillcontainercon1():
	newcontentcon1 = set_conpost_container(add_selectbox)
	st.markdown(newcontentcon1, unsafe_allow_html=True)
	return
def fillcontainercon2():
	newcontentcon2 = set_conpost_container2(add_selectbox)
	st.markdown(newcontentcon2, unsafe_allow_html=True)
	return
def fillcontainercon3():
	newcontentcon3 = set_conpost_container3(add_selectbox)
	st.markdown(newcontentcon3, unsafe_allow_html=True)
	return	
def fillcontainermood1():
	newcontentmood1 = set_moodpost_container(add_selectbox)
	st.markdown(newcontentmood1, unsafe_allow_html=True)
	return
def fillcontainermood2():
	newcontentmood2 = set_moodpost_container2(add_selectbox)
	st.markdown(newcontentmood2, unsafe_allow_html=True)
	return
def fillcontainermood3():
	newcontentmood3 = set_moodpost_container3(add_selectbox)
	st.markdown(newcontentmood3, unsafe_allow_html=True)
	return	
def fillcontainerobs1():
	newcontentobs1 = set_obspost_container(add_selectbox)
	st.markdown(newcontentobs1, unsafe_allow_html=True)
	return
def fillcontainerobs2():
	newcontentobs2 = set_obspost_container2(add_selectbox)
	st.markdown(newcontentobs2, unsafe_allow_html=True)
	return
def fillcontainerobs3():
	newcontentobs3 = set_obspost_container3(add_selectbox)
	print(newcontentobs3 )
	st.markdown(newcontentobs3, unsafe_allow_html=True)
	return				
st.header("Consider a new view, a graph solution")
st.subheader("Submitted by: Damie Brooks")
set_png_as_page_bg2('images/negative_thumbs.png')						
with st.container():	
	if add_selectbox == 'War':
		st.markdown("""<div class='sampleheading'>A Sample War Post</div>""", unsafe_allow_html=True)
	if add_selectbox == 'Cryptocurrency':
		st.markdown("""<div class='sampleheading'>A Sample Cryptocurrency Post</div>""", unsafe_allow_html=True)
	if add_selectbox == 'Antiwork':
		st.markdown("""<div class='sampleheading'>A Sample Antiwork Post</div>""", unsafe_allow_html=True)
	image_column, text_column = st.columns((1,3))
	with image_column:
		if add_selectbox == 'War':
			st.markdown("""<div class='samplecontainer'><div class='sampleicon'>&nbsp;</div>
							<span class='sampleuser'><b>Written by:</b><br>Koobitz</span>
							</div>""", unsafe_allow_html=True)
		if add_selectbox == 'Cryptocurrency':
			st.markdown("""<div class='samplecontainer'><div class='sampleicon'>&nbsp;</div>
							<span class='sampleuser'></span><b>Written by:</b><br>Vaginosis-Psychosis</span>
							</div>""", unsafe_allow_html=True)
		if add_selectbox == 'Antiwork':
			st.markdown("""<div class='samplecontainer'><div class='sampleicon'>&nbsp;</div>
							<span class='sampleuser'></span><b>Written:</b><br>LordeOfTheTree</span>
							</div>""", unsafe_allow_html=True)
	with text_column:
		if add_selectbox == 'War':
			st.markdown("""<div id='samplePost' class='samplecard'><br><div class='sampleheadline'>Neutrality lost</div>
				<b>Subreddit:</b> UkraineVideoWarReport<br><b>Sentiment:</b> <div class='samplesentiment'>&nbsp;</div>
				<a href='https://www.reddit.com/r/UkraineWarVideoReport/comments/t2o489/neutrality_lost/' target='_blank'>View Post</a>
				<div id='body'>This subreddit started out as a neutral space to keep track of the war. However it's become a one sided subreddit. 
				Anything posted or said from the Russian side either quickly gets removed or gets downvoted into oblivion. If you want to see the truth of the war, 
				all sides should be seen. Just to make it clear seeing as to a vast majority of you this isn't clear. I don't care about propaganda. 
				Both sides will have their fair share of it to boost their morale. This subreddit was created to document the war. 
				And I would like to see the war unfold from a unbiased perspective coming from both sides. Either side will post videos that favour 
				themselves and not their enemies. But in the middle we will find and see the truth. If you want the truth of the war that is the only 
				way you can have it is to see both sides.</div>
				</div>""", unsafe_allow_html=True)
		if add_selectbox == 'Cryptocurrency':
			st.markdown("""<div id='samplePost' class='samplecard'><div class='sampleheadline'>Idgaf. I'm leaving my coins on an exchange where it is insured. Too many scams out there that even crypto vets are falling for.</div>
				<b>Subreddit:</b> Cryptocurrency<br><b>Sentiment:</b> <div class='samplesentiment'>&nbsp;</div>
				<a href="https://www.reddit.com/r/CryptoCurrency/comments/tvmtda/idgaf_im_leaving_my_coins_on_an_exchange_where_it/" target="_blank">View Post</a>
				<div id='body'>Last night several threads warned about Trezor phishing scam and almost on cue, today I read a post by 7 year crypto 
				veteran that he fell for it and lost everything about 72,000 in Bitcoin. It can happen to anyone. 
				You're tired, arguing with your gf, distracted, etc nobody is perfect. 
				He lost everything. I can't afford that. Shit gives me nightmares.</div>  
				</div>""", unsafe_allow_html=True)
		if add_selectbox == 'Antiwork':
			st.markdown("""<div id='samplePost' class='samplecard'><br><div class='sampleheadline'>PSA Your coworkers are not your friends.</div>
				<b>Subreddit:</b> Antiwork<br><b>Sentiment:</b> <div class='samplesentiment'>&nbsp;</div>
				<a class='ssamplelink' href="https://wwww.reddit.com/r/antiwork/comments/tcoqqw/psa_your_coworkers_are_not_your_friends/" target="_blank">View Post</a><br>
				<div id='body'>This is just a reminder to anyone on here that YOUR COWORKERS ARE NOT YOUR FRIENDS. Do not share any personal information about 
				your life, family, friends outside of work, side hustles, etc. with them and DEFINITELY DO NOT add them on any type of social media,
				 especially managers. The moment I start a new job anywhere I immediately look up everyone I work with and block them on all platforms and block 
				 the company as well  If they ask, tell them you do not have social media. Also DO NOT put your full name on social media and make sure that you 
				 uncheck in the settings within the apps where it asks if it can connect your contacts or that you can be looked up my email or phone number. 
				 Obviously this is just advice - do what you want, but just be cautious.</div> 
				</div>""", unsafe_allow_html=True)
with st.container():	
	if add_selectbox:
		st.markdown("""<div class='suggestioheading'>Controversial Suggestions</div>""", unsafe_allow_html=True)
	column1, column2, column3 = st.columns((1,1,1))
	with column1:
		placeholder1 = st.empty()
		with placeholder1.container():
			if add_selectbox:
				fillcontainercon1()
	with column2:
		placeholder2 = st.empty()
		with placeholder2.container():
			if add_selectbox:
				fillcontainercon2()	
	with column3:
		placeholder3 = st.empty()
		with placeholder3.container():
			if add_selectbox:
				fillcontainercon3()
with st.container():	
	if add_selectbox:
		st.markdown("""<div class='suggestioheading'>Varied Mood Suggestions</div>""", unsafe_allow_html=True)
	column1, column2, column3 = st.columns((1,1,1))
	with column1:
		placeholdera = st.empty()
		with placeholdera.container():
			if add_selectbox:
				fillcontainermood1()
	with column2:
		placeholderb = st.empty()
		with placeholderb.container():
			if add_selectbox:
				fillcontainermood2()	
	with column3:
		placeholderc = st.empty()
		with placeholderc.container():
			if add_selectbox:
				fillcontainermood3()	
with st.container():	
	if add_selectbox:
		st.markdown("""<div class='suggestioheading'>Obscure Suggestions</div>""", unsafe_allow_html=True)
	column1, column2, column3 = st.columns((1,1,1))
	with column1:
		placeholderi = st.empty()
		with placeholderi.container():
			if add_selectbox:
				fillcontainerobs1()
	with column2:
		placeholderii = st.empty()
		with placeholderii.container():
			if add_selectbox:
				fillcontainerobs2()	
	with column3:
		placeholderiii = st.empty()
		with placeholderiii.container():
			if add_selectbox:
				fillcontainerobs3()
