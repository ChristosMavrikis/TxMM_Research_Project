#https://www.kaggle.com/gpreda/covid19-tweets

#Author s1059094 - TxMM Research Project 2020 - 2021

################# SENTIMENT ANALYSIS AND TOPIC MODELLING ############################

#Imports
import pandas as pd
import nltk
nltk.download('stopwords')
import warnings
warnings.simplefilter("ignore", DeprecationWarning)

from nltk.corpus import stopwords
from MyFunctions import MyFunctions
from MyEmotion import MyEmotion
from MyPiePlots import MyPiePlots
from MyWords import MyWords
from MyLDA import MyLDA
from MyTopNgrams import MyTopNgrams
from nltk.tokenize import word_tokenize
from nltk import PorterStemmer
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob


if __name__ == '__main__':
    path_to_data = 'DataSets/covid19_tweets.csv' #load the dataset
    tweets = pd.read_csv(path_to_data,nrows=100000)  #load to pandas
    ps = PorterStemmer() #function used for stemming
    lemmatizer = WordNetLemmatizer() #function used for lemmatization
    # initializations for lists that later on get added to the inital tweets dataframe
    x = []
    sentiment = []
    compound_l = []
    polarity_l = []
    subjectivity_l = []
    negative_l = []
    positive_l = []
    neutral_l = []
    fine_grain = []
    emotions = []
    #Iterator through tweet text to clean and create other columns - find emotion - find sentiment
    for i in range(len(tweets)):
        print(i)
        word_tokens = []
        tokens_without_sw = ""
        tmp = ""
        polarity = 0
        tweets['text'][i] = tweets['text'][i].lower() #covert to lowercase
        tmp = MyFunctions.clean_string(tweets['text'][i]) #call clean text function - for pre-processing
        emotion = MyEmotion.find_main_emotion(tmp) #call find emotion function
        #print(emotion)
        emotions.append(emotion)
        #code for sentiment analysis
        analysis = TextBlob(tmp)
        score = SentimentIntensityAnalyzer().polarity_scores(tmp)
        negative = score['neg']
        neutral  = score['neu']
        positive = score['pos']
        compound = score['compound']
        polarity += analysis.sentiment.polarity
        #calculate the sentiment based apo the above scores and add to the lists
        if negative > positive:
            sentiment.append("Negative")
            negative_l.append(negative)
            positive_l.append("-")
            neutral_l.append("-")
        elif positive > negative:
            sentiment.append("Positive")
            negative_l.append("-")
            positive_l.append(positive)
            neutral_l.append("-")
        elif positive == negative:
            sentiment.append("Neutral")
            negative_l.append("-")
            positive_l.append("-")
            neutral_l.append(neutral)
        compound_l.append(compound)
        #calculate fine-grain sentiment analysis
        if compound == 0:
            fine_grain.append(0)
        elif compound > 0.5 and compound <= 1:
            fine_grain.append(2)
        elif compound > 0 and compound <= 0.5:
            fine_grain.append(1)
        elif compound < 0 and compound >= -0.5:
            fine_grain.append(-1)
        else:
            fine_grain.append(-2)
        #add subjectivity and polarity of tweet to dataframe
        subjectivity_l.append(analysis.subjectivity)
        polarity_l.append(polarity)

        #Tokenazation and stem
        word_tokens = word_tokenize(tmp)
        tokens_without_sw = [word for word in word_tokens if not word in stopwords.words()]
        #output_stem = [ps.stem(word) for word in tokens_without_sw]
        output_stem = [lemmatizer.lemmatize(word) for word in tokens_without_sw]
        x.append(output_stem)

    #Add new findings to pd.dataframe
    tweets['clean-text'] = x
    tweets['sentiment'] = sentiment
    tweets['positive'] = positive_l
    tweets['negative'] = negative_l
    tweets['neutral'] = neutral_l
    tweets['subjectivity'] = subjectivity_l
    tweets['compound'] = compound_l
    tweets['polarity'] = positive_l
    tweets['fine_grain'] = fine_grain
    tweets['emotions'] = emotions

    #print(type(tweets['emotions']))
    MyEmotion.plot_emotion_sum(tweets['emotions'], "All tweets")
    #print(tweets['emotions'])
    #Normal Sentiment
    list_of_positive = tweets[tweets["sentiment"] == "Positive"]
    list_of_negative = tweets[tweets["sentiment"] == "Negative"]
    list_of_neutral  = tweets[tweets["sentiment"] == "Neutral"]

    MyEmotion.plot_emotion_sum(list_of_positive['emotions'], "Positive tweets") #Figure 9
    MyEmotion.plot_emotion_sum(list_of_negative['emotions'], "Negative tweets") #Figure 10
    MyEmotion.plot_emotion_sum(list_of_neutral['emotions'], "Neutral tweets") #Figure 11
    # #Fine - Grain Sentiment
    list_of_very_positive_fg = tweets[tweets["fine_grain"] == 2]
    list_of_positive_fg = tweets[tweets["fine_grain"] == 1]
    list_of_neutral_fg = tweets[tweets["fine_grain"] == 0]
    list_of_negative_fg = tweets[tweets["fine_grain"] == -1]
    list_of_very_negative_fg = tweets[tweets["fine_grain"] == -2]
    print('\n')
    print('Average sentence length of all tweets', MyWords.word_count(tweets['clean-text']))
    print('Average sentence length of cleaned positive tweets', MyWords.word_count(list_of_positive['clean-text']))
    print('Average sentence length of cleaned negative tweets', MyWords.word_count(list_of_negative['clean-text']))
    print('Average sentence length of cleaned neutral  tweets', MyWords.word_count(list_of_neutral['clean-text']))
    print('\n')
    print('Average subjectivity of all tweets', MyWords.word_subjectivity_avg(tweets['subjectivity']))
    print('Average subjectivity of positive tweets', MyWords.word_subjectivity_avg(list_of_positive['subjectivity']))
    print('Average subjectivity of negative tweets', MyWords.word_subjectivity_avg(list_of_negative['subjectivity']))
    print('Average subjectivity of neutral tweets', MyWords.word_subjectivity_avg(list_of_neutral['subjectivity']))
    print('\n')
    print('Average polarity of all tweets', MyWords.word_polarity_avg(tweets['polarity']))
    print('Average polarity of positive tweets', MyWords.word_polarity_avg(list_of_positive['polarity']))
    print('Average polarity of negative tweets', MyWords.word_polarity_avg(list_of_negative['polarity']))
    print('Average polarity of neutral tweets', MyWords.word_polarity_avg(list_of_neutral['polarity']))

    #Helpful Plots - Pie Plot - WordCloudsx`
    MyPiePlots.print_pie_plot(len(list_of_positive), len(list_of_negative), len(list_of_neutral))
    MyWords.print_wordcloud(tweets['clean-text'].values, "All Words")
    MyWords.print_wordcloud(list_of_positive['clean-text'].values, "Positive Words")
    MyWords.print_wordcloud(list_of_negative['clean-text'].values, "Negative Words")
    MyWords.print_wordcloud(list_of_neutral['clean-text'].values, "Neutral Words")

    MyWords.print_wordcloud(list_of_very_positive_fg['clean-text'].values, "Very Positive ")
    MyWords.print_wordcloud(list_of_positive_fg['clean-text'].values, "Positive")
    MyWords.print_wordcloud(list_of_negative_fg['clean-text'].values, "Negative ")
    MyWords.print_wordcloud(list_of_very_negative_fg['clean-text'].values, "Very Positive ")

    MyEmotion.plot_emotion_sum(list_of_very_positive_fg['emotions'], "Very Positive tweets")
    MyEmotion.plot_emotion_sum(list_of_positive_fg['emotions'], "Positive tweets")
    MyEmotion.plot_emotion_sum(list_of_negative_fg['emotions'], "Negative tweets")
    MyEmotion.plot_emotion_sum(list_of_very_negative_fg['emotions'], "Very negative tweets")
    # #Pie Plot - Fine Grain
    MyPiePlots.print_pie_plot_fg(len(list_of_very_positive_fg), len(list_of_positive_fg), len(list_of_neutral_fg), len(list_of_negative_fg),len(list_of_very_negative_fg))

    count_vectorizer = CountVectorizer(stop_words='english')
    count_data = count_vectorizer.fit_transform((map(str,(tweets['clean-text'].values))))

    n2grams = MyTopNgrams.nGrams((2,2), tweets['clean-text'].values, 10)
    print('Top-10 most occurred bi-gram ', n2grams)
    n3grams = MyTopNgrams.nGrams((3,3), tweets['clean-text'].values, 10)
    print('Top-10 most occurred tri-gram ', n3grams)
    n4grams = MyTopNgrams.nGrams((4,4), tweets['clean-text'].values, 10)
    print('Top-10 most occurred four-gram', n4grams)
    #
    #
    MyPiePlots.plot_10_most_common_words(count_data, count_vectorizer)
    MyTopNgrams.top_words_count(count_vectorizer,count_data)

    MyLDA.LDA(count_data,count_vectorizer)