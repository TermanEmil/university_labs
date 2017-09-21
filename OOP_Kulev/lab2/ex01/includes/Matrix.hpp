#ifndef MATRIX_HPP
# define MATRIX_HPP

# include <string>
# include <iostream>
# include <errno.h>

class Matrix
{
public:
	enum	EMatrixErrno {
		boundsErr = 1, invalidSize, enomem = ENOMEM
	};

	mutable int		mErrno;

	int		getCel(int i, int j) const;
	int		getLines(void) const;
	int		getCols(void) const;

	void	setCel(int newVal, int i, int j);

	Matrix(void);
	Matrix(int lines, int cols);
	Matrix(Matrix const & target);
	~Matrix(void);

	//Operators
	Matrix & operator = (Matrix const & target);

	Matrix operator + (Matrix const & target) const;
	Matrix operator - (Matrix const & target) const;
	Matrix operator * (Matrix const & target) const;

private:
	int		**_tab;
	int		_lines;
	int		_cols;

	//Utils
	void	_delTab(void);
	int		_newTab(int lines, int cols);
};

std::ostream & operator << (std::ostream & o, Matrix const & target);

#endif