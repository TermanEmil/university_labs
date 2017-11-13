#include "SportGame.hpp"

SportGame::SportGame(void) : Game(), _inOpenField(false) {
}

SportGame::SportGame(int const playersCount, bool const inOpenField) :
	Game(playersCount), _inOpenField(inOpenField)
{}

bool	SportGame::isInOpenField(void) const {return _inOpenField;}

void	SportGame::play(void) const {
	std::cout << "We're playing a sportive game!" << std::endl;
}

std::ostream & operator << (std::ostream & o, SportGame const & target) {
	o << "Sport Game: {players: " << target._playerCount << ";";
	o << " is in open field: " << target._inOpenField << "}";
	return o;
}