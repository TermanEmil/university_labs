#include "Date.hpp"
#include <sstream>

std::string const Date::_monthNames[12] = {
	"jan", "feb", "mar", "apr", "may", "jun", "aug", "sept", "oct", "nov", "dec"
};

/*
** Getters
*/

int		Date::getDay(void) const {return _day;}
int		Date::getMonth(void) const {return _month;}
int		Date::getYear(void) const {return _year;}

/*
** Setters
*/

void	Date::setDay(int const day) {
	if (day > _monthMaxDays())
		throw InvalidDate();

	_day = day;
}

void	Date::setMonth(int const month) {
	if (month < 1 || month > 12)
		throw InvalidDate();

	_month = month;
}

void	Date::setYear(int const year) {
	if (year < 0)
		throw InvalidDate();

	_year = year;
}

/*
** Constructors & destructors
*/

Date::Date(void) {
	setYear(0);
	setMonth(1);
	setDay(1);
}

Date::Date(int const day, int const month, int const year) {
	setYear(year);
	setMonth(month);
	setDay(day);
}

Date::Date(Date const & target) {*this = target;}

Date::~Date(void) {}

/*
** Other functions
*/

bool	Date::isLeapYear(void) const {
	return (_year % 100 == 0) ? (_year % 400 == 0) : (_year % 4 == 0);
}

std::string	Date::toStrNamedMonth(void) const {
	std::ostringstream	os;

	os << getDay() << " " << _monthNames[getMonth() - 1] << " " << getYear();
	return os.str();
}

std::string	Date::toStr(void) const {
	std::ostringstream	os;

	os << getDay() << "." << getMonth() << "." << getYear();
	return os.str();
}

//Returns the maximum number of days this month can have in this year.
int		Date::_monthMaxDays(void) const {
	if (_month == apr || _month == jun || _month == sept || _month == nov)
		return 30;
	else if (_month != feb)
		return 31;
	else
		return isLeapYear() ? 29 : 28;
}

/*
** Operators
*/

Date	& Date::operator = (Date const & target) {
	setYear(target.getYear());
	setMonth(target.getMonth());
	setDay(target.getDay());

	return *this;
}

std::ostream & operator << (std::ostream & o, Date const & target) {
	o << target.toStr();
	return o;
}

/*
** Exceptions
*/

char const	* Date::InvalidDate::what() const throw () {
	return "Invalid day, month or year";
}