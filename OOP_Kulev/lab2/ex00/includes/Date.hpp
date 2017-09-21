#ifndef DATE_HPP
# define DATE_HPP

# include <iostream>
# include <string>
# include <stdexcept>

class	Date
{
public:
	class	InvalidDate : public std::exception {
	public:
		virtual const char * what() const throw();
	};

	enum	EMonth {
		jan = 1, feb, mar, apr, may, jun, jul, aug, sept, oct, nov, dec
	};

	//Getters
	int		getDay(void) const;
	int		getMonth(void) const;
	int		getYear(void) const;

	//Setters
	void	setDay(int day);
	void	setMonth(int month);
	void	setYear(int year);

	//Constr & destr
	Date(void);
	Date(int day, int month, int year);
	Date(Date const & target);
	~Date(void);

	bool	isLeapYear(void) const;
	std::string	toStrNamedMonth(void) const;
	std::string	toStr(void) const;


	//Operators
	Date & operator = (Date const & target);

private:
	static const std::string _monthNames[12];

	int			_day;
	int			_month;
	int			_year;

	int			_monthMaxDays(void) const;
};

std::ostream & operator << (std::ostream & o, Date const & target);

#endif