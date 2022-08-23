import json
from dataclasses import dataclass
import datetime
from flask import request, Flask, Blueprint

bp = Blueprint('v1', __name__, url_prefix='/v1')

posts = {}
post_number = 1

@dataclass
class BlogPost:
    title: str
    contents: str
    date: str

@bp.route('/posts', methods=['POST'])
def write_posts():
    request_json = request.get_json()
    title = request_json.get('title', '')
    contents = request_json.get('contents','')
    
    if len(title)==0 or len(contents)==0:
        return 'Bad request', 400
    
    global post_number
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print('titme={0}, contents={1}, date={2}, post_number={3}'.format(
        title, contents, now, post_number
    ))
    
    posts[post_number] = BlogPost(title=title, contents=contents, date=now)
    post_number = post_number + 1
    
    return 'OK', 200

app = Flask(__name__)
app.register_blueprint(bp)
app.url_map.strict_slashes = False
app.run()