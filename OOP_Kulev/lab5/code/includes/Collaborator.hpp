#ifndef COLLABORATOR_HPP
# define COLLABORATOR_HPP

# include <iostream>
# include <string>
# include "Human.hpp"

class Collaborator : public virtual Human
{
public:
	float Grade() const;
	void SetGrade(float newGrade);

	Collaborator(std::string name);

private:
	float _grade;
};

#endif