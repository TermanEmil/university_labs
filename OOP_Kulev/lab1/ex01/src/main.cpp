#include "IntVect.hpp"
#include <algorithm>
#include <cmath>

int		main(void)
{
	int		tab[] = {1, 5, -1, 10};
	IntVect	vect = newIntVect(tab, sizeof(tab) / sizeof(int));

	std::cout << "vect = "; printIntVect(vect) << std::endl;

	setSizeIntVect(vect, 10);
	std::cout << "vect = "; printIntVect(vect) << std::endl;

	setSizeIntVect(vect, 3);
	std::cout << "vect = "; printIntVect(vect) << std::endl;

	std::cout << "abs(vect) = " << absIntVect(vect) << std::endl;

	std::cout << "vect.elements[1] = " << getElementIntVect(vect, 1);
	std::cout << std::endl;

	delIntVect(vect);
	return 0;
}