# 电影推荐系统 (Movie-Recommendation-System) 🎬

### 🚀 项目简介
本项目基于 MovieLens 100k 数据集，实现了一个基于内容的过滤 (Content-Based Filtering) 推荐引擎。系统通过计算电影特征向量的余弦相似度，为用户提供精准的个性化推荐。

### 🛠️ 技术栈
- **核心语言**: Python 3.x
- **数据处理**: Pandas, NumPy
- **相似度算法**: Cosine Similarity (余弦相似度)
- **Web 框架**: Flask (用于展示推荐结果)

### 📂 目录结构说明
- `app.py`: 项目核心逻辑与 Flask 后端。
- `ml-100k/`: 原始数据集文件夹。
- `templates/`: HTML 页面模板。
- `u.item`: 电影信息映射表（核心数据文件）。
- `requirements.txt`: 项目依赖库清单。

### ⚡ 快速开始
1. **克隆项目**: `git clone git@github.com:xiaoyh23/Movie-Recommendation-System.git`
2. **安装依赖**: `pip install -r requirements.txt`
3. **运行程序**: `python app.py`