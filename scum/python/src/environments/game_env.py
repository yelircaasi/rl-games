"""
Purpose : Environment for card game scum, to be used for reinforcement learning.
Author  : Isaac Riley
Date    : August 2020
"""

from itertools import product
from numpy import array
from numpy.random import permutation


class Player(object):
	"""
	Creates a player that will be used in the game environment.
	"""
	def __init__(self, rank):
		"""
		All that is needed at the start of the game is a rank (i.e. position at the table)
		  and an empty list of cards.
		"""
		self.rank = rank
		self.cards = {i:0 for i in range()}
		self.hand_size = 0

	def eval_hand(self):
		self.cards = sorted(self.cards)

	def play(self, showing, action_vector):
		""" => rewrite to use without lowest; play lowest when higher (rename!) ~0
		Takes an action vector [lowest, higher, pass, break] and uses it to play cards.
		"""
		m = len(showing)
		playables = sorted([(x, self.cards.count(x)) for x in list(set(self.cards)) 
		             if x>showing[0] and self.cards.count(x)>=len(showing)], 
		             key = lambda a:a[0])
		p_unique = [p[0] for p in playables]
		lowest, higher, pass_, break_ = action_vector
		if (pass_ > lowest):
			cards = []
		elif (lowest > pass_):
			num = min(p_unique)
		elif (pass_ > lowest):
			num = p_unique[int(len(p_unique)*higher)]
		to_play = (num, m)





	#def base_policy(self):
	#	"""
	#	Simply plays the lowest
	#	"""

	




class ScumEnvironment(object):
	"""
	Creates environment for the card game scum.
	Allows for different rule variations.
	"""
	def __init__(self, nplayers=6, once_per_round=True, nswappers=2, ndecks=1, 
		         joker_wild=True, joker_exempt=True, royal_discretion=True):
		"""
		nplayers         : Number of players
		once_per_round   : Whether the round is over after each player has had an opportunity 
		                   to play once.
		nswappers        : How many of the lowest players are required to give their highest
		                   cards to the corresponding ith-highest player and receive the same
		                   amount of cards (n-i+1) from the same player. 
		ndecks           : How many decks are used, typically only 1 for up to ~6 players.
		joker_wild       : If true, a single joker can defeat doubles, triples, etc.
		joker_exempt     : If true (as is typical), jokers do not count toward the n-highest
		                   cards a lower player is required to give up.
		royal_discretion : If true, players receiving high cards may give up any (n-i+1) cards 
		                   they like, as opposed to the (n-i+1) absolute lowest.
		"""
		self.once_per_round = once_per_round
		self.nplayers = nplayers
		self.nswappers = nswappers
		self.ndecks = ndecks
		self.high_twos = high_twos
		self.joker_ = joker_wild
		self.joker_exempt = joker_exempt
		self.royal_discretion = royal_discretion
		self.players = {i:Player(i) for i in range(nplayers)}
		start = 2+(self.high2)
		end   = 16+(self.high2)
		temp = list(
			        array(
			        	  product(
			        	  	      range(start, end), range(4), range(self.ndecks)
			        	  	      )
			        	  )
			        )
		self.cards = array(temp + 
			               list(
			               	    product([end], range(2), range(self.ndecks))
			               	    )
			               )
		self.pile = []
		self.showing = None


	def play_hand(self):
		"""
		Deals cards and plays a series of rounds until all cards are gone.
		"""
		self.deal_cards()
		while len(self.pile < self.cards):
			self.play_round()



 
	def play_round(self):
		"""
		Plays a single round.
		"""
		for id, player in self.players.items():
			pass



	def deal_cards(self):
		"""
		
		"""


	

class Agent(object):
	"""

	"""
	def __init__(self):
		pass

	def policy(self, hand, showing, cards_left, ):
		""" scratch: policy features: num 2/3/4/etc.-tuples, mean card, median card, skewness, 
		             proportion of cards already played, number of cards in other players' hands,
		             mean, min, max, median number of cards in other players' hands
		             summary stats of cards already played
		             n players

		             possible actions: given showing card(s), all higher cards of the same multiplicity 
		                               
		             actions: default: lowest cards of same multiplicity
		                      break tuple: play m cards of an n-tuple, where m<n
							  higher (in [4,16] to indicate how much higher): 
		                      pass: play nothing at all
							  
		Receives as input: 
		Returns policy vector of length 4:
		  -lowest : play the lowest possible cards (given previously-played card(s) and multiplicity)
		  -higher : of the n playable cards, play card i such that (i-1)/n < higher <= i/n
		  -pass   : play nothing at all
		  -break  : break up tuples if necessary
		"""


