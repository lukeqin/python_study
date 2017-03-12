#-*- coding: UTF-8 -*-
'''
Created on 2017年3月11日
@author: luke
'''

from gittle import Gittle

repo_path = r'E:\date\dev\mygit\tmp'
repo_url = 'git@192.168.9.9:/data/git/ratel.git'
#repo = Gittle.clone(repo_url, repo_path)

'''
key_file = open(r'C:\Users\luke\.ssh\id_rsa')
repo.auth(pkey=key_file)
'''

#git pull
repo = Gittle(repo_path, origin_uri=repo_url)
repo.pull()

#edited file 'test'
f = open(r'E:\date\dev\mygit\tmp\test', 'a+')
f.write('Test python git lib.\n')
f.close()

#git commit
repo.stage(r'E:\date\dev\mygit\tmp\test')
repo.commit(name="Luke", email="none", message="This is a commit")

#git push
repo.push()