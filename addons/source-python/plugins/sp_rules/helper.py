#========================
# Imports
#========================
from engines.server import queue_command_string
from players.helpers import index_from_userid, userid_from_index

#========================
# Server Command
#========================

def server_command(__cmd__):
	queue_command_string(__cmd__)

#========================
# Userid
#========================

def indexFromUserid(userid):
	return index_from_userid(userid)

def useridFromIndex(index):
	return userid_from_index(index)
