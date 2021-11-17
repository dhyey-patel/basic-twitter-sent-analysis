##
#Dhyey Patel
#250960470
#November 15th 2017
#Assignment 3: Sentiment Analysis
##

# Import happy_histogram to give a graphic output
from happy_histogram import *

# Start by defining a function main where the code is put together
def main ():
    # get the name of the keywords file
    keywords_name = input("Enter the name for the files with the keywords: ")
    # try to open the keywords file and if it opens then store all the keywords and their sentiment value, if the file does not open then exit the program and print an error message
    try:
        keywords_file = open(keywords_name,"r",encoding="utf-8")
        keywords = []
        sent_vals = []
        for line in keywords_file:
                words = line.split(",")
                keywords.append(words[0].lower())
                sent_vals.append(int(words[1]))
        # get the name of the file witht he tweets
        tweets_name = input("Enter the name for the files with the tweets: ")
        # try to open the file and calculate the average of sentiment values if file does not open then exit the program and print an error message
        try:
            tweets_file = open(tweets_name,"r",encoding="utf-8")
            eastern_sentVals = []
            central_sentVals = []
            mountain_sentVals = []
            pacific_sentVals = []
            # go through every single line in the tweet, get the tweet, get the words of the tweet, get the location of the tweet, and get the sentiment average of the tweet
            for line in tweets_file:
                timeZone = findTimeZone(line)
                tweet_words = removePunctuation(getTweet(line).lower()).split()
                score = getSentVal(tweet_words,keywords,sent_vals)
                # categorize the tweets into their specific time zones
                if timeZone == "eastern" and score!=0:
                    eastern_sentVals.append(score)
                elif timeZone == "central" and score!=0:
                    central_sentVals.append(score)
                elif timeZone == "mountain" and score!=0:
                    mountain_sentVals.append(score)
                elif timeZone == "pacific" and score!=0:
                    pacific_sentVals.append(score)
            # calculate the average of all the sentiment average per tweet
            easternAverage = sum(eastern_sentVals)/len(eastern_sentVals)
            centralAverage = sum(central_sentVals)/len(central_sentVals)
            mountainAverage = sum(mountain_sentVals)/len(mountain_sentVals)
            pacificAverage = sum(pacific_sentVals)/len(pacific_sentVals)
            # print the number of tweets in each time zone, and print the average
            print("There are %d tweets in the Eastern Time Zone, and the average sentiment value is %0.4f" % (len(eastern_sentVals), easternAverage))
            print("There are %d tweets in the Central Time Zone, and the average sentiment value is %0.4f" % (len(central_sentVals), centralAverage))
            print("There are %d tweets in the Mountain Time Zone, and the average sentiment value is %0.4f" % (len(mountain_sentVals), mountainAverage))
            print("There are %d tweets in the Pacific Time Zone, and the average sentiment value is %0.4f" % (len(pacific_sentVals), pacificAverage))
            # print the histogram using the drawSimpleHistogram function from happy_histogram
            drawSimpleHistogram(easternAverage,centralAverage,mountainAverage,pacificAverage)
            tweets_file.close()
        except IOError:
            exit("Error: File not found")
        keywords_file.close()
    except IOError:
        exit("Error: File not found")

# get the sentimental value given the list of words in the tweet, the keywords and the sentimental value of each tweet
def getSentVal (tweetWords,keyWords,sentVal):
    score = 0
    counter = 0
    averagescore = 0
    for word in tweetWords:
        for i in range (len(keyWords)):
            if keyWords[i] == word:
                score += sentVal[i]
                counter+=1
    if counter>0:
        averagescore = score/counter
    return averagescore

# this function will get just the tweet from the line with everything
def getTweet (fullTweet):
    seperatedTweet = fullTweet.split(" ",5)
    tweet = seperatedTweet[5].strip()
    return tweet

# this function gets the longitude and latitude and uses that to find the time zone of the tweet
def findTimeZone (fullTweet):
    seperateTweet = fullTweet.split("]")
    latANDlong = seperateTweet[0].split(" ")
    lat = float((latANDlong[0]).strip("[,"))
    long = float(latANDlong[1])
    if lat>=24.660845 and lat <= 49.189787:
        if long <= -67.444574 and long > -87.518395:
            return "eastern"
        elif long <=  -87.518395 and long > -101.998892:
            return "central"
        elif long <= -101.998892 and long > -115.236428:
            return "mountain"
        elif long <= -115.236428 and long >= -125.242264:
            return "pacific"

#removes all puntuation and numbers from the tweet
def removePunctuation (sentence):
    puntuation = ["!","@","#","$","%","^","&","*","(",")","-","_","+","=","{","}","|","[","]",";",":",",",".","<",">","/","?",".",'"']
    for el in puntuation:
        sentence = sentence.replace(el,"")
    for i in range(10):
        sentence = sentence.replace(str(i),"")
    return sentence


# Run the whole code, but running main
main()
