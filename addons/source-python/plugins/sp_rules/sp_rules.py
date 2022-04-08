from core import SOURCE_ENGINE
from engines.server import queue_command_string
from players.entity import Player
from players.helpers import index_from_userid, userid_from_index
from events import Event
from menus import SimpleMenu, SimpleOption, Text
from messages import SayText2

get_rules = ['No Spawn Killing', 'No Flaming', 'No Chat/Mic Spam', 'No Bomb Griefing', 'No Other Servers Adverting', 'No Bug Abuse', 'No Suicide'] # The rules text for menu

if SOURCE_ENGINE == 'csgo':
	close_button = 9
else:
	close_button = 0

@Event('player_activate')
def player_activate(args):
	userid = args.get_int('userid')
	Player(index_from_userid(userid)).delay(2.0, rules, (userid,))

def rules(userid):
	menu = SimpleMenu()
	menu.append(Text('The Rules'))
	menu.append(Text(' '))
	for i in get_rules:
		menu.append(Text('%s' % (i)))
	menu.append(Text(' '))
	menu.append(Text('Do you accept the rules?'))
	menu.append(Text(' '))
	menu.append(SimpleOption(8, 'No', 'No'))
	menu.append(SimpleOption(9, 'Yes', 'Yes'))
	menu.append(SimpleOption(close_button, 'Close', 0))
	@menu.register_close_callback
	def on_close_checkpoints_menu(menu, index):
		queue_command_string('kickid %s You have to accept the rules!' % (userid))
	menu.select_callback = rule_menu_callback
	menu.send(index_from_userid(userid))
	

def rule_menu_callback(_menu, _index, _option):
	choice = _option.value
	if choice:
		userid = userid_from_index(_index)        
		if choice == 'No':
			queue_command_string('kickid %s You have to accept the rules!' % (userid))
		elif choice == 'Yes':
			SayText2('\x04Thank you for accepting the rules and have fun!').send(_index)
     	    
