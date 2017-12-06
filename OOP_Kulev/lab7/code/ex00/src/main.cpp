#include <iostream>
#include <vector>
#include <algorithm>
#include <functional>

template <typename T>
std::vector<T> myShuffle(std::vector<T> tab)
{
	std::vector<T> result;

	if (tab.size() <= 1)
		return std::vector<T>(tab);

	for (auto it = tab.begin() + tab.size() / 2; it < tab.end(); it++)
		result.push_back(*it);

	for (auto it = tab.begin(); it < tab.begin() + tab.size() / 2; it++)
		result.push_back(*it);
	return result;
}

template <typename T>
std::ostream & operator<<(std::ostream & o, std::vector<T> const & tab)
{
	for (T viktor: tab)
		o << viktor << " ";
	return o;
}

int main()
{
	std::vector<int> tab[5] =
	{
		{1},
		{1, 2},
		{1, 2, 3},
		{1, 2, 3, 4},
		{1, 2, 3, 4, 5, 6}
	};

	for (int i = 0; i < 5; i++)
		std::cout << myShuffle<int>(tab[i]) << std::endl;

	std::vector<char> cTab[3] =
	{
		{'A'},
		{'A', 'B', 'C'},
		{'A', 'B', 'C', 'D'},
	};

	for (int i = 0; i < 3; i++)
		std::cout << myShuffle<char>(cTab[i]) << std::endl;
	return 0;
}