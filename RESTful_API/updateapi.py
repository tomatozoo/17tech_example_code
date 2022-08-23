@bp.route('/posts/<number>', methods=['PUT'])
def update_post(number):
    number = int(number)
    post = posts.get(number, None)
    if not post:
        return 'Bad Request', 400
    
    request_json = request.get_json()
    title = request_json.get('title', '')
    contents = request_json.get('contents', '')
    
    if len(title) == 0 or len(contents) == 0:
        return 'Bad request', 400
    
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print('title={0}, contents={1}, date={2}, number={3}'.format(
        title, contents, now, number
    ))
    
    posts[number] = BlogPost(title=title, contents=contents, date=now)
    return 'OK', 200