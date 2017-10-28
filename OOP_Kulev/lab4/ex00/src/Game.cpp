#include "Game.hpp"

/*
** Constructors && destructors
*/

Game::Game(void) {
	_playerCount = 0;
}

Game::Game(int const playersCount) {
	_playerCount = playersCount;
}

/*
** Getters && Setters
*/

int		Game::getPlayerCount(void) const {return _playerCount;}

void	Game::setPlayerCount(int const newPlayerCount) {
	_playerCount = newPlayerCount;
}

/*
** Other functions
*/

void	Game::play(void) const {
	std::cout << "We're playing a Game!" << std::endl;
}

/*
** Operators
*/

Game & Game::operator = (Game const & target) {
	setPlayerCount(target.getPlayerCount());
	return *this;
}

std::ostream & operator << (std::ostream & o, Game const & target) {
	o << "Game: {playersCount: " << target.getPlayerCount() << "}";
	return o;
}