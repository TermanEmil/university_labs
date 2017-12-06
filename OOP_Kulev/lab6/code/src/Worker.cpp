#include "Worker.hpp"

std::string Worker::Name() const { return _name; }
float Worker::TimeWorked() const { return _timeWorked; }

void Worker::SetTimeWorked(float newTime)
{
	_timeWorked = newTime;
}

Worker::Worker(std::string name) : _name(name)
{
	_timeWorked = 0;
}