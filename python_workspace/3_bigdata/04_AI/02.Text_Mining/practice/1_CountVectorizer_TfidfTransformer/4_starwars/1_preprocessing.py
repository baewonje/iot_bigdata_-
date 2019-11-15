import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
# 사용모델: 스타워즈 에피소드 4 대본(
#https://www.kaggle.com/xvivancos/star-wars-movie-scripts)

# 종속변수: 등장인물들의 이름 여기서는 주인공  luke의 대사에 따른 인물이름 추측
protagonist_header=' LUKE'
documents = []
labels= []
# 고정변수: 각 캐릭터들의 대사
# luke의 대사는 labels 을 1을 주고 그외인물은 0을 준다.
with open('sw_ep','r',encoding='utf-8') as file_handle:
    for line in file_handle:
        if line.startswith(protagonist_header):
            labels.append(1)
            documents.append(line[len(protagonist_header)+1:])
        else:
            cnt = 0
            for line2 in line:
                cnt += 1
                if line2 == ',':
                    break
            labels.append(0)
            documents.append(line[cnt:])

# 텍스트문장을 벡터로 구성(단어 추출)
vectorizer = CountVectorizer()
term_conunts = vectorizer.fit_transform(documents)
vocabulary = vectorizer.get_feature_names()

tf_transformer = TfidfTransformer(use_idf=False).fit(term_conunts)
features = tf_transformer.transform(term_conunts)
#추출된 데이터(단어, 빈도수, 레이블)을 저장
with open('processed.pickle','wb') as file_handle:
    pickle.dump((vocabulary,features,labels),file_handle)
