#ifndef WHEEL_HPP
# define WHEEL_HPP

# include <iostream>
# include <string>
# include <stdexcept>

class Wheel {
public:
	class InvalidR: public std::exception {
	public:
		virtual char const * what() const throw();
	};

	Wheel(float r);
	Wheel(Wheel const & t);

	float getR(void) const;

	friend std::ostream & operator << (std::ostream & o, Wheel const & t);

private:
	float const _r;
};

#endif