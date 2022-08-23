from flask import Flask
from flask import request
from flask import make_response
import uuid
app = Flask(__name__)

@app.route('/')
def hello_world():
    cookies = request.cookies
    if 'sessionId' in cookies:
        response = make_response(
            '기존 연결입니다 : sessionId={0}'.format(cookies['sessionId'])
        )
    else:
        new_session_id = str(uuid.uuid4())
        response = make_response(
            '새 연결입니다 : sessionId={0}'.format(cookies['sessionId'])
        )
        response.set_cookie('sessionId', new_session_id)
    return response
app.run()