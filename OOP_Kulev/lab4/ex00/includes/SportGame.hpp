#ifndef SPORTGAME_HPP
# define SPORTGAME_HPP

# include "Game.hpp"

class SportGame : public Game {
public:
	SportGame(void);
	SportGame(int playersCount, bool inOpenField);

	bool	isInOpenField(void) const;
	void	play(void) const;

	friend std::ostream & operator << (std::ostream & o, SportGame const & g);
	
private:
	bool const	_inOpenField;
};

#endif