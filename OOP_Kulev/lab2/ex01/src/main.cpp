#include "Matrix.hpp"

void	checkAdditionAndSubstr(void) {
	std::cout << "Addition & substraction" << std::endl;

	Matrix	matrix1(2, 2);
	Matrix	matrix2;

	matrix1[0][0] = 1;
	matrix1[1][1] = 2;

	matrix2 = matrix1;
	matrix2[0][1] = 42;

	std::cout << "matrix1:\n" << matrix1;
	std::cout << "matrix2:\n" << matrix2;

	std::cout << "matrix1 + matrix2:\n" << matrix1 + matrix2 << std::endl;

	Matrix matrix3(5, 5);

	std::cout << "matrix3:\n" << matrix3;
	std::cout << "matrix1 + matrix3:\n" << matrix1 + matrix3;
	std::cout << "error: " << matrix1.mErrno << std::endl;
}

void	checkMultiplication(void) {
	std::cout << "\nMultiplication" << std::endl;

	Matrix	matrix1(2, 4);
	Matrix	matrix2(4, 4);

	matrix1[0][0] = 1;	matrix1[1][0] = 0;
	matrix1[0][1] = 3;	matrix1[1][1] = 5;
	matrix1[0][2] = 2;	matrix1[1][2] = -1;
	matrix1[0][3] = 4;	matrix1[1][3] = 6;

	matrix2[0][0] = 1;	matrix2[1][0] = -2;
	matrix2[0][1] = -3;	matrix2[1][1] = 0;
	matrix2[0][2] = 2;	matrix2[1][2] = 3;
	matrix2[0][3] = -4;	matrix2[1][3] = 4;

	matrix2[2][0] = 5;	matrix2[3][0] = 8;
	matrix2[2][1] = -1;	matrix2[3][1] = 9;
	matrix2[2][2] = 6;	matrix2[3][2] = 10;
	matrix2[2][3] = 7;	matrix2[3][3] = 11;

	std::cout << "matrix1:\n" << matrix1;
	std::cout << "matrix2:\n" << matrix2;

	std::cout << "matrix1 x matrix2:\n" << matrix1 * matrix2;
	std::cout << "matrix1 x 10:\n" << matrix1 * 10;
}

int		main(void) {
	checkAdditionAndSubstr();
	checkMultiplication();
	return 0;
}