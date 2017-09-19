#ifndef COMPLEXLIB_HPP
# define COMPLEXLIB_HPP

# include <iostream>

struct		ComplexNb
{
	double	re;
	double	im;

	// ComplexNb & operator = (ComplexNb const & target);

	// //Arithmetic operators
	// ComplexNb operator + (ComplexNb const & target);
	// ComplexNb operator - (ComplexNb const & target);
	// ComplexNb operator * (ComplexNb const & target);
	// ComplexNb operator / (ComplexNb const & target);

	// //Comparison operations
	// bool operator > (ComplexNb const & target) const;
	// bool operator < (ComplexNb const & target) const;
};

// std::ostream & operator << (std::ostream & o, ComplexNb const & target);

void		setComplex(ComplexNb & thisC, ComplexNb const & target);

ComplexNb	addComplex(ComplexNb & thisC, ComplexNb const & target);
ComplexNb	decComplex(ComplexNb & thisC, ComplexNb const & target);
ComplexNb	multComplex(ComplexNb & thisC, ComplexNb const & target);
ComplexNb	divComplex(ComplexNb & thisC, ComplexNb const & target);

bool		lessComplex(ComplexNb const & thisC, ComplexNb const & target);
bool		greatComplex(ComplexNb const & thisC, ComplexNb const & target);

std::ostream &printComplex(ComplexNb const & target);

ComplexNb	Complex(double re, double im);
double		abs(ComplexNb const & target);

#endif