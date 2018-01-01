#現在のパスを確認
getwd()
#カレントディレクトリの変更
setwd("~/Downloads")
#read.csvでcsvの読み込み、stateInfo変数の読み込み
#横タブのenvironmentsで見ることができる→
stateInfo <- read.csv('stateData.csv')
#情報の絞込
stateSubset <- subset(stateInfo, state.region == 1)

#上記と同様
stateSubsetBracket <- stateInfo[stateInfo$state.region == 1, ]

#redditのデータを読み込む