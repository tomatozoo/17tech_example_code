@dp.route('/posts/<number>', methods=['DELETE'])
def delete_post(number):
    post = posts.get(int(number), None)
    if not post:
        return 'Bad Request', 400
    del posts[int(number)]
    return 'OK', 200