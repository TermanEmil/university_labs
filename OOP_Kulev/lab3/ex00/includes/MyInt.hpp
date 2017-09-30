#ifndef MYINT_HPP
# define MYINT_HPP

# include <ostream>

class MyInt {
public:
	//Getters
	int		getVal(void) const;

	//Constructors
	MyInt(void);
	MyInt(int value);
	MyInt(MyInt const & target);

	//Arithmetic operators
	MyInt operator + (MyInt const & target) const;
	MyInt operator + (int nb) const;

	friend MyInt operator - (MyInt const & target1, MyInt const & target2);
	friend MyInt operator - (MyInt const & target, int nb);
	friend MyInt operator - (int nb, MyInt const & target);

	MyInt & operator ++ (void);
	MyInt operator -- (int);

	MyInt const & operator = (MyInt const & target);

	//Other operators
	operator int() const;

private:
	int	_value;
};

std::ostream & operator  << (std::ostream & o, MyInt const & target);

#endif