from fabric.api import env,run
from fabric.operations import sudo
GIT_REPO = "https://github.com/viciong/blog.git"
env.user = 'wuheng'
env.password = 'eternal...'
env.hosts = ['eternalwu.com']
env.port = '22'

def deploy():
    source_folder = '/home/wuheng/sites/eternalwu.com/blog'
    run('cd %s && git pull' % source_folder)
    run("""
        cd {} &&
        ../env/bin/pip install -r requirements.txt &&
        ../env/bin/python3 manage.py collectstatic --noinput &&
        ../env/bin/python3 manage.py migrate
        """.format(source_folder))
    #sudo('restart gunicorn-eternalwu.com')
    sudo('service nginx reload')
    sudo('cd /home/wuheng/sites/eternalwu.com && source env/bin/activate && cd blog && gunicorn --bind unix:/tmp/eternalwu.com.socket blogproject.wsgi:application')