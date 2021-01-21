import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
sns.set_style('whitegrid')
class MyPiePlots:
    def print_pie_plot(x1, x2, x3):
        fig = plt.figure()
        ax = fig.add_axes([0, 0, 1, 1])
        ax.axis('equal')
        Sent = ['Positive', 'Negative', 'Neutral']
        num = [x1, x2, x3]
        ax.pie(num, labels=Sent, autopct='%1.2f%%')
        plt.show()

    def print_pie_plot_fg(x1, x2, x3, x4, x5):
        fig = plt.figure()
        ax = fig.add_axes([0, 0, 1, 1])
        ax.axis('equal')
        Sent = ['Very Positive', 'Positive', 'Neutral', 'Negative', 'Very Negative']
        num = [x1, x2, x3, x4, x5]
        ax.pie(num, labels=Sent, autopct='%1.2f%%')
        plt.show()

    def plot_10_most_common_words(count_data, count_vectorizer):
        import matplotlib.pyplot as plt
        words = count_vectorizer.get_feature_names()
        total_counts = np.zeros(len(words))
        for t in count_data:
            total_counts += t.toarray()[0]

        count_dict = (zip(words, total_counts))
        count_dict = sorted(count_dict, key=lambda x: x[1], reverse=True)[0:20]
        words = [w[0] for w in count_dict]
        counts = [w[1] for w in count_dict]
        x_pos = np.arange(len(words))

        plt.figure(2, figsize=(15, 15 / 1.6180))
        plt.subplot(title='10 most common words')
        sns.set_context("notebook", font_scale=1.25, rc={"lines.linewidth": 2.5})
        sns.barplot(x_pos, counts, palette='husl')
        plt.xticks(x_pos, words, rotation=90)
        plt.xlabel('words')
        plt.ylabel('counts')
        plt.show()