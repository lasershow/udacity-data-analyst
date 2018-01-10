setwd("~/Downloads")

library(ggplot2)
data(diamonds)

qplot(data=diamonds, x=carat, y=price,
      xlim= c(0, quantile(diamonds$carat, 0.99)),
      ylim= c(0, quantile(diamonds$price, 0.99))) + 
  geom_point(fill= I('#F79420'), color = I('black'), shape = 21)

ggplot(data=diamonds, aes(x=carat, y=price)) + 
    scale_x_continuous(lim = c(0, quantile(diamonds$carat, 0.99))) + 
    scale_y_continuous(lim = c(0, quantile(diamonds$price, 0.99))) +
    geom_point(fill= I('#F79420'), color = I('black'), shape = 21)

#→非線形の関係性、指数的な関係性

ggplot(data=diamonds, aes(x=carat, y=price)) + 
  geom_point(color= I('#F79420'), alpha=1/4) + 
  stat_smooth(method = "lm") + 
  scale_x_continuous(lim = c(0, quantile(diamonds$carat, 0.99))) +
  scale_y_continuous(lim = c(0, quantile(diamonds$price, 0.99)))

# これだと、指数関数的に増加するデータを表すことができていない

# install these if necessary
install.packages('GGally')
install.packages('scales')
install.packages('memisc')
install.packages('lattice')
install.packages('MASS')
install.packages('car')
install.packages('reshape')
install.packages('plyr')

# load the ggplot graphics package and the others
library(ggplot2)
library(GGally)
library(scales)
library(memisc)

# sample 10,000 diamonds from the data set
#set.seed(20022012)
#diamond_samp <- diamonds[sample(1:length(diamonds$price), 10000), ]
#ggpairs(diamond_samp, params = c(shape = I('.'), outlier.shape = I('.')))

ggpairs(diamond_samp,
        lower = list(continuous = wrap("points", shape = I('.'))),
        upper = list(combo = wrap("box", outlier.shape = I('.'))))


# ダイヤモンドの需要により、指数関数的なデータの多さにつながっている

library(gridExtra)



qplot(data=diamonds, x = price, binwidth = 100, fill= I("#099DD9")) + 
  ggtitle('Price')

qplot(data=diamonds, x = price, binwidth = 0.01, fill= I("#F79420")) +
  ggtitle('Price (log10)') + 
  scale_x_log10()



plot1 <- qplot(data=diamonds, x = price, binwidth = 100, fill= I("#099DD9")) + 
  ggtitle('Price')

plot2 <- qplot(data=diamonds, x = price, binwidth = 0.01, fill= I("#F79420")) +
  ggtitle('Price (log10)') + 
  scale_x_log10()

library(gridExtra)
library(grid)
grid.arrange(plot1, plot2, ncol=2)

# 双峰型 → 豊かさが2グループある

qplot(data=diamonds, x=carat,y=price) + 
  scale_y_continuous(trans = log10_trans()) + 
  ggtitle("Price (log10) by Carat")


cuberoot_trans = function() trans_new('cuberoot', transform = function(x) x^(1/3),
                                      inverse = function(x) x^3)

ggplot(aes(carat, price), data = diamonds) + 
  geom_point() + 
  scale_x_continuous(trans = cuberoot_trans(), limits = c(0.2, 3),
                     breaks = c(0.2, 0.5, 1, 2, 3)) + 
  scale_y_continuous(trans = log10_trans(), limits = c(350, 15000),
                     breaks = c(350, 1000, 5000, 10000, 15000)) +
  ggtitle('Price (log10) by Cube-Root of Carat')

### Overplotting Revisited

head(sort(table(diamonds$carat), decreasing = T))
head(sort(table(diamonds$price), decreasing = T))

# どこが密なのかを調べることができる

ggplot(aes(carat, price), data = diamonds) + 
  geom_point(alpha = 0.5, size = 0.75, position = 'jitter') + 
  scale_x_continuous(trans = cuberoot_trans(), limits = c(0.2, 3),
                     breaks = c(0.2, 0.5, 1, 2, 3)) + 
  scale_y_continuous(trans = log10_trans(), limits = c(350, 15000),
                     breaks = c(350, 1000, 5000, 10000, 15000)) +
  ggtitle('Price (log10) by Cube-Root of Carat')
