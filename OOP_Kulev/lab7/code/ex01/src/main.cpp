#include "stack.h"
#include "generic_node.h"
#include <string>

int main()
{
	auto myStack = Stack<std::string>();
	myStack.Push("1");
	myStack.Push("2");
	myStack.Push("3");
	std::cout << "size(" << myStack.size() << ") " << myStack << std::endl;

	std::cout << myStack.Pop() << std::endl;
	std::cout << myStack << std::endl;

	std::cout << myStack.Pop() << std::endl;
	std::cout << myStack << std::endl;

	std::cin >> myStack;
	std::cout << myStack << std::endl;
	return 0;
}