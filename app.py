# -*- coding: utf-8 -*-
import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)

# 读取电影数据（u.item 是竖线分隔）
# 字段：id, title, release_date, video_release_date, IMDb_URL, 类型（19个0/1）
columns = ['id', 'title', 'release_date', 'video_release_date', 'imdb_url'] + [f'genre_{i}' for i in range(19)]
movies = pd.read_csv('u.item', sep='|', names=columns, encoding='latin-1')

# 提取类型列（前5个类型）
genre_cols = [f'genre_{i}' for i in range(5)]
genre_names = ['unknown', 'Action', 'Adventure', 'Animation', 'Children']

# 构造类型向量
for i, name in enumerate(genre_names):
    movies[name] = movies[genre_cols[i]]

# 简化：只保留id, title, 类型列
movies = movies[['id', 'title'] + genre_names]

# 推荐函数：根据输入电影标题，返回相同类型的电影
def recommend_movie(movie_title, top_n=5):
    # 查找输入电影
    movie_row = movies[movies['title'].str.contains(movie_title, case=False)]
    if movie_row.empty:
        return []
    # 获取电影类型（取类型值为1的列）
    genres = movie_row.iloc[0][genre_names]
    liked_genres = genres[genres == 1].index.tolist()
    if not liked_genres:
        # 如果没有匹配类型，推荐最受欢迎的类型（这里简单取Action）
        liked_genres = ['Action']
    # 筛选出包含任一喜欢类型的电影
    mask = movies[liked_genres].any(axis=1)
    candidates = movies[mask]
    # 排除输入电影本身
    candidates = candidates[candidates['id'] != movie_row.iloc[0]['id']]
    return candidates['title'].head(top_n).tolist()

@app.route('/', methods=['GET', 'POST'])
def index():
    recommendations = []
    if request.method == 'POST':
        movie_name = request.form['movie']
        recommendations = recommend_movie(movie_name)
    return render_template('index.html', recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)