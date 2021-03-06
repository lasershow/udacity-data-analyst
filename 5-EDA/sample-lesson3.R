setwd("~/Downloads")
list.files()
pf <- read.delim('pseudo_facebook.tsv') 
names(pf)

library(ggplot2)
#qplot(x=dob_day, data=pf) + 
#  scale_x_discrete(breaks=1:31)

ggplot(aes(x = dob_day), data = pf) +
  geom_histogram(binwidth = 1) +
  scale_x_continuous(breaks = 1:31)

# ヒストグラムを見て何に気づいたか 1日と31日

ggplot(data = pf, aes(x = dob_day)) +
  geom_histogram(binwidth = 1) +
  scale_x_continuous(breaks = 1:31) +
  facet_wrap(~dob_month)

# ヒストグラムを見て何に気づいたか 1月1

ggplot(aes(x = friend_count), data = pf) +
  geom_histogram()


ggplot(aes(x = friend_count), data = pf) +
  geom_histogram() +
  scale_x_continuous(limits = c(0, 1000))

ggplot(aes(x = friend_count), data = pf) +
  geom_histogram(binwidth = 25) +
  scale_x_continuous(limits = c(0, 1000), breaks = seq(0, 1000, 50))

ggplot(aes(x = friend_count), data = pf) +
  geom_histogram() +
  scale_x_continuous(limits = c(0, 1000), breaks = seq(0, 1000, 50)) +
  facet_wrap(~gender)

ggplot(aes(x = friend_count), data = subset(pf, !is.na(gender))) +
  geom_histogram() +
  scale_x_continuous(limits = c(0, 1000), breaks = seq(0, 1000, 50)) +
  facet_wrap(~gender)

table(pf$gender)
by(pf$friend_count, pf$gender, summary)

ggplot(aes(x = tenure), data = pf) +
  geom_histogram(binwidth = 30, color = 'black', fill = '#099DD9')

ggplot(aes(x = tenure/365), data = pf) +
  geom_histogram(binwidth = .25, color = 'black', fill = '#F79420')


ggplot(aes(x = tenure / 365), data = pf) +
  geom_histogram(color = 'black', fill = '#F79420') +
  scale_x_continuous(breaks = seq(1, 7, 1), limits = c(0, 7)) +
  xlab('Number of years using Facebook') +
  ylab('Number of users in sample')

ggplot(aes(x = age), data = pf) +
  geom_histogram(binwidth = 1, fill = '#5760AB') +
  scale_x_continuous(breaks = seq(0, 113, 5))

# log

summary(log10(pf$friend_count))
summary(sqrt(pf$friend_count))

install.packages('gridExtra')
library(gridExtra)

p1 <- qplot(x = friend_count, data=pf)
p2 <- qplot(x = log10(friend_count), data=pf)
p3 <- qplot(x = sqrt(friend_count), data=pf)
grid.arrange(p1,p2,p3,ncol=1)

p1 <- ggplot(aes(x=friend_count),data=pf) + geom_histogram()
p2 <- p1 + scale_x_log10()
p3 <- p1 + scale_x_sqrt()

ggplot(aes(x = friend_count, y = ..count../sum(..count..)),
       data = subset(pf, !is.na(gender))) +
  geom_freqpoly(aes(color = gender), binwidth=10) +
  scale_x_continuous(limits = c(0, 1000), breaks = seq(0, 1000, 50)) +
  xlab('Friend Count') +
  ylab('Proportion of users with that friend count')

ggplot(aes(x = www_likes), data = subset(pf, !is.na(gender))) +
  geom_freqpoly(aes(color = gender)) +
  scale_x_log10()

by(pf$www_likes, pf$gender, sum)

qplot(x=gender, y=friend_count,data=subset(pf, !is.na(gender)),geom = 'boxplot', ylim = c(0,1000))

qplot(x=gender, y=friend_count,data=subset(pf, !is.na(gender)),
      geom = 'boxplot', ylim = c(0,1000)) +
  scale_y_continuous(limits = c(0,1000))

qplot(x=gender, y=friendships_initiated,data=subset(pf, !is.na(gender)),
      geom = 'boxplot') +
  coord_cartesian(ylim  = c(0,150))

by(pf$friendships_initiated, pf$gender, summary)
