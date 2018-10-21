'''

Generate HTML code for word cloud

'''

import pandas as pd
import random
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer


class WordCloud:

    def __init__(self):
        self.data = []
        self.color_choices = ['#b82c2c',
                              '#a55571',
                              '#bc72d0',
                              '#8000FF',
                              '#3498DB',
                              '#FF5733',
                              '#223AE6',
                              '#2ECC71',
                              '#5F6A6A',
                              '#6C22E6',
                              '#CE22E6',
                              '#ACB02E',
                              '#B18904',
                              '#848484',
                              '#04B404',
                              '#5882FA',
                              '#FF0080',
                              '#0489B1',
                              '#FA5858',
                              '#DBA901',
                              '#00b4ff',
                              '#008080',
                              '#003366',
                              '#725394'
                              ]

        # load a set of stop words
        self.stopwords = self.get_stop_words("stopwords.txt")

    def get_color_code(self, score):
        """Get the appropriate color codes."""

        step = 0.05
        current_incremented_score = 0
        idx = 0

        while current_incremented_score < 1:
            if score <= current_incremented_score:
                return self.color_choices[idx]
            idx += 1
            current_incremented_score = current_incremented_score + step

        return self.color_choices[0]

    def get_font_size(self, score: float):
        """Increment scale until score almost equals current_incremented_score."""

        # font size start and increment
        scale = 0.6
        max_scale = 3.0
        scale_step = 0.3

        # score increment
        score_step = 0.05
        current_incremented_score = 0

        while current_incremented_score < 1 and scale < max_scale:

            # increment scale until score almost equals current_incremented_score
            # the larger the score, the more the scale increment
            if score <= current_incremented_score:
                return scale

            current_incremented_score = current_incremented_score + score_step
            scale += scale_step

            if scale > max_scale:
                scale = max_scale

        return scale

    def get_embed_code(self, text: list, topn=100, random_color=True):

        items = self.extract_topn_from_vector(text, topn=topn)
        new_df = pd.DataFrame(items, columns=['words', 'score'])

        if random_color:
            random.shuffle(self.color_choices)

        html = []
        words_colors = []

        html = [
            "<div align='center' style='width:100%'><div align='center' style='text-align:justify; border-radius: 25px;background: #fff7f7;overflow: auto; width:500px !important; padding:20px; '; text-align: center; word-wrap: break-word;>"]
        for idx, row in new_df.iterrows():
            word = row.words.replace(" ", "-")
            scale = self.get_font_size(row.score)
            color_code = self.get_color_code(row.score)
            words_colors.append(
                " <span style='color:{0};font-size:{1}em;white-space: normal;font-family:verdana;display: inline-block;line-height:20px'>{2}&nbsp;</span>".format(
                    color_code, scale, word))

        random.shuffle(words_colors)

        html.extend(words_colors)
        html.append("</div></div>")
        return ''.join(html)

    def sort_coo(self, coo_matrix):
        tuples = zip(coo_matrix.col, coo_matrix.data)
        return sorted(tuples, key=lambda x: (x[1], x[0]), reverse=True)

    def get_stop_words(self, stop_file_path):
        """Load stop words."""

        with open(stop_file_path, 'r', encoding="utf-8") as f:
            stopwords = f.readlines()
            stop_set = set(m.strip() for m in stopwords)
            return frozenset(stop_set)

    def extract_topn_from_vector(self, text: list, topn=10):
        """Extract keywords based on tf-idf score."""

        # get word count
        cv = CountVectorizer(stop_words=self.stopwords)
        word_count_vector = cv.fit_transform(text)

        # concatenate all texts
        big_text = ' '.join(text)

        # compute word scores
        tfidf_transformer = TfidfTransformer(smooth_idf=True, use_idf=True)
        tfidf_transformer.fit(word_count_vector)
        tf_idf_vector = tfidf_transformer.transform(cv.transform([big_text]))

        # sort the tf-idf vectors by descending order of scores
        sorted_items = self.sort_coo(tf_idf_vector.tocoo())

        # use only topn items from vector
        sorted_items = sorted_items[:topn]

        final_items = []

        # word index and corresponding tf-idf score
        for idx, score in sorted_items:
            final_items.append([cv.get_feature_names()[idx], score])

        return final_items
