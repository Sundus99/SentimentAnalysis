import requests
from bs4 import BeautifulSoup
from googletrans import Translator
import math
import string
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from termcolor import colored
import os 

os.system('color')
#url = "https://www.amazon.ca/product-reviews/B08CBT8GNW"
url_base = "https://www.amazon.ca/NICE-POWER-Variable-Adjustable-Regulated-Higher-Precision/product-reviews/B08CBT8GNW/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews"
url_base2 = "https://www.amazon.ca/UNIROI-Regulator-Variable-Adjustable-Alligator/product-reviews/B07XDWPB3L/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews"

url_suffix = "&pageNumber={}"

complete_url1 = url_base+url_suffix
complete_url2 = url_base2+url_suffix
#input("Please input url of the reviews section and paste the link. \n Please ensure that the url ends with all_reviews only")

#========================insert header here

def get_soup(url, headers):
	r = requests.get(url,headers=headers)

	#r gives html result
	#print(r.text+"\n=================\n")
	soup = BeautifulSoup(r.text, 'html.parser')
	return soup

def get_numRevs(soup):
	numRevs = soup.find('div', {'data-hook': 'cr-filter-info-review-rating-count'}).get_text()
	num_rat, num_rvs = numRevs.strip().split("|")
	num_rvs = int(num_rvs.replace("global reviews","").strip())
	return num_rvs

def get_ratings(soup):
	rating = soup.find('span', {'data-hook': 'rating-out-of-text'}).get_text()
	return rating


def get_reviews(soup):
	reviews = soup.find_all('div', {'data-hook': 'review'})
	rev_string = ""
	count = 0
	for item in reviews:
		if item is not None:
			body = item.find('span', {'data-hook': 'review-body'}).get_text().strip()
			count = count + 1
			rev_string = rev_string + " " + body 
	return rev_string #all reviews merged as 1 in a string
#===========================================================================
def sentiment_score(text):
	s_dict = SentimentIntensityAnalyzer().polarity_scores(text)
	print(colored("Compound: ", 'cyan',attrs=['bold']), s_dict['compound'])
	print(colored("Positive: ",'green',attrs=['bold']),s_dict['pos']*100,"%")
	print(colored("Neutral: ", 'grey',attrs=['bold']),s_dict['neu']*100,"%")
	print(colored("Negative: ",'red',attrs=['bold']),s_dict['neg']*100,"%")
	if s_dict['compound'] >= 0.05:
		return "Positive"
	elif s_dict['compound'] <= -0.05:
		return "Negative"
	else:
		return "Neutral"
#===========================================================================
s = get_soup(url_base, headers)
r = get_numRevs(s)
rat = get_ratings(s)

url1=""
rev = ""
trans_rev = ""
for i in range(1,math.ceil(r/10)+1):
	url1 = complete_url1.format(i)
	s1 = get_soup(url1,headers)

	rev = rev + get_reviews(s1)
	translator = Translator()
	trans_rev = translator.translate(rev)
lower_case = trans_rev.text.lower()

#removing punctuations
cleaned_text = lower_case.translate(str.maketrans('','',string.punctuation))
print(colored("For the product at the following url: ",'magenta',attrs=['bold']), url_base)
print(colored("\nOverall Sentiment: ",'cyan',attrs=['bold']), sentiment_score(cleaned_text))

