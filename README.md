# Sentiment Analysis and Topic Modelling On COVID-19 Tweets
This project's purpose is to perform sentiment analysis and topic modelling on COVID-19 tweets in order to determine the public's overall reaction to the newly presented pandemic. The project uses a dataset from Kaggle specifically : https://www.kaggle.com/gpreda/covid19-tweets and performs basic methods to get a legitimate output for each research question given in the paper. A future extension of this code and project could be implementing my own sentiment analysis function instead of using ready implemented functions, as I believe they are obeselte for sentiment analysis on pandemic related Tweets.

The script was implemented on Pycharm Community and followed several steps from different tutorials as this is my first ever Text Mining project. To run the script just pip install all the dependcies listed in the 'Libraries Used' part of this file.


# General Information about the project
This is a repository for the Research Project for the Text and Multimedia Mining course. It contains the scripts used for the project and plots that could not be added to the final report. It also contains a .pdf with difficulties I encountered during the project. I have tried to record every step and phase of the project.

Subject : Sentiment Analysis and Topic Modelling On COVID-19  Tweets  <br />
Programming Language : Python 3.8  <br />
Libraries Used: The imported Python libraries for the project are listed below.
* Pandas
* NLTK
* Warnings
* PorterStemmer
* Vader for sentiment analysis (Vader is preferred for social media sentiment analysis)
* Textblob 
* NRClex
* Matplotlib
* Re
* Sklearn ~ Latent Dirichlet Allocation
* PyLDAvis
* Pickle
* Os
* Wordcloud
* Numpy
* Seaborn
* Imported .py scripts imported by author : MyEmotions, MyTopNgrams, MyFunctions, MyLDA , MyWords , MyPiePlots
Semester : 2020-2021

# Figures
In the Figures - Lemmatization folder you can find images/txt of the results of the project. The results are plotted using matplotlib and contain output about the sentiment, emotions , most common words, the topics, the n-grams, polarity and subjectivity of the Tweets. More specifically:
 * Figure 1 : Pie plot containing a general sentiment analysis of the Tweets.
 * Figure 2 : Wordcloud containing all the words from all the Tweets.
 * Figure 3 : Wordcloud containing all the words from the list of positive Tweets.
 * Figure 4 : Wordcloud containing all the words from the list of negative Tweets.
 * Figure 5 : Wordcloud containing all the words from the list of neutral Tweets.
 * Figure 6 : Pie plot containing the fine-grain sentiment analysis of the Tweets.
 * Figure 7 : Bar plot containing the most common words in the topics.
 * Figure 8 : Pie plot containing the emotions captured from the Tweets - positive,negative not contained.
 * Figure 9 : Pie plot containing the emotions captured form the list of positive Tweets.
 * Figure 10: Pie plot containing the emotions captured from the list of negative Tweets.
 * Figure 11: Pie plot containing the emotions captured from the list of neutral Tweets.
 * Figure 12: Wordclould containing all the words from the list of Very positive Tweets (after fine-grain sentiment analysis)
 * Figure 13: Wordclould containing all the words from the list of positive Tweets (after fine-grain sentiment analysis)
 * Figure 14: Wordclould containing all the words from the list of negative Tweets (after fine-grain sentiment analysis)
 * Figure 15: Wordclould containing all the words from the list of Very negative Tweets (after fine-grain sentiment analysis)
 * Figure 16: Pie plot containing the emotions captured form the list of Very positive Tweets (after fine-grain sentiment analysis)
 * Figure 17: Pie plot containing the emotions captured form the list of  positive Tweets (after fine-grain sentiment analysis)
 * Figure 18: Pie plot containing the emotions captured form the list of negative Tweets (after fine-grain sentiment analysis)
 * Figure 19: Pie plot containing the emotions captured form the list of Very negative Tweets (after fine-grain sentiment analysis)
 * Average Polarity.txt : Display the polarity of list of all, positive,negative,neutral Tweets (no fine-grain)
 * Average subjectivity.txt : Display the subjectivity of list of all , positive, negative, neutral Tweets (no fine-grain)
 * Average sentence length.txt : Display the average lenght of positive, negative and neutral Tweets (no fine-grain)
 * nGrams.txt : Display the most common bi-grams, tri-grams and four-grams in the Tweets.
 * Sum of emotions.txt : Display the sum of each emotion - excluding negative-positive- for all Tweets.
 (The plain Figure folder contains less results of the initial script which followed stemming instead of lemmatization)

# pyLDAvis
Contains images of the visualization of the runs for each number of fixed topics. HTML scripts will be added.

# Scripts
Containts the project's script used

# Encountered Problems 
I also have attached a .pdf which briefly explains each 'hiccup' I encountered throughtout the project.

# Timeline
I have added a timeline which shows the brief steps take to implement the project.
# Runtime
* Processor : Intel (R) Core (TM) i5-8265U CPU @ 1.60GHz 1.80GHz
* RAM : 8.00 GB (7.82 usable) <br />
With the above specs it takes about 1-2h to run 100k tweets for the analysis.
