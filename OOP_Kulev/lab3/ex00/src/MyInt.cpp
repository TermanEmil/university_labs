#include "MyInt.hpp"

//Getters
int		MyInt::getVal(void) const {return _value;}

//Constructors
MyInt::MyInt(void) {
	_value = 0;
}

MyInt::MyInt(int const value) {
	_value = value;
}

MyInt::MyInt(MyInt const & target) {
	_value = target.getVal();
}

/*
** Operators
*/

MyInt const & MyInt::operator = (MyInt const & target) {
	_value = target.getVal();
	return *this;
}

//Pre
MyInt MyInt::operator + (MyInt const & target) const {
	return MyInt(getVal() + target.getVal());
}

MyInt MyInt::operator + (int nb) const {
	return MyInt(getVal() + nb);
}

MyInt & MyInt::operator ++ (void) {
	_value++;
	return *this;
}

/*
** Friendly
*/

//With class ref on both sides
MyInt operator - (MyInt const & target1, MyInt const & target2) {
	return MyInt(target1.getVal() - target2.getVal());
}

//With Class ref on the left
MyInt operator - (MyInt const & target, int const nb) {
	return MyInt(target.getVal() - nb);
}

//With Class ref on the right
MyInt operator - (int nb, MyInt const & target) {
	return MyInt(nb - target.getVal());
}

MyInt MyInt::operator -- (int) {
	MyInt	result(*this);

	_value--;
	return result;
}

//Other operators
MyInt::operator int() const {return getVal();}

std::ostream & operator  << (std::ostream & o, MyInt const & target) {
	o << target.getVal();
	return o;
}