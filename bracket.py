import math
import random

def generate_bracket_rec(players):
	games_map = {}
	next_players = []

	assert len(players) > 0 

	if len(players) == 1:
		return games_map

	for i in range(int(len(players) / 2)):
		player1_id = i
		player2_id = len(players) - 1 - i

		if players[player2_id] is None:
			next_players.append(players[player1_id])		
		else:
			game_id = str(int(math.log(len(players), 2))) + "g" + str(i + 1)
			g = Game((players[player1_id], players[player2_id]), game_id)
			games_map[g.id] = g		
			next_players.append((g, "winner"))
	d = {}
	d.update(games_map)
	d.update(generate_bracket_rec(next_players).items())
	return d

# Players in each game will either be string literals
# or tuples that contain a Game and "loser" or "winner"
class Game:
	def __init__(self, players, game_id=None):
		self.players = players
		self.done = False
		self.id = random.getrandbits(24) if game_id is None else game_id

	def __str__(self):
		output = self.id + ": "
		output = output + (self.players[0][0].get(self.players[0][1]) if type(self.players[0]) is tuple else self.players[0]) + " vs "
		output = output + (self.players[1][0].get(self.players[1][1]) if type(self.players[1]) is tuple else self.players[1])
		return output

	def __repr__(self):
		output = str(self)
		output = output + "\nDone: " + str(self.done) + (" | Winner: " + self.winner + " Loser: " + self.loser if self.done else "")
		return output

	def get_raw_players(self):
		return tuple(player[0].get(player[1]) if type(player) is tuple else player for player in self.players)

	def is_ready(self):
		for player in self.players:
			if type(player) is tuple and player[0].done == False:
				return False
		return True

	def play_game(self, winning_player):
		# TODO: Deal with fact that this is just the is_ready method again
		for player in self.players:
			if type(player) is tuple and player[0].done == False:
				print("ERROR 1: Attempting to start " + self.id + " before " + player[0].id + " is complete")
				return


		players_raw = tuple(player[0].get(player[1]) if type(player) is tuple else player for player in self.players)

		if winning_player not in players_raw:
			print("ERROR 2: " + winning_player + " not in " + self.id)
			return

		self.winner = winning_player
		self.loser = players_raw[0] if players_raw[1] == winning_player else players_raw[1]
		self.done = True

	def get(self, item):
		if not self.done:
			return str(item) + " of " + str(self.id)
		else:
			if item == "winner":
				return self.winner
			elif item == "loser":
				return self.loser
			else:
				return "INVALID"

# TODO: Make a more a general get function that checks if the type is a Tuple or a game and then evaluates


class Tournament:
	def __init__(self, players):
		self.players = players
		self.player_count = len(players)
		self.games = {}
	def __str__(self):
		output = ""
		for s in players:
			output = output + ((s + " ") if s is not None else "" )
		output = output + "\nlog(Size): " + str(self.n_size) + " | underflow: " + str(self.underflow)
		return output

	def __repr__(self):
		return __str__()

	def generate_bracket(self, bracket_class, randomize):
		if bracket_class != "single":
			print("Illegal bracket class")
			quit()

		self.n_size = int(math.ceil(math.log(self.player_count, 2)))
		self.underflow = int(math.pow(2, self.n_size) - self.player_count)

		if randomize:
			random.shuffle(self.players)

		for i in range(self.underflow):
			self.players.append(None)

		self.games = generate_bracket_rec(self.players)

	def play_game(self, game_id, game_winner):
		if game_id not in self.games:
			print("ERROR 3: Illegal Game ID " + game_id)

		if self.games[game_id].done:
			print("ERROR 4: Game aready complete " + game_id)

		self.games[game_id].play_game(game_winner)


players = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
t = Tournament(players)
t.generate_bracket("single", True)

print([str(g) for g in t.games.values()])


print("\n\n\n\n")

while(True):
	print([str(g) for g in t.games.values() if g.is_ready() and not g.done])
	game = input("Enter game ID: ") 
	winner = input("Enter game winner: ")
	t.play_game(game, winner)