#include "VolleyBall.hpp"

int const VolleyBall::defaultNbPlayers = 12;
int const VolleyBall::minNbPlayers = 2;

VolleyBall::VolleyBall(void) : SportGame(defaultNbPlayers, true) {}

VolleyBall::VolleyBall(int nbOfPlayers) : SportGame(nbOfPlayers, true) {
	if (_playerCount < minNbPlayers)
		throw InvalidNbOfPlayers();
}

void VolleyBall::play(void) const {
	std::cout << "We're playing Volley Ball!" << std::endl;
}

std::ostream & operator << (std::ostream & o, VolleyBall const & t) {
	o << "Volley Ball: {players: " << t._playerCount << "; "
		<< "is in open field: " << t.isInOpenField() << "}";
	return o;
}