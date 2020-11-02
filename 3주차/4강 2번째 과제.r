score.name <- c("KOR","ENG", "MATH", "HIST", "SOC", "MUSIC", "BIO", "EARTH" ,"PHY",	"ART" ) 
score <- c(90, 85, 73, 80, 85, 65, 78, 50, 68, 96)
table(score) 
mean(score)
median(score)
sd(score)
var(score)
max(score)
score.name[which.max(score)]
boxplot(score) # 85점 넘거나 69.25보다 박으면 이상치에 해당 
quantile(score)

hist(score
    , main = "title : Hong's score"
    , col = "purple"
    )

wt = mtcars$wt
mean(wt)
median(wt)
mean(wt, trim = 0.15) # 절사평균
summary(wt)

cyl = mtcars$cyl
table(cyl)
barplot(cyl)

par(mfrow = c(1,3))
barplot(cyl)
hist(wt)
barplot(mtcars$gear)

boxplot(wt) # 평균값은 3 초반대 이고 최댓값이 5보다 큰 것에 비해 낮은 값들이 많이 분포 되어 있다. 
boxplot(mtcars$disp) # 평균값은 200 정도 인것에 비해 200 보다 큰값들이 많이 분포 되어 있다. 
