from flask import Flask, render_template

app = Flask(__name__)

# # 여기
# import requests
# from bs4 import BeautifulSoup
#
# from pymongo import MongoClient
#
# client = MongoClient('localhost', 27017)
# db = client.dbsparta
#
#
# @app.route('/free', methods=['GET'])
# def listing():
#     free = list(db.free.find({}, {'_id': False}))
# return jsonify({'all_free': free})
#
#
# ## API 역할을 하는 부분
# @app.route('/free', methods=['POST'])
# def saving():
#     free_img_receive = request.form['free_img_give']
#     free_name_receive = request.form['free_name_give']
#
#     # 크롤링 한 데이터(지금은 메모장 넣어둠)
#
#     url_receive = request.form['url_give']
#     comment_receive = request.form['comment_give']
#
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
#     data = requests.get(url_receive, headers=headers)
#
#     soup = BeautifulSoup(data.text, 'html.parser')
#
#     title = soup.select_one('meta[property="og:title"]')['content']
#     image = soup.select_one('meta[property="og:image"]')['content']
#     desc = soup.select_one('meta[property="og:description"]')['content']
#
#     # 인서트
#
#     doc = {
#         'title': title,
#         'image': image,
#         'desc': desc,
#         'url': url_receive,
#         'comment': comment_receive
#     }
#
#     db.free.insert_one(doc)
#
#
# return jsonify({'msg': 'POST 연결되었습니다!'})
#
#
# # 여기

# Home
@app.route('/')
def home():
    return render_template('index.html')


# TOP50 카테고리
@app.route('/top50')
def top():
    return render_template('top50.html')


# 종료임박 카테고리
@app.route('/closing')
def closing():
    return render_template('closing_soon.html')


# 무료전시 카테고리
@app.route('/free')
def free():
    return render_template('free.html')


# 온라인전시 카테고리
@app.route('/online')
def online():
    return render_template('online.html')


# About Us 카테고리
@app.route('/about_us')
def aboutUs():
    return render_template('about_us.html')


if __name__ == '__main__':
    app.run(port=5000, debug=True)
