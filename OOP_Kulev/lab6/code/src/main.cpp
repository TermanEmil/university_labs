#include "Worker.hpp"
#include "StateWorker.hpp"
#include "HourlyWorker.hpp"
#include "CommissionWorker.hpp"

#include <iostream>
#include <vector>
#include <stdlib.h>

int main()
{
	std::vector<Worker*> workers;

	workers.push_back(new StateWorker("StateWorker_Kek1"));
	workers.push_back(new HourlyWorker("HourlyWorker_Kek2"));
	workers.push_back(new HourlyWorker("CommissionWorker_Kek3"));

	srand(0);

	for (auto const & w : workers)
	{
		w->SetTimeWorked(rand() % 100);
		std::cout << w->Name() << ": " << w->Salary() << std::endl;
	}
	return 0;
}