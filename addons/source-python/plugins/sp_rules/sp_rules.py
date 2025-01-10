from players.entity import Player
from events import Event
from menus import SimpleMenu, SimpleOption, Text
from messages import SayText2

get_rules = ['No Spawn Killing', 'No Flaming', 'No Chat/Mic Spam', 'No Bomb Griefing', 'No Other Servers Adverting', 'No Bug Abuse', 'No Suicide'] # The rules text for menu

rules_accepted_message = SayText2('\x04Thank you for accepting the rules and have fun playing on the server!')

@Event('player_activate')
def player_activate(args):
	player = Player.from_userid(args['userid'])
	player.delay(2.0, rules_menu.send, (player.index,))

def rules_menu_callback(menu, index, option):
	choice = option.value
	if choice == 'no':
		Player(index).kick('You have to accept the rules!')
	elif choice == 'yes':
		rules_accepted_message.send(index)

def build_rules_menu(menu, index):
	menu.clear()
	menu.append(Text('Server rules'))
	menu.append(Text(' '))
	menu.append(Text('Do you accept the rules?'))
	menu.append(Text(' '))
	for rule in get_rules:
		menu.append(Text(rule))
	menu.append(SimpleOption(1, 'No', 'no'))
	menu.append(SimpleOption(2, 'Yes', 'yes'))
	menu.append(Text(' '))
	menu.append(SimpleOption(0, 'No', None))
	@menu.register_close_callback
	def on_close_rules_menu(menu, index):
		Player(index).kick('You have to accept the rules!')

rules_menu = SimpleMenu()
rules_menu.build_callback = build_rules_menu
rules_menu.select_callback = rules_menu_callback
