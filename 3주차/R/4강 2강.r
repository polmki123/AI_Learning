head(mtcars)
cartb <- mtcars[, "carb"]
table(cartb)
par(mfrow = c(1,3))
barplot(table(mtcars$carb)
        , main = "plot"
        , xlab = "ok"
        , ylab = "ko"
        , col  = "blue"
        # , names = ["ko". "vetor"]
)
barplot(table(cartb)
        , main = "plot"
        , xlab = "ok"
        , ylab = "ko"
        , col  = "blue"
        # , names = ["ko". "vetor"]
)
barplot(table(cartb)
        , main = "plot"
        , xlab = "ok"
        , ylab = "ko"
        , col  = "blue"
        # , names = ["ko". "vetor"]
)