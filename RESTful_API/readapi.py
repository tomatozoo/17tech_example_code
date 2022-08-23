@bp.route('/posts/<number>', methods=['GET'])
def get_post(number):
    post = posts.get(int(number), None)
    if not post:
        return 'Bad Request', 400
    posts_json = [{'title':post.title, 
                   'contents':post.contents, 
                   'date':post.date, 
                   'number':number}]
    response_json = {'post':posts_json}
    
    try:
        return json.dumps(response_json, ensure_ascii=False)
    except json.JSONDecodeError:
        return 'Internal Server Error', 500
    
@bp.route('/posts', methods=['GET'])
def get_posts():
    posts_size = request.args.get('size', '-1')
    posts_size = int(posts_size)
    
    posts_json = []
    posts_acquired = 0
    
    for number in posts:
        post = posts[number]
        posts_json.append({'title':post.title, 
                           'contents':post.contents, 
                           'date':post.date, 
                           'number':number})
        posts_acquired = posts_acquired + 1
        if 0 <= posts_size <= posts_acquired:
            break
    response_json = {'posts':posts_json}
    try:
        return json.dumps(response_json, ensure_ascii=False)
    except json.JSONDecodeError:
        return 'Internal Server Error', 500
    
