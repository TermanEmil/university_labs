#include "HourlyWorker.hpp"

HourlyWorker::HourlyWorker(std::string name) : Worker(name)
{
}

float HourlyWorker::Salary() const
{
	return TimeWorked() * 42 * 2;
}