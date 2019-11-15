import os
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# 사용 모델 : 싸이키런(sklearn)
#  분석 목표(예측 값): 85%
# 데이터 출처 : https://ai.stanford.edu/~amaas/data/sentiment/ (university of stanford a.i laboratory)

documents = []
labels= []

file_list_neg = os.listdir("./neg")
for a in range(len(file_list_neg)):
        labels.append(0)  # 부정적인 평가의 라벨
for a in file_list_neg:
    with open('./neg/%s'% a, 'r',encoding='utf-8') as fp:
        k = fp.read()
        documents.append(k)

file_list_neg = os.listdir("./pos")
for a in range(len(file_list_neg)):
        labels.append(1)  # 부정적인 평가의 라벨
for a in file_list_neg:
    with open('./pos/%s'% a, 'r',encoding='utf-8') as fp:
        k = fp.read()
        documents.append(k)

vectorizer = CountVectorizer() # 단어 횟수 피처를 만드는 클래스
term_count = vectorizer.fit_transform(documents) # 문서에서 단어 횟수세기
vocabulary = vectorizer.get_feature_names()

# 단어 횟수 피처에서 단어 빈도 피처를 만드는 클래스
# 단어 빈도(term frequency)가 생성
tf_transformer = TfidfTransformer(use_idf=False).fit(term_count)
features = tf_transformer.transform(term_count)

#처리된 을 저장
with open('processed.pickle','wb') as file_handle:
    pickle.dump((vocabulary, features, labels),file_handle)

train_features, test_features, train_labels, test_labels = \
    train_test_split(features, labels)

# 학습
classifier = LogisticRegression()
classifier.fit(train_features, train_labels)

print('train accuracy: %4.4f'%classifier.score(train_features,train_labels))
print('test accuracy: %4.4f'%(classifier.score(test_features,test_labels)))

# 어떤 항목이 판별에 영향을 많이 줬는지 알아보기
weights=classifier.coef_[0, :]
pairs=[]
for index, value in enumerate(weights):
    pairs.append( (abs(value),vocabulary[index]))
pairs.sort(key=lambda x:x[0], reverse=True)
for pair in pairs[:20]:
    print('score: %4.4f, word : %s' % pair)

# train accuracy: 0.8834
# test accuracy: 0.8630
# score: 10.3251, word : worst
# score: 9.8813, word : bad
# score: 8.6600, word : great
# score: 7.0295, word : awful
# score: 7.0219, word : excellent
# score: 6.9752, word : boring
# score: 6.8002, word : waste
# score: 6.4160, word : terrible
# score: 5.8395, word : nothing
# score: 5.8166, word : poor
# score: 5.4981, word : best
# score: 5.3183, word : perfect
# score: 5.0471, word : minutes
# score: 5.0031, word : wonderful
# score: 4.8806, word : loved
# score: 4.6098, word : amazing
# score: 4.4913, word : stupid
# score: 4.4351, word : dull
# score: 4.3377, word : horrible
# score: 4.2817, word : script
#