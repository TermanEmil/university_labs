#ifndef LORRY_HPP
# define LORRY_HPP

# include "Car.hpp"

class Lorry: public Car {
public:
	Lorry(float mass, size_t wheelN, float wheelR, std::string const & mark);
	friend std::ostream & operator << (std::ostream & o, Lorry const & t);

private:
	float const _mass;
};

#endif