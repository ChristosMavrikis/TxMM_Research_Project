from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
class MyTopNgrams:

        def top_words_count(count_vectorizer, count_data):
            count_vect_df = pd.DataFrame(count_data.toarray(), columns=count_vectorizer.get_feature_names())
            count_vect_df.head()
            count = pd.DataFrame(count_vect_df.sum())
            countdf = count.sort_values(0, ascending=False).head(20)
            print('Exact number of Top-10 occurences', countdf[1:11])
            return

        def nGrams(range, list, n=None):
            vec = CountVectorizer(ngram_range=range, stop_words='english').fit((map(str,(list))))
            bag_of_words = vec.transform((map(str,(list))))
            sum_words = bag_of_words.sum(axis=0)
            words_freq = [(word, sum_words[0, idx]) for word, idx in vec.vocabulary_.items()]
            words_freq = sorted(words_freq, key=lambda x: x[1], reverse=True)
            return words_freq[:n]
