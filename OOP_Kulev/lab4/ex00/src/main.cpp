#include "Game.hpp"
#include "SportGame.hpp"
#include "VolleyBall.hpp"

int		main(void) {
	Game gm(10);

	std::cout << gm << std::endl;
	gm.play();

	SportGame sGm(10, false);
	std::cout << sGm << std::endl;
	sGm.play();

	VolleyBall voll;
	std::cout << voll << std::endl;
	voll.play();
	return 0;
}