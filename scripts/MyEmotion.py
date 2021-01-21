from nrclex import NRCLex
import matplotlib.pyplot as plt
class MyEmotion:

    def find_main_emotion(text):
        emotion = NRCLex(text)
        if len(emotion.top_emotions) == 1:
            s =  emotion.top_emotions[0][0]
            listToStr=''.join(map(str, s))
            return listToStr
        elif len(emotion.top_emotions) == 2:
            s = emotion.top_emotions[0][0] + ' ' + emotion.top_emotions[1][0]
            listToStr=''.join(map(str, s))
            return listToStr
        else:
            max = emotion.top_emotions[0][1]
            max_str = emotion.top_emotions[0][0]
            listToStr=''.join(map(str, max_str))
            for i in range(len(text)):
                if emotion.top_emotions[i+1][i+1] > max:
                    max = emotion.top_emotions[i+1][i+1]
                    max_str = emotion.top_emotions[i+1][i+1]
                    listToStr = ''.join(map(str, max_str))
                return listToStr

    def print_emotion_sum(series):
        print(('Fear sum :', series.str.contains("fear").sum()))
        print(('Disgust sum :', series.str.contains("disgust").sum()))
        print(('Surprise sum :', series.str.contains("surprise").sum()))
        print(('Joy sum :', series.str.contains("joy").sum()))
        print(('Sadness sum :', series.str.contains("sadness").sum()))
        print(('Trust sum :', series.str.contains("trust").sum()))
        print(('Anticipation sum :', series.str.contains("anticipation").sum()))
        print(('Anger sum :', series.str.contains("anger").sum()))

    def plot_emotion_sum(series,title):
        num = [series.str.contains("fear").sum(), series.str.contains("disgust").sum(), series.str.contains("surprise").sum(), series.str.contains("joy").sum(), series.str.contains("sadness").sum(),
               series.str.contains("trust").sum(), series.str.contains("anticipation").sum(), series.str.contains("anger").sum()]
        fig = plt.figure()
        ax = fig.add_axes([0, 0, 1, 1])
        ax.axis('equal')
        emotions = ['Fear', 'Disgust', 'Surprise', 'Joy', 'Sadness', 'Trust', 'Anticipation', 'Anger']
        ax.pie(num, labels=emotions, autopct='%1.2f%%')
        plt.title(title)
        plt.show()