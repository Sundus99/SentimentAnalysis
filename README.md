# SentimentAnalysis
*Description: * This is a shopping assistant that helps users see the gist of all the reviews via sentiment analysis 
to quickly determine if they'd like to buy that product or not without manually going through so many reviews.
Best thing is, it utilizes reviews in foreign language via google translate

More features to be added later.

Instructions: 
Step1: use pip3 install commands to download the following:
- request
- bs4
- googletrans
- termcolor
- nltk

Step2: run the python script settings.py using the command python setting.py

Step3: You will need to create header file to be able to make scrape review data from Amazon
- select a product, go to its review section, right click then select inspect, then select Network, then select doc
- then refresh, then select the first one, right click on and copy then copy as curl(bash)
- then go to curl.trillworks.com paste it there and then copy the header in python and add it to the release1.... file

Step4: go to command prompt, go to the directory you downloaded it in, then do python re then press tab the file name will automatically fill and hit enter and tada
