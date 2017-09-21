#include "Matrix.hpp"

void	checkAdditionAndSubstr(void) {
	std::cout << "Addition & substraction" << std::endl;

	Matrix	matrix1(2, 2);
	Matrix	matrix2;

	matrix1.setCel(1, 0, 0);
	matrix1.setCel(2, 1, 1);

	matrix2 = matrix1;
	matrix2.setCel(42, 0, 1);

	std::cout << matrix1;
	std::cout << matrix2;

	std::cout << matrix1 + matrix2 << std::endl;
	std::cout << matrix1 + matrix2 << std::endl;

	Matrix matrix3(5, 5);

	std::cout << matrix1 + matrix3;
	std::cout << "error: " << matrix1.mErrno << std::endl;
}

void	checkMultiplication(void) {
	std::cout << "Multiplication" << std::endl;

	Matrix	matrix1(3, 2);
	Matrix	matrix2(2, 5);

	matrix1.setCel(1, 0, 0);
	matrix1.setCel(1, 0, 1);
	matrix1.setCel(1, 1, 0);
	matrix1.setCel(1, 2, 1);

	matrix2.setCel(2, 0, 0);
	matrix2.setCel(2, 0, 1);
	matrix2.setCel(2, 0, 2);
	matrix2.setCel(2, 0, 3);
	matrix2.setCel(2, 1, 4);

	std::cout << "matrix1:\n" << matrix1;
	std::cout << "matrix2:\n" << matrix2;

	std::cout << "matrix1 x matrix2:\n" << matrix1 * matrix2;
}

int		main(void) {
	checkAdditionAndSubstr();
	checkMultiplication();
	return 0;
}