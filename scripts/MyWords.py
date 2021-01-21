import matplotlib.pyplot as plt
from wordcloud import WordCloud
class MyWords:

    def word_count(tmp):
        total_count = 0
        for i in tmp:
            total_count += len(i)
        return total_count / len(tmp)

    def word_subjectivity_avg(tmp):
        total_count = 0
        for i in tmp:
            total_count += i
        return total_count / len(tmp)

    def word_polarity_avg(tmp):
      total_count = 0
      for i in tmp:
            if(i!='-'):
                f = float(i)
                total_count += f
      return total_count / len(tmp)

    def word_count_positv(tmp):
        total_count = 0
        for i in tmp:
            print(i)
            if i.count("posit") > 0:
                total_count = total_count + 1
        return total_count

    def print_wordcloud(tweet, title):
        long_string = ','.join((map(str, tweet)))
        wordcloud = WordCloud(background_color="white", max_words=5000, contour_width=3, contour_color='steelblue')
        wordcloud.generate(long_string)
        plt.figure()
        plt.title(title)
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        plt.show()
