#ifndef STATEWORKER_HPP
# define STATEWORKER_HPP

# include <string>
# include "Worker.hpp"

class StateWorker : public Worker
{
public:
	StateWorker(std::string name);
	float Salary() const;
};

#endif