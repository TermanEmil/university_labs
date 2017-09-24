#ifndef MATRIX_HPP
# define MATRIX_HPP

# include <string>
# include <iostream>
# include <errno.h>

class Matrix
{
public:
	enum			EMatrixErrno {
						boundsErr = 1,
						invalidSize,
						enomem = ENOMEM
	};

	mutable int		mErrno;

	int				getLines(void) const;
	int				getCols(void) const;

	Matrix(void);
	Matrix(int lines, int cols);
	Matrix(Matrix const & target);
	~Matrix(void);

	//Utils
	void			assignAll(int value);

	//Operators
	Matrix &		operator = (Matrix const & target);

	int	const *		operator [] (int i) const;
	int	*			operator [] (int i);

	Matrix			operator + (Matrix const & target) const;
	Matrix			operator - (Matrix const & target) const;
	Matrix			operator * (Matrix const & target) const;
	Matrix			operator * (int nb) const;

private:
	int				**_tab;
	int				_lines;
	int				_cols;

	//Utils
	void			_delTab(void);
	int				_newTab(int lines, int cols);
};

std::ostream &		operator << (std::ostream & o, Matrix const & target);

#endif