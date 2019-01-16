"""
英文情感分析
"""

from textblob import TextBlob
import pandas as pd


def judge(text):
    if text and isinstance(text, str):
        blob = TextBlob(text)
        sentiment = blob.sentiment
        return sentiment.polarity
    return ""


def text_compare(a, b):
    if abs(a - b) > 0.3:
        return False
    return True


def main():
    frame = pd.read_excel()
    frame["new_sentiment"] = frame.text.apply(judge)
    frame["old_sentiment"] = frame.old_text.apply(judge)
    frame["compare"] = frame.apply(lambda x: text_compare(x.new_sentiment, x.old_sentiment))


if __name__ == '__main__':
    main()
