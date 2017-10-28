#ifndef VOLLEYBALL_HPP
# define VOLLEYBALL_HPP

# include "SportGame.hpp"
# include <stdexcept>

class VolleyBall: public SportGame {
public:
	static int const defaultNbPlayers;
	static int const minNbPlayers;

	class InvalidNbOfPlayers: public std::exception {
	public:
		virtual char const * what() const throw() {
			return "Invalid Number of Players.";
		}
	};

	VolleyBall(void);
	VolleyBall(int nbOfPlayers);

	void play(void) const;

	friend std::ostream & operator << (std::ostream & o, VolleyBall const & t);
};

#endif