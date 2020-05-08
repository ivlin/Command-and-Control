# cse363c-and-c

Ivan Lin, Nicholas Pradlik

## Description

Covert command-and-control software meant to allow infected machines to communicate with an external server.

### Client

send - calls testnetwork to check network conditions and makes a decision based on the output

send_git_commit -> uploads a message in the form of multiple commits
send_git_file -> uploads a message as a file to the git repo
send_https_file -> sends a file as a https post using (DoH, HTTPS)

recv - chooses one of the get methods - if None is passed as argument, pull the commit log, else get the url passed as an argument

get_https_file -> downloads the file at a url (DoH, HTTPS)
get_git_commits -> Downloads the commit log and saves it as commitlog in the working directory

## Features

Sat 02 May 2020 02:27:34 PM EDT
