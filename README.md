# cse363c-and-c

Ivan Lin, Nicholas Pradlik

## Demo

Due to technical difficulties, there are significant issues with playback of the first video past the 3:30 mark. There are audio cutouts from the first video after 3:00 and minor breaks in audio in the second video. However, the video is able to display running the code.

## Description

Covert command-and-control software meant to allow infected machines to communicate with an external server.

## Demo

Due to technical difficulties, there are significant issues with playback of the first video past the 3:30 mark. There are audio cutouts from the first video after 3:00 and minor breaks in audio in the second video. However, the video is able to display running the code.

## Description

Covert command-and-control software meant to allow infected machines to communicate with an external server.

## Features

Transmit data with git commits and uploads.
Transmit data with HTTPS.
Receive data through git commits by pulling the git log.
Receive data with HTTPS.


### Client

send - calls testnetwork to check network conditions and makes a decision based on the output

send_git_commit(msg) -> uploads a message in the form of multiple commits
send_git_file(fname) -> uploads a file with name fname as a file to the git repo
send_https_file(file, dest, resolver) -> sends a file as a https post to a destination using a specified resolver endpoint(DoH, HTTPS)

recv - chooses one of the get methods - if None is passed as argument, pull the commit log, else get the url passed as an argument

get_https_file(url) -> downloads the file at a url (DoH, HTTPS)
get_commit_message() -> Downloads the commit log and saves it as commitlog in the working directory

### Server

On running, if there are no keys in server/keys it will prompt you to make one. These should be named id_rsa. Add these keys to the git server but do no add them to the server's ssh agent.

## Running It
Current settings are configured to run with the developer's git account. In order to test, the following must be modified:
- email in test_server.py to the email associated with the git
- USER - set to git account name
- REPO - set to an existing git repo for communication
