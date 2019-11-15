import codecs
import numpy as np
from sklearn.metrics import mean_squared_error
from matplotlib import pyplot as plt

def read_data(fin, delim):
    info_li = []

    for line in codecs.open(fin,'r',encoding='latin-1'):
        line_items = line.strip().split(delim)

        key = int(line_items[0])

        if (len(info_li)+1) != key:
            print('errors ad data_id')
            exit(0)
        info_li.append(line_items[1:])

    print('rows in %s: %d'%(fin,len(info_li)))

    return info_li

# 교대 최소제곱법(Altering Least Square)을 활용한 손실 함수
def compute_ALS(R, test, n_iter, lambda_, k):
    '''임의의 사용자 요인 행렬 X와 임의의 영화 요인 행렬 T를 생성하고
    교대 최소제곱법을 이용하여 유틸리티 행렬 R을 근사합니다. 그후 test행렬을 이용하여 평가합니다.
    R(ndarray) : 유틸리티 행렬
    test: 평가행렬
    lambda_(float) : 정규화 파라미터
    n_iter(fint) : X와 Y의 갱신 횟수
    '''
    m,n = R.shape
    # m: 943(사용자수) , n: 1682(영화수)
    X = np.random.rand(m, k)
    Y = np.random.rand(k, n)
    errors = []
    # 갱신 시마다 계산한 에러를 저장합니다.
    for i in range(0, n_iter):
        X = np.linalg.solve(np.dot(Y, Y.T) +  lambda_ * np.eye(k), np.dot(Y, R.T)).T
        Y = np.linalg.solve(np.dot(X.T, X) + lambda_ * np.eye(k), np.dot(X.T, R))
        error_val = get_test_mse(test, np.dot(X,Y))
        errors.append(error_val)
        print('Error of rated movies: %.5f' %(error_val))

    R_hat = np.dot(X,Y)
    print('Final Error of rated movies: %.5f' % (get_test_mse(test, R_hat)))
    return(R_hat, errors)

# n_test 숫자만 큼 test 셋을 만들고 훈련셋에서는 test셋을 제외한다.
def train_test_split(R, n_test):
    train = R.copy()
    # 모든 향이 0으로 채워진 학습용 별점 행렬을 만듭니다.
    test = np.zeros(R.shape)

    for user in range(R.shape[0]):
        # 각 사용자마다 n_test개의 0이 아닌 항(사용자가 입력한 별점)을 입의로 골라
        # 인덱스를 기억합니다.
        test_index = np.random.choice(R[user, :].nonzero()[0], size=n_test,replace=False)

        # 위에서 정한 인덱스에 해당하는 별점을 0으로 만듭니다.
        train[user, test_index] = 0

        # 평가 데이터 행렬의 해당 인덱스에 사용자가 입력한 실제 별점을 입력합니다.
        test[user, test_index] = R[user, test_index]
    return(train, test)

# 예제 12-13
def get_test_mse(true, pred):
    # 학습-평가 데이터에서 0이 ㅎ아닌 값만 이용해서 에러를 계산합니다.
    # true가 평가 데이터, pred가 학습 데이터입니다.
    # 평가 데이터가 0이 아닌 항들의 인덱스에 해당하는 점수만 추출합니다.
    pred = pred[true.nonzero()].flatten()
    true = true[true.nonzero()].flatten()
    return mean_squared_error(true, pred)

def recommend_by_user(user):
    # 사용자의 ID를 입력으로 받아 그 사용자가 보지 않은 영화를 추천합니다.
    user_index = user-1
    user_seen_movies = sorted(list(enumerate(R_hat[user_index])),key=lambda x:x[1], reverse=True)
    recommended = 1
    print("----- recommendation for user %d ----"%(user))
    for u, movie_info in enumerate(user_seen_movies):
        if W[u][movie_info[0]] == 0:
            # movie_title = movie_info_dic[str(movie_info[0]+1]
            movie_title = movie_info_dic[movie_info[0]]
            movie_score = movie_info[1]
            #  print("rank%d recommendation:%s(%.3f)"
            #  %(recommended,movie_title[0], movie_score))
            print("rank %d recommendation:%s(%.3f)"
                  %(recommended,movie_title,movie_score))
            recommended += 1
        if recommended == 6:
            break
fin_user = 'ml-100k/u.user'
fin_movie = 'ml-100k/u.item'

user_info_li = read_data(fin_user, '|')
movie_info_li = read_data(fin_movie, '|')
movie_info_dic = {}
for index, movie_info in enumerate(movie_info_li):
    movie_info_dic[index] = movie_info[0]

R = np.zeros((len(user_info_li), len(movie_info_li)), dtype=np.float64)

for line in codecs.open('ml-100k/u.data','r',encoding='latin-1'):
    user, movie, rating, date = line.strip().split('\t')
    user_index = int(user)-1
    movie_index = int(movie)-1

    R[user_index, movie_index]=float(rating)

train, test = train_test_split(R,10)
num_of_iteration = 20
# num_of_iteration = 4
R_hat, train_errors =compute_ALS(train, test, num_of_iteration, 0.1, 100)

plt.xlim(0, num_of_iteration) # x축의 표시 범위를 0-20까지 설정(2020은 반복 횟수입니다.)
plt.ylim(0,15) # y축의 표시 범위를 0-15까지 설정
plt.xlabel('iteration')
plt.ylabel('MSE')
plt.xticks(range(num_of_iteration), range(0,20)) # x축에 표시할 숫자를 0부터 19까지의 정수로 함

# 학습 에러를 실선으로 표시
train_plot, = plt.plot(range(num_of_iteration),train_errors, label='train_error')

plt.legend(handles=[train_plot]) # 범례 생성
plt.show()

# 근사 행렬의 가장 작은 값을 0으로 만들고자 전체 항의 값에서 작은 값을 뺍니다.
R_hat -= np.min(R_hat)

# 근사 행렬의 가장 큰 값을 5로 만들고자 5를 가장 큰 예측값(np.max(R_hat))으로 나눈 값을 곱합니다.
# 예를 들어 가장 큰예측값이 3일 경우 3을 5로 만들기 위해서는 5/3을 곱하면 됩니다.
# 위에서 구한 값을 예측 행렬의 모든 항에 곱합니다.
R_hat *= float(5) / np.max(R_hat)

W = R>0.0
# 본 영화는 1
W[W==True] = 1
# 안 본영화는 0
W[W == False] = 0
W = W.astype(np.float64, copy=False)

recommend_by_user(1)