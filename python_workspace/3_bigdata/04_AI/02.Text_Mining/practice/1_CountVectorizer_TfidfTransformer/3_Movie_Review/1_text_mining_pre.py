import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
# 사용모델: 스타워즈 에피소드 4 대본(
#https://blog.naver.com/PostView.nhn?blogId=samsjang&logNo=
# 220982297456&redirect=Dlog&widgetTypeCall=true)

positive = '1\t' # 긍정 리뷰의 헤더는 1
negative = '0\t' # 부정 리뷰의 헤더는 0
documents = []
labels= []

with open('movie_review.txt','r',encoding='utf-8') as file:
    for line in file:
        if line.startswith(positive): # 긍정인 경우
            labels.append(1)
            # 1 abcdefg... => line[len(positive):] : abcdefg....
            documents.append(line[len(positive):])
        elif line.startswith(negative): # 부정인 경우
            labels.append(0)
            documents.append(line[len(negative):])

# CountVectorizer 클래스 : 문서를 단어 단위로 쪼개서 각 단어가 몇 번 나왔는지 세어 단어 카운팅 피처를 만든다.
count_vector = CountVectorizer()
# word_count :(데이터,특성)\t 카운트\n...
word_count = count_vector.fit_transform(documents)
# voca: 사용된 피처 단어 목록
voca = count_vector.get_feature_names()

# 위의 피처를 단어 빈도 피처로 변환
tf_transformer = TfidfTransformer(use_idf=False).fit(word_count)
features = tf_transformer.transform(word_count)
#추출된 데이터(단어, 빈도수, 레이블)을 저장
with open('pre_movie_review.pickle','wb') as file_handle:
    pickle.dump((labels,voca,features),file_handle)
