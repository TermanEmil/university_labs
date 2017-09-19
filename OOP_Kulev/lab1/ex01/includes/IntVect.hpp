#ifndef INTVECT_HPP
# define INTVECT_HPP

# include <string>
# include <iostream>

struct		IntVect
{
	int		*elements;
	size_t	count;
};

// std::ostream & operator << (std::ostream & o, IntVect const & target);

std::ostream &printIntVect(IntVect const & target);

/*
** Constructors / destructors
*/

IntVect		newIntVect(void);
IntVect		newIntVect(size_t count);
IntVect		newIntVect(int const *elements, size_t count);
IntVect		newIntVect(IntVect const & target);
void		delIntVect(IntVect & target);

/*
** Other functions
*/

int			setSizeIntVect(IntVect & target, size_t newSize);
int			getElementIntVect(IntVect const & target, int index);
double		absIntVect(IntVect const & target);

#endif