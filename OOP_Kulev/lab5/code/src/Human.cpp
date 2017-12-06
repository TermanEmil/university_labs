#include "Human.hpp"

std::string Human::Name() const
{
	return _name;
}

Human::Human(std::string name)
{
	_name = name;
}