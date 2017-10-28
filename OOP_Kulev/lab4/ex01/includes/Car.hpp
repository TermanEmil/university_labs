#ifndef CAR_HPP
# define CAR_HPP

# include "Wheel.hpp"
# include <vector>

class Car {
public:
	Car(size_t wheelCount, float wheelR, std::string const & mark);

	size_t wheelCount(void) const;
	float wheelsR(void) const;

	friend std::ostream & operator << (std::ostream & o, Car const & t);

protected:
	std::vector<Wheel>	_wheels;
	std::string const	_mark;
};

#endif