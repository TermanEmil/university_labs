#ifndef SET_TPP
# define SET_TPP

# include <ostream>
# include <exception>
# include <iostream>
# include <istream>
# include <initializer_list>

/*
** Custom operators
*/

const struct _opSetIn_ {} in = {};

template <typename T>
class Set {
public:

	/*
	** Exceptions
	*/

	class IndexOutOfRange : public std::exception {
	public:
		virtual char const * what() const throw() {
			return "Index out of range";
		}
	};

	/*
	** Getters
	*/

	size_t		count(void) const;
	T			getDefaultVal(void) const;

	/*
	** Constructors & Destructors
	*/

	Set<T>(void);
	Set<T>(size_t const size);
	Set<T>(size_t const size, T const defaultVal);
	Set<T>(Set<T> const & target);
	Set<T>(T const defaultVal, std::initializer_list<T> args);
	~Set<T>(void);

	//Operators
	Set<T> const &	operator = (Set<T> const & target);
	T &				operator [] (size_t const i) const;
	
	/*
	** Arithmetic operators
	*/

	template <typename U>
	friend Set<U>	operator + (Set<U> const & target1, Set<U> const & target2);

	template <typename U>
	friend Set<U>	operator * (Set<U> const & target1, Set<U> const & target2);

	template <typename U>
	friend Set<U>	operator - (Set<U> const & target1, Set<U> const & target2);

	Set<T> &		operator += (Set<T> const & target);
	
	/*
	** Boolean operators
	*/

	bool		operator == (Set<T> const & target);

	/*
	** IO operators
	*/

	template <typename U>
	friend std::ostream & operator << (std::ostream & o, Set<U> const & target);

	template <typename U>
	friend std::istream & operator >> (std::istream & is, Set<U> & target);

private:
	T *			_tab;
	size_t		_size;
	T const		_defaultVal;
};

/*
** Getters
*/

template <typename T>
size_t		Set<T>::count(void) const {return _size;}

template <typename T>
T			Set<T>::getDefaultVal(void) const {return _defaultVal;}

/*
** Constructors & Destructors
*/

//Default Constructor
template <typename T>
Set<T>::Set(void) : _defaultVal(0)
{
	_tab = new T[0];
	_size = 0;
}

//Constructor with given size
template <typename T>
Set<T>::Set(size_t const size) : _defaultVal(0)
{
	_tab = new T[size];
	_size = size;

	for (size_t i = 0; i < size; i++)
		_tab[i] = _defaultVal;
}

//Constructor with given size and default value
template <typename T>
Set<T>::Set(size_t const size, T const defaultVal) : _defaultVal(defaultVal)
{
	_tab = new T[size];
	_size = size;

	for (size_t i = 0; i < size; i++)
		_tab[i] = _defaultVal;
}

//Copy Constructor
template <typename T>
Set<T>::Set(Set<T> const & target) : _defaultVal(target.getDefaultVal())
{
	_tab = NULL;
	*this = target;
}

//Multiple variable constructor
template <typename T>
Set<T>::Set(T const defaultVal, std::initializer_list<T> args) :
	_defaultVal(defaultVal)
{
	int		i = 0;

	_size = args.size();
	_tab = new T [_size];

	for (T element: args)
		_tab[i++] = element;
}

//Destructor
template <typename T>
Set<T>::~Set(void)
{
	delete [] _tab;
}

//Operators
template <typename T>
Set<T> const &	Set<T>::operator = (Set<T> const & target)
{
	if (&target == this)
		return *this;

	if (_tab)
		delete [] _tab;
	_tab = new T[target.count()];
	_size = target.count();

	for (size_t i = 0; i < target.count(); i++)
		_tab[i] = target[i];

	return *this;
}

template <typename T>
T &				Set<T>::operator [] (size_t const i) const
{
	if (i >= _size)
		throw IndexOutOfRange();

	return _tab[i];
}

/*
** Arithmetic operators
*/

template <typename T>
Set<T>			operator + (Set<T> const & target1, Set<T> const & target2)
{
	Set<T>	result(target1.count() + target2.count(),
		target1.getDefaultVal());

	for (size_t i = 0; i < target1.count(); i++)
		result[i] = target1[i];

	for (size_t i = 0; i < target2.count(); i++)
		result[i + target1.count()] = target2[i];

	return result;
}

template <typename T>
Set<T>			operator * (Set<T> const & target1, Set<T> const & target2)
{
	size_t	len;

	len = 0;
	for (size_t i = 0; i < target1.count(); i++)
		if (target1[i] <in> target2)
			len++;

	Set<T>	result(len, target1.getDefaultVal());
	size_t	k = 0;

	for (size_t i = 0; i < target1.count(); i++)
		if (target1[i] <in> target2) {
			result[k] = target1[i];
			k++;
		}

	return result;
}

template <typename T>
Set<T>			operator - (Set<T> const & target1, Set<T> const & target2)
{
	size_t	len;

	len = target1.count();
	for (size_t i = 0; i < target1.count(); i++)
		if (target1[i] <in> target2)
			len--;

	Set<T>	result(len, target1.getDefaultVal());
	size_t	k = 0;

	for (size_t i = 0; i < target1.count(); i++)
		if (!(target1[i] <in> target2)) {
			result[k] = target1[i];
			k++;
		}

	return result;
}

template <typename T>
Set<T> &		Set<T>::operator += (Set<T> const & target)
{
	T *		newTab;

	newTab = new T [_size + target.count()];
	for (size_t i = 0; i < _size; i++)
		newTab[i] = _tab[i];

	for (size_t i = 0; i < target.count(); i++)
		newTab[i + _size] = target[i];

	delete [] _tab;
	_tab = newTab;
	_size += target.count();

	return *this;
}

/*
** Boolean operators
*/

template <typename T>
bool			Set<T>::operator == (Set<T> const & target)
{
	for (size_t i = 0; i < count(); i++)
		if (!(_tab[i] <in> target))
			return false;

	for (size_t i = 0; i < target.count(); i++)
		if (!(target[i] <in> *this))
			return false;

	return true;
}

/*
** IO operators
*/

template <typename T>
std::ostream & operator << (std::ostream & o, Set<T> const & target)
{
	o << "{";
	for (size_t i = 0; i < target.count(); i++) {
		o << target[i];
		if (i != target.count() - 1)
			o << ", ";
	}
	o << "}";
	return o;
}

template <typename T>
std::istream & operator >> (std::istream & is, Set<T> & target)
{
	size_t	size;

	std::cout << "size: ";
	std::cin >> size;

	target = Set<T> (size, target.getDefaultVal());

	std::cout << "Set = {";
	for (size_t i = 0; i < size; i++) {
		std::cin >> target[i];
	}
	std::cout << "}" << std::endl;
	
	return is;
}

/*
** Custom `<in>' operator
** Ex:
** Set<int> a(3);
** a[0] = 3;
** 3 <in> a == true
*/

template <typename T>
struct				_opSetInProxy
{
	T const &	obj;

	//Constructor
	_opSetInProxy(T const & newObj): obj(newObj) {}
};

template <typename T>
_opSetInProxy<T>	operator < (T const & left, _opSetIn_ const & right)
{
	(void)right;
	return _opSetInProxy<T>(left);
}

template <typename T>
bool				operator > (_opSetInProxy<T> const & left,
						Set<T> const & right)
{

	for (size_t i = 0; i < right.count(); i++)
		if (left.obj == right[i])
			return true;

	return false;
}

#endif