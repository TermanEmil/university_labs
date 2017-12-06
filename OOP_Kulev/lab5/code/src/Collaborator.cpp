#include "Collaborator.hpp"

float Collaborator::Grade() const { return _grade; }

void Collaborator::SetGrade(float newGrade)
{
	_grade = newGrade;
}

Collaborator::Collaborator(std::string name) : Human(name)
{
	_grade = 0;
}