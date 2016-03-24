import hashlib, itertools

db = {}

def register(username, password):
    db[username] = get_md5(password + username + 'the-salt')

def get_md5(s):
    md5 = hashlib.md5()
    md5.update(s.encode('utf-8'))
    return md5.hexdigest()

def login(username, password):
    hashstr = get_md5(password + username + 'the-salt')
    if db[username] == hashstr:
        print('Welcome %s' % username)
    else:
        print('Sorry %s, your user name or password is incorrect.' % username)

#test

register('Ian', '12345')
register('kaka', '12345')

print(db)

login('Ian', '12345')
login('kaka', '12345')

ns = itertools.repeat((1,2),2)
for n in ns:
    print(n)