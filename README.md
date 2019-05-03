# mongodb
an app in Python to connect with MongoDB

Install MongoDB on macOS Sierra

This procedure explains how to install MongoDB using Homebrew on macOS Sierra 10.13.6

Install Homebrew: open Terminal and enter :
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

then install python3:
brew install python3

Enter the following command : $ brew info mongodb
Expected output: mongodb: stable 4.0.3 (bottled)

To install MongoDB enter : $ brew install mongodb

Additional configuration
Homebrew
To load and start the MongoDB background service, open Terminal and execute the following commands :

Load and start the MongoDB service : $ brew services start mongodb.
Expected output : Successfully started mongodb (label: homebrew.mxcl.mongodb)

Check of the MongoDB service has been loaded : $ brew services list 1

Verify the installed MongoDB instance : $ mongod --version.
Expected output : db version v4.0.3

to verify if the db is running:
ps -ef | grep mongod | grep -v grep | wc -l | tr -d ' ' (returns # of processes. if more than 0 , then mongo db is running)

Install PyCharm
