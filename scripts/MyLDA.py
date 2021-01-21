from sklearn.decomposition import LatentDirichletAllocation as LDA
from pyLDAvis import sklearn as sklearn_lda
import pickle
import pyLDAvis
import os
from sklearn.feature_extraction.text import CountVectorizer
import warnings
warnings.simplefilter("ignore", DeprecationWarning)
class MyLDA:

    def print_topics(model, count_vectorizer, n_top_words):
        words = count_vectorizer.get_feature_names()
        for topic_idx, topic in enumerate(model.components_):
            print("\nTopic #%d:" % topic_idx)
            print(" ".join([words[i] for i in topic.argsort()[:-n_top_words - 1:-1]]))

    def LDA(count_data, count_vectorizer):
        # Tweak the two parameters below
        number_topics = 35
        number_words = 20
        # Create and fit the LDA model
        lda = LDA(n_components=number_topics, n_jobs=-1)
        lda.fit(count_data)
        # Print the topics found by the LDA model
        print("Topics found via LDA:")
        MyLDA.print_topics(lda, count_vectorizer, number_words)

        LDAvis_data_filepath = os.path.join('./ldavis_prepared_' + str(number_topics))
        # # this is a bit time consuming - make the if statement True
        # # if you want to execute visualization prep yourself
        if 1 == 1:
            LDAvis_prepared = sklearn_lda.prepare(lda, count_data, count_vectorizer)
        with open(LDAvis_data_filepath, 'wb') as f:
            pickle.dump(LDAvis_prepared, f)

        # load the pre-prepared pyLDAvis data from disk
        with open(LDAvis_data_filepath, 'rb') as f:
            LDAvis_prepared = pickle.load(f)
        return pyLDAvis.save_html(LDAvis_prepared, './ldavis_prepared_' + str(number_topics) + '.html')