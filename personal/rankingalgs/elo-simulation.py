'''
elo-simulation.py
author: Justin Chen
date: 12.8.15

Objective:
Trying to figure out if the ELO algorithm is order invariant.
R' = R + K * (S - E)

Assumptions:
Kong Gainer = hardest
Down Monkey = medium
Kong Front  = easy
Kong Gainer beats both Down Monkey and Kong Front in difficulty, so I expect that Kong Gainer will have a higher rank than the other two moves.
Down Monkey should have the second highest score and Kong Front should have the lowest score.

Results:
{'kong front': 1468.7023986633528, 'kong gainer': 1531.263693206478, 'down monkey': 1500.0339081301693}
{'kong front': 1468.766810297684, 'kong gainer': 1530.4968829087939, 'down monkey': 1500.736306793522}
{'kong front': 1468.0339081301693, 'kong gainer': 1531.263693206478, 'down monkey': 1500.7023986633528}
{'kong front': 1468.736306793522, 'kong gainer': 1531.9660918698307, 'down monkey': 1499.2976013366472}
{'kong front': 1469.5031170912061, 'kong gainer': 1531.233189702316, 'down monkey': 1499.263693206478}
{'kong front': 1468.736306793522, 'kong gainer': 1531.2976013366472, 'down monkey': 1499.9660918698307}

Conclusion:
The ranks were computed as expected, however, the ELO ranking algorithm is not order-invariant.
This is a problem if you need scores to construct a ranking system.
Sigh. I need another algorithm. Back to the drawing board. :/
'''

import csv
import itertools

def expect(player1, player2):
	return 1.0/(1.0+ pow(10.0, ((player2 - player1)/400.0)))

def simulateMatches(matches, scoreBoard):
	
	K = 32

	for m in matches:
		print('\n'+m[0]+' v. '+m[1])
		print(m[0])
		S1 = input("win/lose (1/0)?")
		print(m[1])
		S2 = input("win/lose (1/0)?")

		rank1 = scoreBoard[m[0]]
		rank2 = scoreBoard[m[1]]
		expected1 = expect(rank1, rank2)
		expected2 = expect(rank2, rank1)
		rank1 += K * (S1 - expected1)
		rank2 += K * (S2 - expected2)

		scoreBoard[m[0]] = rank1
		scoreBoard[m[1]] = rank2

	return scoreBoard

def permute(matches):
	return list(itertools.permutations(matches))

def genMatches(moves):
	return list(itertools.combinations(moves,2))

def initializeScoreboard(moves):
	startingScore = float(1500)
	return dict([(m, startingScore) for m in moves])

if __name__ == "__main__":
	moves        = ['kong gainer', 'down monkey', 'kong front']
	matches 	 = genMatches(moves)
	permutations = permute(matches) 
	allResults   = []

	for p in permutations:
		scoreBoard   = initializeScoreboard(moves)
		results      = simulateMatches(p, scoreBoard)
		allResults.append(results)

	for res in allResults:
		print(res)







