import requests
import json
from sklearn.feature_extraction.text import TfidfVectorizer

result_lines = []
movie_plot_li = []
movie_title_li = []

current_api_key = 'c863e960'
import codecs
import pickle

def read_data(fin, delim, mode='normal'):
    info_li = []

    index = 0
    for line in codecs.open(fin,'r',encoding='latin-1'):
        index += 1
        try:
            line_items = line.strip().split(delim)
            key = int(line_items[0])

            if (len(info_li)+1) != key:
                print('errors at data_id')
                print(f'index:(index)')
                exit(0)
            if mode=='plot':
                info_li.append(line_items[1])
            else:
                info_li.append(line_items[1:])
        except Exception as e:
            print(e)
            print(f'index:(index)')

    print('rows in %s: %d'%(fin, len(info_li)))

    return info_li

fin_move = 'ml-100k/u.item'
movie_plot_file = 'ml-100k/ml-100k-plot.txt'
movie_info_li = read_data(fin_move,'|')
movie_plot_li = read_data(movie_plot_file,'|',mode='plot')

print('download complete: %d movie data downloaded'%(len(movie_title_li)))
vectorizer = TfidfVectorizer(min_df=2,stop_words=['of','is','this','that','which'])
vectorizer.fit_transform(movie_plot_li)

feature_names = vectorizer.get_feature_names()
print(feature_names)

with open('movie_plot.bin','wb') as f:
    pickle.dump(movie_plot_li,f)

print('전처리 완료')