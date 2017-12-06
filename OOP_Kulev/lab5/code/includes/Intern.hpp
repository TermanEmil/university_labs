#ifndef INTER_HPP
# define INTER_HPP

# include <iostream>
# include <string>
# include "Student.hpp"
# include "Collaborator.hpp"

class Intern : public Student, public Collaborator
{
public:
	Intern(std::string name, std::string university);
};

#endif