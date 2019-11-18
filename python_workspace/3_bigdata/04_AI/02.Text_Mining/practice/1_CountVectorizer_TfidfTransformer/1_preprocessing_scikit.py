import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
# 사용 모델 : 싸이키런(sklearn)
#  고정 변수 항목 : 형태소에서 추출된 vocabulary, 단어 빈도
#  분석 목표(예측 값): 스팸 메일 판별
# 데이터 출처 : https:archive.ics.uci.edu/ml/datasets/SMS+Spam+Collection

spam_header = 'spam\t'
no_spam_header = 'ham\t'
documents = []
labels= []

with open('SMSSpamCollection','r',encoding='utf-8') as file_handle:
    for line in file_handle:
        # 각 줄에서 레이블 부분만 떼어내고 나머지를 documents에 넣는다.
        if line.startswith(spam_header):
            labels.append(1)
            documents.append(line[len(spam_header):])
        elif line.startswith(no_spam_header):
            labels.append(0)
            documents.append(line[len(no_spam_header):])

# 희소 행렬(Sparse Matrix)  => Compressed sparse Matrix
#  | 1 0 0 0 2 0 |              | 0 0 1 |
#  | 0 0 0 3 0 0 |              | 0 4 2 |
#  | 0 0 0 4 5 0 |              | 1 3 3 |
#  | 6 0 0 0 0 0 |              | 2 3 4 |
#  | 0 0 0 0 0 7 |              | 2 5 6 |
#  | 0 8 0 0 0 0 |              | 3 0 6 |
#                               | 4 5 7 |
#                               | 5 1 8 |

vectorizer = CountVectorizer() # 단어 횟수 피처를 만드는 클래스
term_count = vectorizer.fit_transform(documents) # 문서에서 단어 횟수세기
vocabulary = vectorizer.get_feature_names()

# 단어 횟수 피처에서 단어 빈도 피처를 만드는 클래스
# 단어 빈도(term frequency)가 생성
# TF: Term Frequency (문서상에 발견된 단어) / (전체 문서상의 단어)
# IDF: Inverse Document Frequency
#       (주요언어: is, of, that 같은 단어는 제외하고 빈도를 측정한다.)
tf_transformer = TfidfTransformer(use_idf=False).fit(term_count)
features = tf_transformer.transform(term_count)

#처리된 을 저장
with open('processed.pickle','wb') as file_handle:
    pickle.dump((vocabulary, features, labels),file_handle)