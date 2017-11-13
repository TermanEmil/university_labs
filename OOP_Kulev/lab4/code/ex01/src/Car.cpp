#include "Car.hpp"

Car::Car(size_t const wheelN, float const wheelR, std::string const & mark) :
	_mark(mark)
{
	_wheels.reserve(wheelN);

	for (size_t i = 0; i < wheelN; i++)
		_wheels.push_back(Wheel(wheelR));
}

size_t Car::wheelCount(void) const {
	return _wheels.size();
}

float Car::wheelsR(void) const {
	if (wheelCount() == 0)
		return 0;
	else
		return _wheels[0].getR();
}

std::ostream & operator << (std::ostream & o, Car const & t) {
	o << "Car: {Mark: " << t._mark << "; Wheels["
		<< t.wheelCount() << "]: {" << std::endl << "\t";

	std::vector<Wheel>::const_iterator wheel = t._wheels.begin();
	for (; wheel < t._wheels.end(); wheel++) {
		o << *wheel;
		if (wheel != t._wheels.end())
			o << "; ";
	}
	o << std::endl << "}";
	return o;
}