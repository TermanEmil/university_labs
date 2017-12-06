#include "Student.hpp"

std::string Student::University() const { return _university; }
float Student::Grade() const { return _grade; }

void Student::SetGrade(float newGrade)
{
	_grade = newGrade;
}

Student::Student(std::string name, std::string university) : Human(name)
{
	_university = university;
	_grade = 0;
}
