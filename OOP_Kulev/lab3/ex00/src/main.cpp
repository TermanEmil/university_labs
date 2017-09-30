#include "MyInt.hpp"

#include <iostream>

int		main(void) {
	MyInt	a(3);
	MyInt	b(5);

	std::cout << "a + b = " << a + b << std::endl;
	std::cout << "a + 5 = " << a + 5 << std::endl;
	std::cout << "3 + b = " << 3 + b << std::endl;

	std::cout << "a - b = " << a - b << std::endl;
	std::cout << "a - 5 = " << a - 5 << std::endl;
	std::cout << "3 - b = " << 3 - b << std::endl;

	std::cout << "----------" << std::endl;
	std::cout << "a = " << a << std::endl;
	std::cout << "++a: " << ++a << std::endl;
	std::cout << "a = " << a << std::endl;

	std::cout << "----------" << std::endl;
	std::cout << "a--: " << a-- << std::endl;
	std::cout << "a = " << a << std::endl;
	std::cout << "----------" << std::endl;

	int intA = a;
	std::cout << "int aInt = a; aInt = " << intA << std::endl;

	return 0;
}