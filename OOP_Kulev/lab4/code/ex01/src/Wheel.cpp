#include "Wheel.hpp"

Wheel::Wheel(float const r) : _r(r) {
	if (_r <= 0)
		throw InvalidR();
}

Wheel::Wheel(Wheel const & t) : _r(t.getR()) {}

float Wheel::getR(void) const {return _r;}

std::ostream & operator << (std::ostream & o, Wheel const & t) {
	o << "Wheel: {R = " << t.getR() << "}";
	return o;
}

char const * Wheel::InvalidR::what() const throw() {
	return "Invalid Radius";
}