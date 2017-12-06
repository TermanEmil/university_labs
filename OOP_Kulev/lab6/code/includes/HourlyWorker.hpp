#ifndef HOURLYWORKER_HPP
# define HOURLYWORKER_HPP

# include <string>
# include "Worker.hpp"

class HourlyWorker : public Worker
{
public:
	HourlyWorker(std::string name);
	float Salary() const;
};

#endif