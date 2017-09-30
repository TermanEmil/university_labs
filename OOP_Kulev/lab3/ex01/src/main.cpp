#include "Set.tpp"
#include <iostream>

void	checkSum(void) {
	Set<int> a(5);

	a[0] = 1;
	a[1] = 2;

	Set<int> b(a);
	b[4] = 5;

	Set<int> c;

	std::cout << a << " + " << b << " + " << c << " = " << a + b << std::endl;

	Set<float> f1(3, 0);
	Set<float> f2;

	f1[2] = 5.1;
	f2 = f1;
	f2[0] = 42.5;

	std::cout << f1 << " + " << f2 << " = " << f1 + f2 << std::endl;

	Set<std::string> s1(5, "");
	Set<std::string> s2(2, "");

	s1[0] = "Adriana";
	s1[1] = "Emil";
	s1[2] = "Sergiu";
	s2[0] = "Alina";
	s2[1] = "Sergiu";

	std::cout << s1 << " + " << s2 << " = " << s1 + s2 << std::endl;

	Set<int> e1;

	std::cout << e1 << " + " << a << " = " << e1 + a << std::endl;
}

void	checkInOperator(void) {
	std::cout << std::endl << "Checking <in> operator" << std::endl;

	Set<std::string> s("", {"a", "b", "cd"});
	std::string needle = "a";

	std::cout << needle << " in " << s << " = " << (needle <in> s) << std::endl;
	needle = "x";
	std::cout << needle << " in " << s << " = " << (needle <in> s) << std::endl;

	Set<std::string> e("", {});

	std::cout << needle << " in " << e << " = " << (needle <in> s) << std::endl;
}

void	checkIntersection(void) {
	std::cout << std::endl << "Intersection check:" << std::endl;

	Set<int>	a(0, {1, 2, 42, -1, -1});
	Set<int>	b(0, {1, -2, 42});

	std::cout << a << " * " << b << " = " << a * b << std::endl;

	Set<std::string> s1("", {"S1", "S2", "S3"});
	Set<std::string> s2("", {"S1", "S2", "S", "S", "S"});

	std::cout << s1 << " * " << s2 << " = " << s1 * s2 << std::endl;

	Set<int>	e1;
	Set<int>	e2;

	std::cout << e1 << " * " << e2 << " = " << e1 * e2 << std::endl;
	std::cout << e1 << " * " << a << " = " << e1 * a << std::endl;
	std::cout << b << " * " << e1 << " = " << b * e1 << std::endl;
}

void	checkDifference(void) {
	std::cout << std::endl << "Difference check:" << std::endl;

	Set<int>	a(0, {1, 2, 3, 4});
	Set<int>	b(0, {1, 4, -1, -2});

	std::cout << a << " - " << b << " = " << a - b << std::endl;

	Set<int>	e(0, {});
	std::cout << e << " - " << b << " = " << e - b << std::endl;
	std::cout << a << " - " << e << " = " << a - e << std::endl;
}

void	checkAdd(void) {
	std::cout << std::endl << "Add check:" << std::endl;

	Set<int>	a(0, {1, 2, 3});
	Set<int>	b(0, {5});
	Set<int>	tmp(a);

	std::cout << tmp << " += " << b << " = " << (a += b) << std::endl;
	b = Set<int> (0, {});
	tmp = a;
	std::cout << tmp << " += " << b << " = " << (a += b) << std::endl;
}

void	checkEqual(void) {
	std::cout << std::endl << "Equality check:" << std::endl;

	Set<int>	a(0, {1, 2, 3});
	Set<int>	b(0, {5});

	std::cout << a << " == " << b << " = " << (a == b) << std::endl;

	b = Set<int> (0, {1, 2, 3, 3, 2, 1, 2});
	std::cout << a << " == " << b << " = " << (a == b) << std::endl;

	b = Set<int> (0, {1, 2, 3, 4});
	std::cout << a << " == " << b << " = " << (a == b) << std::endl;

	a = Set<int> (0, {1, 2, 3, 4, 5});
	std::cout << a << " == " << b << " = " << (a == b) << std::endl;
}

void	checkReading(void) {
	std::cout << std::endl << "Reading check:" << std::endl;

	Set<int> a(0, 0);
	std::cout << "Integer set:" << std::endl;
	std::cin >> a;
	std::cout << "a = " << a << std::endl;

	Set<std::string> s(0, "");
	std::cout << "String set:" << std::endl;
	std::cin >> s;
	std::cout << "s = " << s << std::endl;
}

void	checkOutOfRange(void) {
	std::cout << std::endl << "Out of range check:" << std::endl;
	Set<int> a(5);

	try
	{
		a[5] = 0;
	}
	catch (Set<int>::IndexOutOfRange const & e)
	{
		std::cout << e.what() << std::endl;
	}
}

int		main(void) {
	checkSum();
	checkInOperator();
	checkIntersection();
	checkDifference();
	checkAdd();
	checkEqual();
	checkOutOfRange();

	// checkReading();
	return 0;
}