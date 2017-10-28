#include "Wheel.hpp"
#include "Car.hpp"
#include "Lorry.hpp"

int		main(void) {
	Car car1(4, 10, "Jaguar");
	Lorry lorry1(5, 6, 10, "Plaha");

	std::cout << car1 << std::endl;
	std::cout << lorry1 << std::endl;
	return 0;
}