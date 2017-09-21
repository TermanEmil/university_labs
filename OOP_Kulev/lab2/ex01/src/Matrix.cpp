#include "Matrix.hpp"

/*
** Getters & setters
*/

int		Matrix::getCel(int i, int j) const {
	if (i < 0 || i >= _lines || j < 0 || j >= _cols)
	{
		mErrno = boundsErr;
		return (0);
	}
	return _tab[i][j];
}

int		Matrix::getLines(void) const {return (_tab == NULL) ? 0 : _lines;}
int		Matrix::getCols(void) const {return (_tab == NULL) ? 0 : _cols;}

void	Matrix::setCel(int newVal, int i, int j) {
	if (i < 0 || i >= _lines || j < 0 || j >= _cols)
		mErrno = boundsErr;
	else
		_tab[i][j] = newVal;
}

/*
** Constructors & destructors
*/

Matrix::Matrix(void) {
	_tab = NULL;
	_lines = 0;
	_cols = 0;
	mErrno = 0;
}

Matrix::Matrix(int lines, int cols) {
	_tab = NULL;
	mErrno = 0;
	_newTab(lines, cols);
}

Matrix::Matrix(Matrix const & target) {
	_tab = NULL;
	mErrno = 0;
	*this = target;
}

Matrix::~Matrix(void) {_delTab();}

/*
** Utilities
*/

void	Matrix::_delTab(void) {
	if (_tab != NULL) {
		for (int i = 0; i < _lines; i++) {
			if (_tab[i])
				delete [] _tab[i];
		}

		delete [] _tab;
		_tab = NULL;
	}

	_cols = 0;
	_lines = 0;
}

int		Matrix::_newTab(int lines, int cols) {
	if (_tab != NULL)
		_delTab();

	_tab = new int * [lines];

	if (_tab == NULL) {
		mErrno = enomem;
		return -1;
	}

	for (int i = 0; i < lines; i++) {
		_tab[i] = new int [cols];

		if (_tab[i] == NULL) {
			mErrno = enomem;
			for (int i_free = 0; i_free < i; i_free++)
				delete [] _tab[i];
			
			delete [] _tab;
			return -1;
		}

		for (int j = 0; j < cols; j++)
			_tab[i][j] = 0;
	}

	_lines = lines;
	_cols = cols;
	return 0;
}

/*
** Operators
*/

Matrix & Matrix::operator = (Matrix const & target) {
	if (_newTab(target.getLines(), target.getCols()) == -1)
		return *this;

	for (int i = 0; i < _lines; i++)
		for (int j = 0; j < _cols; j++)
			_tab[i][j] = target.getCel(i, j);

	return *this;
}

/*
** Arithmetic operators
*/

Matrix Matrix::operator + (Matrix const & target) const {
	if (target.getLines() != _lines || target.getCols() != _cols) {
		mErrno = invalidSize;
		return Matrix();
	}

	Matrix	result(*this);

	for (int i = 0; i < _lines; i++)
		for (int j = 0; j < _cols; j++)
			result.setCel(_tab[i][j] + target.getCel(i, j), i, j);

	return result;
}

Matrix Matrix::operator - (Matrix const & target) const {
	if (target.getLines() != _lines || target.getCols() != _cols) {
		mErrno = invalidSize;
		return Matrix();
	}

	Matrix	result(*this);

	for (int i = 0; i < _lines; i++)
		for (int j = 0; j < _cols; j++)
			result.setCel(_tab[i][j] - target.getCel(i, j), i, j);

	return result;
}

Matrix Matrix::operator * (Matrix const & target) const {
	int sum;

	if (target.getCols() != target.getLines()) {
		mErrno = invalidSize;
		return Matrix();
	}

	Matrix	result(_lines, target.getCols());

	for (int i = 0; i < _lines; i++) {
		for (int j = 0; j < target.getCols(); j++) {
			sum = 0;
			for (int k = 0; k < _cols; k++)
				sum += _tab[i][k] * target.getCel(k, j);
			result.setCel(sum, i, j);
		}
	}

	return result;
}

/*
** Printing operator
*/

std::ostream & operator << (std::ostream & o, Matrix const & target) {
	o << "{" << std::endl;
	for (int i = 0; i < target.getLines(); i++) {
		o << "\t{";
		for (int j = 0; j < target.getCols(); j++) {
			o << target.getCel(i, j);
			if (j != target.getCols() - 1)
				o << ",\t";
		}
		o << "}" << std::endl;
	}
	o << "}" << std::endl;
	return o;
}