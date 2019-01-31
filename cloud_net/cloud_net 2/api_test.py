import requests, json

base = 'http://localhost:8000/frinet/'
header = {'Content-Type': 'application/json'}
# 'Authorization': 'Token xxxxxx'

def test_register(uname, password, netid):
    payload = {'username': uname, 'password': password, 'netid': netid}
    r = requests.post(base + 'register', data=json.dumps(payload), headers=header)
    return r.status_code

def test_login(uname, passwd):
    payload = {'username': uname, 'password': passwd}
    r = requests.post(base + 'login', data=json.dumps(payload), headers=header)
    return r.json()

def test_logout(auth):
    header['Authorization'] = 'Token ' + auth
    r = requests.post(base + 'logout', headers = header)
    return r.status_code

def test_get_friends(auth):
    header['Authorization'] = 'Token ' + auth
    r = requests.get(base + 'friend', headers = header)
    return r.json()

def test_get_posts(auth):
    header['Authorization'] = 'Token ' + auth
    r = requests.get(base + 'post', headers = header)
    return r.json()

def test_make_post(auth, post_ctnt):
    payload = {'content': post_ctnt}
    header['Authorization'] = 'Token ' + auth
    r = requests.post(base + 'make_post', data=json.dumps(payload), headers=header)
    return r.json()

def test_add_following(auth, f_uname):
    payload = {'friend_name': f_uname}
    header['Authorization'] = 'Token ' + auth
    r = requests.post(base + 'follow', data=json.dumps(payload), headers=header)
    return r.json()


if __name__ == "__main__":
    print test_register('elaine', '1234', '1234')
    print test_register('chuchao', '1234', '1234')
    print test_register('oscar', '1234', '1234')
    print test_register('matt', '1234', '1234')



