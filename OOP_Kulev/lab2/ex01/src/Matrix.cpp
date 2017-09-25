#include "Matrix.hpp"

/*
** Getters
*/

int		Matrix::getLines(void) const {return (_tab == NULL) ? 0 : _lines;}
int		Matrix::getCols(void) const {return (_tab == NULL) ? 0 : _cols;}

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

void	Matrix::assignAll(int const value) {
	if (_tab == NULL)
		return;

	for (int i = 0; i < _lines; i++)
		for (int j = 0; j < _cols; j++)
			_tab[i][j] = value;
}

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
			_lines = i;
			_delTab();
			_lines = 0;
			return -1;
		}
	}

	_lines = lines;
	_cols = cols;
	assignAll(0);
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
			_tab[i][j] = target[i][j];

	return *this;
}

int	*		Matrix::operator [] (int const i) {return _tab[i];}
int	const *	Matrix::operator [] (int const i) const {return _tab[i];}


/*
** Arithmetic operators
*/

Matrix Matrix::operator + (Matrix const & target) const {
	if (target.getLines() != _lines || target.getCols() != _cols) {
		mErrno = invalidSize;
		return Matrix();
	}

	Matrix	result(*this);

	if (result.mErrno != 0)
		return result;

	for (int i = 0; i < _lines; i++)
		for (int j = 0; j < _cols; j++)
			result[i][j] = _tab[i][j] + target[i][j];

	return result;
}

Matrix Matrix::operator - (Matrix const & target) const {
	if (target.getLines() != _lines || target.getCols() != _cols) {
		mErrno = invalidSize;
		return Matrix();
	}

	Matrix	result(*this);

	if (result.mErrno != 0)
		return result;

	for (int i = 0; i < _lines; i++)
		for (int j = 0; j < _cols; j++)
			result[i][j] = _tab[i][j] - target[i][j];

	return result;
}

Matrix Matrix::operator * (Matrix const & target) const {
	int sum;

	if (target.getCols() != target.getLines()) {
		mErrno = invalidSize;
		return Matrix();
	}

	Matrix	result(_lines, target.getCols());

	if (result.mErrno != 0)
		return result;

	for (int i = 0; i < _lines; i++) {
		for (int j = 0; j < target.getCols(); j++) {
			sum = 0;
			for (int k = 0; k < _cols; k++)
				sum += (_tab[i][k]) * (target[k][j]);
			result[i][j] = sum;
		}
	}

	return result;
}

Matrix Matrix::operator * (int const nb) const {
	if (_tab == NULL)
		return Matrix();

	Matrix	result(_lines, _cols);

	if (result.mErrno != 0)
		return result;

	for (int i = 0; i < _lines; i++)
		for (int j = 0; j < _cols; j++)
			result[i][j] = _tab[i][j] * nb;

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
			o << target[i][j];
			if (j != target.getCols() - 1)
				o << ",\t";
		}
		o << "}" << std::endl;
	}
	o << "}" << std::endl;
	return o;
}