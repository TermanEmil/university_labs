#include "Date.hpp"

int		main(void)
{
	Date	date1(10, Date::mar, 1997);

	std::cout << date1 << std::endl;
	std::cout << date1.toStrNamedMonth() << std::endl;

	Date	date2(date1);

	try
	{
		date2.setDay(100);
	}
	catch (std::exception const & e)
	{
		std::cout << e.what() << std::endl;
	}

	date2.setMonth(Date::feb);

	try
	{
		date2.setDay(29);
	}
	catch (std::exception const & e)
	{
		std::cout << e.what() << std::endl;
	}

	date2.setYear(2000);
	date2.setDay(29);

	std::cout << date2 << std::endl;

	try
	{
		Date	date3(29, Date::feb, 1998);
	}
	catch (std::exception const & e)
	{
		std::cout << e.what() << std::endl;
	}

	return 0;
}