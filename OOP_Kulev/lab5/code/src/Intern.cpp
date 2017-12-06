#include "Intern.hpp"

Intern::Intern(std::string name, std::string university) :
	Human(name),
	Student(name, university),
	Collaborator(name)
{
}