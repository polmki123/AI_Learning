head(infert)
edu <- infert[, "education"]
unique(edu)
table(edu)
barplot(table(edu)
        , main = "plot"
)
