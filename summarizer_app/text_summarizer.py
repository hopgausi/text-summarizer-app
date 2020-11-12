import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
import re


class Summarizer:
    punct = re.compile(r'[!|,.:;()|0-9]')
    stop_words = stopwords.words('english')
    words_freqdist = FreqDist()
    sents_freqdsit = FreqDist()

    def summarize(self, text):
        words = word_tokenize(text)
        sentences = sent_tokenize(text)

        # removed punctuations
        words_post_punc = []
        for i in words:
            word = self.punct.sub("", i)
            if len(word) > 0:
                words_post_punc.append(word)

        # words frequency distribution
        for word in words_post_punc:
            if word not in self.stop_words:
                self.words_freqdist[word] += 1

        for sentence in sentences:
            for word, freq in self.words_freqdist.items():
                if word in sentence.lower():
                    self.sents_freqdsit[sentence] += 1

        val_sum = 0
        for sent in self.sents_freqdsit:
            val_sum += self.sents_freqdsit[sent]

        avg = int(val_sum / len(self.sents_freqdsit))

        summary = ""
        for sentence in sentences:
            if sentence in self.sents_freqdsit and self.sents_freqdsit[sentence] > (1.2 * avg):
                summary += " " + sentence
        return summary
