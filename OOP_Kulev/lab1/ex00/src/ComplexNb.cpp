#include "ComplexLib.hpp"
#include <cmath>

ComplexNb	Complex(double const re, double const im)
{
	ComplexNb	result;

	result.re = re;
	result.im = im;
	return result;
}

/*
** Arithmetic operations
*/

void		setComplex(ComplexNb & thisC, ComplexNb const & target)
{
	thisC.re = target.re;
	thisC.im = target.im;
}

ComplexNb	addComplex(ComplexNb & thisC, ComplexNb const & target)
{
	thisC.re += target.re;
	thisC.im += target.im;
	return (thisC);
}

ComplexNb	decComplex(ComplexNb & thisC, ComplexNb const & target)
{
	thisC.re -= target.re;
	thisC.im -= target.im;
	return (thisC);
}

ComplexNb	multComplex(ComplexNb & thisC, ComplexNb const & target)
{
	thisC.re = thisC.re * target.re - thisC.im * target.im;
	thisC.im = thisC.re * target.im + thisC.im * target.re;
	return thisC;
}

ComplexNb	divComplex(ComplexNb & thisC, ComplexNb const & target)
{
	double const	divPart = (target.re * target.re + target.im * target.im);

	thisC.re = (thisC.re * target.re + thisC.im * target.im) / divPart;
	thisC.im = (thisC.im * target.re - thisC.re * target.im) / divPart;
	return thisC;
}

/*
** Comparison Operations
*/

bool		lessComplex(ComplexNb const & thisC, ComplexNb const & target)
{
	return abs(thisC) > abs(target);
}

bool		greatComplex(ComplexNb const & thisC, ComplexNb const & target)
{
	return abs(thisC) < abs(target);
}

/*
** Other operators
*/

std::ostream &printComplex(ComplexNb const & target)
{
	std::cout << target.re;

	if (target.im < 0)
		std::cout << " - ";
	else
		std::cout << " + ";
	
	std::cout << fabs(target.im);
	std::cout << "i";

	return std::cout;
}

/*
** Functions
*/

double		abs(ComplexNb const & target)
{
	return sqrt(target.re * target.re + target.im * target.im);
}
