#========================
# Imports
#========================
from engines.server import queue_command_string
from players.helpers import index_from_userid, userid_from_index
from events import Event
from listeners.tick import Delay
from menus import SimpleMenu, SimpleOption, Text

#========================
# Config
#========================

get_rules = ['No Spawn Killing', 'No Flaming', 'No Chat/Mic Spam', 'No Bomb Griefing', 'No Other Servers Adverting', 'No Bug Abuse', 'No Suicide'] # Rules text

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

#========================
# Menu
#========================

def is_queued(_menu, _index):
	q = _menu._get_queue_holder()
	for i in q:
		if i == _index:
			for x in q[i]:
				return True
	return False

#========================
# Menu Callback
#========================

def rule_menu_callback(_menu, _index, _option):
	choice = _option.value
	if choice:
		userid = useridFromIndex(_index)        
		if choice == 'No':
			server_command('kickid %s You have to accept the rules!' % (userid))    
        
#========================
# Event
#========================

@Event('player_activate')
def player_activate(args):
	userid = args.get_int('userid')   
	Delay(2.0, rules, (userid,))

#========================
# Rules Menu
#========================

def rules(userid):
	menu = SimpleMenu()
	if is_queued(menu, indexFromUserid(userid)):
		return  
	menu.append(Text('The Rules'))
	menu.append(Text(' '))
	for i in get_rules:
		menu.append(Text('%s' % (i)))
	menu.append(Text(' '))
	menu.append(Text('Do you accept the rules?'))
	menu.append(Text(' '))    
	menu.append(SimpleOption(8, 'No', 'No'))    
	menu.append(SimpleOption(9, 'Yes', None))   
	menu.select_callback = rule_menu_callback
	menu.send(indexFromUserid(userid))          
    
 	 	    