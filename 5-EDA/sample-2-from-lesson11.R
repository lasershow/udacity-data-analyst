#現在のパスを確認
#getwd()
#カレントディレクトリの変更
setwd("~/Downloads")
#read.csvでcsvの読み込み、stateInfo変数の読み込み
#横タブのenvironmentsで見ることができる→
#stateInfo <- read.csv('stateData.csv')
#情報の絞込
#stateSubset <- subset(stateInfo, state.region == 1)
#上記と同様
#stateSubsetBracket <- stateInfo[stateInfo$state.region == 1, ]

#redditのデータを読み込む
reddit <- read.csv('reddit.csv')

summary(reddit)
table(reddit$employment.status)

levels(reddit$age.range)

library(ggplot2)
qplot(data = reddit,x = age.range)
#qplot(data = reddit,x = income.range)

#順番に並べる
reddit$age.range <- factor(reddit$age.range, levels = c('Under-18','18-24','25-34',
                                                        '35-44','45-54','55-64', '65 of above', 'NA'))

