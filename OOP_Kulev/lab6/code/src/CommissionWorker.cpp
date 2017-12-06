#include "CommissionWorker.hpp"

CommissionWorker::CommissionWorker(std::string name) : Worker(name)
{
}

float CommissionWorker::Salary() const
{
	return TimeWorked() * 42 * 3;
}