#ifndef STUDENT_HPP
# define STUDENT_HPP

# include "Human.hpp"
# include <iostream>
# include <string>

class Student : virtual public Human
{
public:
	std::string University() const;
	float Grade() const;
	void SetGrade(float newGrade);

	Student(std::string name, std::string university);

private:
	std::string _university;
	float _grade;
};

#endif