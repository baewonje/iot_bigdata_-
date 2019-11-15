x <- read.csv("C:/python_workspace/3_bigdata/03_Linear_Regression_Analysis/winequality-both.csv", header=TRUE)
y <- x[,13] # quality 열 추출
x <- x[,-1] # 첫번째 열을 빼고 나머지 열 추출
#hist(y)
#qqnorm(y)
#qqline(y, col=1)

#ks.test(y, "pnorm", mean = mean(y), sd = sd(y))

m <- lm(quality ~ ., data = x)
summary(m)
m2 <- step(m, direction = 'both')
summary(m2)
#res = residuals(m2)
#qqnorm(res)
#qqline(res, col=1)
#ks.test(res, "pnorm", mean = mean(res), sd = sd(res))

#m3 <- glm(quality ~ ., family = 'poisson', data = x)
#summary(m3)
#m4 <- step(m3, direction = 'both')
#summary(m4)

#x.pca <- prcomp(x, center = T, scale. = T)
#print(x.pca)
#plot(x.pca, type='l')

