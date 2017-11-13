#ifndef GAME_HPP
# define GAME_HPP

# include <iostream>
# include <string>

class Game {
public:
	Game(void);
	Game(int playersCount);

	int		getPlayerCount(void) const;
	void	setPlayerCount(int newPlayerCount);

	void	play(void) const;

	Game & operator = (Game const & target);
	friend std::ostream & operator << (std::ostream & o, Game const & target);

protected:
	int		_playerCount;
};

#endif