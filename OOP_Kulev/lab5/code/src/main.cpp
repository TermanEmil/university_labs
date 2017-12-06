#include "Human.hpp"
#include "Student.hpp"
#include "Collaborator.hpp"
#include "Intern.hpp"

int main()
{
	Intern intern = Intern("emil", "UTM");

	std::cout << intern.Name() << std::endl;
	std::cout << intern.University() << std::endl;

	intern.Student::SetGrade(10);
	intern.Collaborator::SetGrade(11);

	std::cout << intern.Student::Grade() << std::endl;
	std::cout << intern.Collaborator::Grade() << std::endl;
	return 0;
}