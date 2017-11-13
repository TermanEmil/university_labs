#include "Lorry.hpp"

Lorry::Lorry(
	float const mass,
	size_t const wheelN,
	float const wheelR,
	std::string const & mark
) : Car(wheelN, wheelR, mark), _mass(mass) {}

std::ostream & operator << (std::ostream & o, Lorry const & t) {
	o << "Lorry: {Mark: " << t._mark
		<< "; Mass: " << t._mass
		<< "t; Wheels[" << t.wheelCount() << "]: {" << std::endl << "\t";

	std::vector<Wheel>::const_iterator wheel = t._wheels.begin();
	for (; wheel < t._wheels.end(); wheel++) {
		o << *wheel;
		if (wheel != t._wheels.end())
			o << "; ";
	}
	o << std::endl << "}";
	return o;
}