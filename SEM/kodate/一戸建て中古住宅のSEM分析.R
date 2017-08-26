
#一戸建て中古住宅のSEM分析
#データの読み込み
#excelファイルから読み込む（テスト：AAA）　　Rのフォルダーに保存

library(xlsx)　　#ライブラリーの読み込み
 
m1<-read.xlsx("一戸建て中古住宅.xlsx",sheetName="AAA") 　#三原一戸建てデータ

#m1  #フレーム構造を確認する（出力する）
m1　　　#データ数が少ないので全データ表示させる

cor(m1)  #アンケート設問間の相関関係を確認する（出力する）

#因子分析
#library(psych)で因子分析する
library(psych)　　#ライブラリーの読み込み
library(GPArotation)

cortest.bartlett(m1) #Bartlettテスト

res2<-fa.parallel(m1,fa="pc") #因子数を算出する
res3<-fa(m1,fm="minres",nfactors=2,rotate="oblimin",scores=TRUE)
#print(res3,sort=TRUE,cut=.3)　　#大きさでソートする  　　　　　　
print(res3,cut=.2)　　　　　　　　#ソートなし
head(res3$scores)  #因子得点

alpha(m1)  #信頼性係数：クロンバックのα　0.8を超えること

#alpha(m1, keys=NULL,cumulative=FALSE, title=NULL, max=10,na.rm = TRUE,
#check.keys=FALSE,n.iter=1,delete=TRUE,use="pairwise")
omega(m1,2)  #信頼性計数：　ω係数
describe(m1)  #各列毎の統計値

#SEM分析
#lavaanモデル
library(lavaan)  #ライブラリーの読み込み

#モデル作り＜1＞
model.test1<-'
#測定モデル  なし

#回帰モデル
kakaku~nensu +tatemono +tochi　　　#販売価格（万円）　築年数（年）　建物面積（m2)  土地面積（m2)
tatemono~tochi

#残差の相関
 nensu ~~ tatemono　　#データ数が小さい場合は残差相関を入れると適合度指標が良くなる

'
#モデル作り＜2＞   #結局変数が少ない場合は潜在因子を使うとモデルが適切に出来ない
model.test1<-'
#測定モデル  
hirosa =~ tatemono +tochi
kachi =~ kakaku
furusa =~ nensu
#回帰モデル
kachi~hirosa+nensu

#残差の相関
 nensu ~~ tatemono　　#データ数が小さい場合は残差相関を入れると適合度指標が良くなる

'
#--------------------------------------------------------------------------------
#Rチュートリアルセミナーを参照（山口大学）
#関西大学資料参照
fit<-sem(model.test1,data=m1)
summary(fit,rsquare=TRUE,standardized=TRUE,fit.measures=TRUE,modindices=TRUE) 
#summary(fit,rsquare=TRUE,standardized=TRUE,fit.measures=TRUE) 　#修正インデックスなし
fitMeasures(fit,c("gfi","agfi","rmr"))

#パス図を描く
library(semPlot)　　#ライブラリーの読み込み
semPaths(fit,"std")



#終わり

 
