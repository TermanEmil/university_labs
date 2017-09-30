from random import *
from operator import add

def		individual(count, minNb, maxNb):
	return [randint(minNb, maxNb) for _ in xrange(count)]

def		population(individCount, individLen, minNb, maxNb):
	return [individual(individLen, minNb, maxNb) for _ in xrange(individCount)]

def		fitness(individual, target):
	return abs(sum(individual) - target)

def		grade(pop, target):
	totalSum = sum(fitness(individ, target) for individ in pop)
	return float(totalSum) / len(pop)

def		mutate(pop, mutateChance):
	for individ in pop:
		if mutateChance > random():
			posToMutate = randint(0, len(individ) - 1)
			individ[posToMutate] = randint(0, 100)

	return pop

def		evolve(pop, target, retain=0.2, randomSelect=0.05, mutateChance=0.01):
	graded = [(fitness(individ, target), individ) for individ in pop]
	sortedPop = [comb[1] for comb in sorted(graded)]

	retainLen = int(max(round(len(sortedPop) * retain, 0), 1))
	parents = sortedPop[:retainLen]

	# Add some new individuals - to create some diversity
	for newIndivid in sortedPop[retainLen:]:
		if randomSelect > random():
			parents.append(newIndivid)

	parents = mutate(parents, mutateChance)

	# Make some love
	parentsLen = len(parents)
	desiredLen = len(pop) - parentsLen
	children = []

	while len(children) < desiredLen:
		maleI = randint(0, parentsLen - 1)
		femaleI = randint(0, parentsLen - 1)

		if maleI == femaleI:
			continue

		male = parents[maleI]
		female = parents[femaleI]

		half = len(male) / 2
		child = male[:half] + female[half:]
		children.append(child)

	return parents + children

target = 371
popCount = 100
indiviLen = 5
individMin, individMax = 0, 100

pop = population(popCount, indiviLen, individMin, individMax)
fitness_history = [grade(pop, target)]

for _ in xrange(100):
	pop = evolve(pop, target, 0.2, 0.05, 0.01)
	fitness_history.append(grade(pop, target))

# for individ in pop:
# 	print individ
print fitness_history
