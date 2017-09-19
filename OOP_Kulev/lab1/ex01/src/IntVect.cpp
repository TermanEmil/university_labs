#include "IntVect.hpp"
#include <exception>
#include <algorithm>
#include <cmath>

/*
** Constructors / destructors
*/

IntVect		newIntVect(void)
{
	IntVect	result;

	result.elements = NULL;
	result.count = 0;
	return result;
}

IntVect		newIntVect(size_t count)
{
	IntVect	result;

	if (count == 0)
		result.elements = NULL;
	else
	{
		result.elements = new int[count];
		if (result.elements == NULL)
			return newIntVect();
	}

	for (int i = 0; i < count; i++)
		result.elements[i] = 0;

	result.count = count;
	return result;
}

IntVect		newIntVect(int const *elements, size_t count)
{
	IntVect	result;

	result = newIntVect(count); 
	if (result.count != count)
		return newIntVect();

	for (int i = 0; i < count; i++)
		result.elements[i] = elements[i];

	return result;
}

IntVect		newIntVect(IntVect const & target)
{
	return newIntVect(target.elements, target.count);
}

void		delIntVect(IntVect & target)
{
	if (target.elements != NULL)
		delete [] target.elements;
}

/*
** operators
*/

std::ostream &printIntVect(IntVect const & target)
{
	size_t		n;

	if (target.count > 50)
		n = 50;
	else
		n = target.count;

	std::cout << "{";
	for (int i = 0; i < n; i++)
	{
		std::cout << target.elements[i];

		if (i != n - 1)
			std::cout << ", ";
	}
	std::cout << "}";

	return std::cout;
}

// std::ostream & operator << (std::ostream & o, IntVect const & target)
// {
// 	size_t		n;

// 	if (target.count > 50)
// 		n = 50;
// 	else
// 		n = target.count;

// 	o << "{";
// 	for (int i = 0; i < n; i++)
// 	{
// 		o << target.elements[i];

// 		if (i != n - 1)
// 			o << ", ";
// 	}
// 	o << "}";

// 	return o;
// }

/*
** Other functions
*/

int			setSizeIntVect(IntVect & target, size_t const newSize)
{
	int		*newElements;

	newElements = new int[newSize];
	if (newElements == NULL)
		return -1;

	if (target.elements != NULL)
	{
		for (int i = 0; i < std::min(target.count, newSize); i++)
			newElements[i] = target.elements[i];

		delete [] target.elements;
	}

	for (int i = target.count; i < newSize; i++)
		newElements[i] = 0;

	target.elements = newElements;
	target.count = newSize;

	return 0;
}

double		absIntVect(IntVect const & target)
{
	int		result;

	if (target.elements == NULL)
		return 0;

	result = 0;

	for (int i = 0; i < target.count; i++)
		result += target.elements[i] * target.elements[i];

	return sqrt(result);
}

int			getElementIntVect(IntVect const & target, int const index)
{
	return target.elements[index];
}
