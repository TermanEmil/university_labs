#ifndef HUMAN_HPP
# define HUMAN_HPP

# include <iostream>
# include <string>

class Human
{
public:
	std::string Name() const;

	Human(std::string name);
private:
	std::string _name;
};

#endif