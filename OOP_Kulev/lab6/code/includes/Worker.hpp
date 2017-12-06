#ifndef WORKER_HPP
# define WORKER_HPP

# include <string>

class Worker
{
public:
	std::string Name() const;
	float TimeWorked() const;

	void SetTimeWorked(float newTime);

	Worker(std::string name);

	virtual float Salary() const = 0;

private:
	std::string const _name;
	float _timeWorked;
};

#endif