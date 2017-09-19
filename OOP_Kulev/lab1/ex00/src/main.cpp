#include "ComplexLib.hpp"
#include <iostream>

int		main(void)
{
	ComplexNb	a;
	ComplexNb	b;
	ComplexNb	tmp;

	a = Complex(1.2, 2.5);
	b = Complex(-2, -1.3);

	std::cout << "a: "; printComplex(a) << std::endl;
	std::cout << "b: "; printComplex(b) << std::endl;

	tmp = addComplex(a, b);
	std::cout << "a + b: "; printComplex(tmp) << std::endl;

	tmp = decComplex(a, b);
	std::cout << "a - b: "; printComplex(tmp) << std::endl;

	tmp = multComplex(a, b);
	std::cout << "a * b: "; printComplex(tmp) << std::endl;

	tmp = divComplex(a, b);
	std::cout << "a / b: "; printComplex(tmp) << std::endl;

	std::cout << "a < b: " << lessComplex(a, b) << std::endl;
	std::cout << "a > b: " << greatComplex(a, b) << std::endl;

	std::cout << "abs(a): " << abs(a) << std::endl;
	std::cout << "abs(b): " << abs(b) << std::endl;

	return 0;
}