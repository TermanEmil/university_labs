#include "StateWorker.hpp"

StateWorker::StateWorker(std::string name) : Worker(name)
{
}

float StateWorker::Salary() const
{
	return TimeWorked() * 42 * 1;
}