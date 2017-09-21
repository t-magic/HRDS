# HRDS
[ホームページ](https://t-magic.github.io/HRDS/)  
[リポジトリー](https://github.com/t-magic/HRDS/)
[Wikiページ](https://github.com/t-magic/HRDS/wiki)
# 進め方
* 同じ項目をする人でペアになり、教え合いながら進めます。
* わからないところは多くの人が疑問を持つところですので、ペアで解決できないところは、みんなで解決していきます。

# 最初にすること
* 画像をクリックするとyoutubeの動画を視聴できます。

## 1. Jupyterのインストール
* HRDataScientistWG 03 Jupyterのインストール

 [![](https://i.ytimg.com/vi/xV2lnIInON8/hqdefault.jpg?sqp=-oaymwEXCPYBEIoBSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLAxy_mBn51kdTEOuP8zaK9ZqkAeyA)](https://youtu.be/xV2lnIInON8)
 * このyoutubeではPython3.5をインストールしていますが、最新版(3.6)をインストールしてください。
### 参考
 1. 環境変数の設定を確認する場合、[ここ](環境変数の確認.md)を参考にしてください。
 1. Jupyterの中でRを使用する場合は、[ここ](https://conda.io/docs/user-guide/tasks/use-r-with-conda.html)を参考にしてください。コマンドプロンプトで以下を実行します。
 ```
 > conda install r-essentials
 ```
 1. Jupyterの中でPython2.7も使用する場合は、[ここ](http://www.geocities.jp/penguinitis2002/computer/programming/Python/Anaconda_Python2_3.html)を参考にしてください。

## 2. (できれば)GitHubのアカウント作成
アカウント作成後、ユーザー名をサイト管理者(舘野)にお知らせください。
* How to Create a GitHub Account • A Quick Look

 [![](https://i.ytimg.com/vi/ezxRcdJ8glM/hqdefault.jpg?sqp=-oaymwEXCPYBEIoBSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLDAWj49JpX_ngEiLEeHfwMxTVM2Eg)](https://youtu.be/ezxRcdJ8glM)

または

* Git入門：GitHubのアカウントを作る｜lynda.com 日本版

 [![](https://i.ytimg.com/vi/RHj-859yXWo/hqdefault.jpg?sqp=-oaymwEXCPYBEIoBSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLDtN_loLgVpeY1SeQ2aY2xpR9bhCQ)](https://youtu.be/RHj-859yXWo?t=94)
* (先頭から1分34秒目～)

---

## 3. リポジトリーのダウンロード

### リポジトリーの場所
* 公開のものは、[https://github.com/t-magic/HRDS](https://github.com/t-magic/HRDS)にあります。
* 非公開(ユーザー名/パスワードが必要です)のものは、[https://github.com/t-magic/DSPR](https://github.com/t-magic/DSPR)にありますが、管理者がユーザー名を登録することでアクセスできるようになります。

### 解凍の際に文字化けする場合 (Windows)
* 以下のソフトを使って解凍すると文字化けしないようです。
  * CubeICE (http://www.cube-soft.jp/cubeice/index.php)
  * 7zip (https://sevenzip.osdn.jp/)

#### 3-1 GitHubのアカウントを作成しない場合
* [https://github.com/t-magic/HRDS](https://github.com/t-magic/HRDS)に行き、下図のようにして、ダウンロードしてください。

![](pict/HRDSpage.JPG)

---

#### 3-2 GitHubのアカウントを作成した場合
(アカウント作成後、管理者(舘野)にユーザー名を連絡し、管理者からの招待メールにあるURLをクリックした後、操作できます。)
* [https://github.com/t-magic/DSPR](https://github.com/t-magic/DSPR)に行き、下図のようにして、ダウンロードしてください。

![](pict/github_page.JPG)

#### 3-3 ポケドラを使用する場合
[こちら](ポケドラの接続.md)

### 3-4 GitHubのリポジトリーからクローンを作成する
[こちら](GitHubのリポジトリーからクローンを作成する.md)

---

## 4. JupyterでPandasを試す
  * 「 [Lesson_01_Pandasを使ってみよう](LessonPandas/Lesson_01_Pandasを使ってみよう.html) 」を参考にして、Jupyterで「 LessonPandas/Lesson_01_Pandasを使ってみよう.ipynb 」を開いて実行します。
  * 「 [Lesson_02_Pandasを使ってみよう2](LessonPandas/Lesson_02_Pandasを使ってみよう2.html) 」を参考にして、Jupyterで「 Lesson_02_Pandasを使ってみよう2.ipynb 」を開いて実行します。
  * 日本語の表示がうまくできない場合
    * 「 [LessonPandas/日本語フォントの設定_まとめ.html](LessonPandas/日本語フォントの設定_まとめ.html) 」を参考にして、「 LessonPandas/日本語フォントの設定_まとめ.ipynb 」を開いて実行します。

## 5. 構造方程式モデリングを試す
* JupyterにRが入っているか、PCにRが入っている必要があります。

[こちら](SEM.md)へ

## 6. クラスタリングを試す
  * [Clustering using K-Means with Titanic Dataset](Clustering/Clustering+using+K-Means+with+Titanic+Dataset.html)
  * [Trials of Flat and Hierarchical Clusterings with Titanic Data](Clustering/Trials+of+Flat+and+Hierarchical+Clusterings+with+Titanic+Data.html)

## 7. カテゴライズを試す
  * [Random_Forests_%3D%3D_Awesome](https://github.com/mbernico/CS570/blob/master/module_2/Random_Forests_%3D%3D_Awesome.ipynb)
