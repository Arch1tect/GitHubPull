from bottle import get, post, put, delete, route, request, run, template
import json
import git



# git_dir = "/Users/swotong/Project/Qtime" #my local
git_dir = "/home/ec2-user/project/qtime" #AWS Singapore



# dynamic routing
@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

@post('/github')
def githubUpdated():

	g = git.cmd.Git(git_dir)
	g.pull()


	return "succeed!"





run(host='0.0.0.0', port=8080)