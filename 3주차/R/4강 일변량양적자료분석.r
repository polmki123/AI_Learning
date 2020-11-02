mydata <- c(50, 60, 100, 75, 200)
mydata.big <- c(mydata, 50000)
mean(mydata, trim = 0.2) # 절사평균 
table(mydata.big)
quantile(mydata.big, (0:10)/10)
summary(mydata)
fivenum(mydata)

diff(range(mydata)) # 두수의 차이 
var(mydata)
sd(mydata)


head(state.x77)
st.income <- state.x77[, "Income"]
boxplot(st.income)

head(iris)
boxplot(iris$Petal.Width)
boxplot(Petal.Width~Species, data = iris)

hist(st.income
    , border = "blue"
    , col = "green"
    , les = 3    # x 축 글씨 방향 
    , breaks = 5 # 막대의 개수 수가 적으면 넓게 자르는 것 
    )


score <- c(11,21,31,42,53,64,71)
stem(score, scale = 2)