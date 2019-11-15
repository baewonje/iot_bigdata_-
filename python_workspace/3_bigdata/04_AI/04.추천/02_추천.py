from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import codecs

def read_data(fin, delim):
    info_li = []

    for line in codecs.open(fin,'r',encoding='latin-1'):
        line_items = line.strip().split(delim)

        key = int(line_items[0])

        if (len(info_li)+1) != key:
            print('errors at data_id')
            exit(0)
        info_li.append(line_items[1:])

    print('rows in %s: %d'%(fin, len(info_li)))

    return info_li

def similar_recommend_by_movie_id(movielens_id):
    movie_index = movielens_id-1
    similar_movies = sorted(list(enumerate(movie_sim[movie_index])),key=lambda x:x[1],reverse=True)
    recommended = 1
    print("---- recommendation for movie %d ----"%(movielens_id))
    for movie_info in similar_movies[1:6]:
        movie_title = movie_info_li[movie_info[0]]
        print('rank %d recommendation:%s'%(recommended,movie_title[0]))
        recommended += 1

f = open('movie_plot.bin','rb')
vectorizer2 = TfidfVectorizer(min_df = 2, stop_words=['of','is','this','that','which'])
movie_plot_li = pickle.load(f)
x = vectorizer2.fit_transform(movie_plot_li)
feature_names = vectorizer2.get_feature_names()

movie_sim = cosine_similarity(x)

fin_movie = 'ml-100k/u.item'
movie_info_li = read_data(fin_movie, '|')

similar_recommend_by_movie_id(1)