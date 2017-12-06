#ifndef COMMISSIONWORKER_HPP
# define COMMISSIONWORKER_HPP

# include <string>
# include "Worker.hpp"

class CommissionWorker : public Worker
{
public:
	CommissionWorker(std::string name);
	float Salary() const;
};

#endif