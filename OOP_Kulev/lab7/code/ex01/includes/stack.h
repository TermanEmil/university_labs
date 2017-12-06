#ifndef STACK_H
# define STACK_H

# include "generic_node.h"
# include <iostream>
# include <string>
# include <exception>
# include <ostream>

template <typename T>
class Stack
{
public:
	class IndexOutOfRange: public std::exception {
	public:
		virtual const char* what() const throw() {
			return "Index is out of range";
		}
	};

	class NoElements: public std::exception {
	public:
		virtual const char* what() const throw() {
			return "No elements in stack";
		}
	};

	int size() const { return size_; }
	bool isEmpty() const { return size() == 0; }

	Stack()
	{
		size_ = 0;
		last_ = nullptr;
	}

	~Stack()
	{
		auto tmp = last_;

		while (last_ != nullptr)
		{
			tmp = last_;
			last_ = last_->prev();
			delete tmp;
		}
	}

	void Push(T newData)
	{
		auto new_node = new GenericNode<T>(newData);
		new_node->set_prev(last_);
		last_ = new_node;
		size_++;
	}

	T Pop()
	{
		if (last_ == nullptr)
			throw NoElements();

		auto target_node = last_;
		T result = target_node->data();
		last_ = last_->prev();

		delete(target_node);
		size_--;
		return result;
	}

	/*
	** Operators
	*/

	T& operator [] (int i)
	{
		auto node_iter = last_;

		while (i > 0)
			if (node_iter == nullptr)
				break;
			else
			{
				node_iter = node_iter->prev();
				i--;
			}

		if (node_iter == nullptr)
			throw IndexOutOfRange();

		return node_iter->data();
	}

	friend std::ostream& operator << (std::ostream& o, const Stack<T>& target)
	{
		auto node_iter = target.last_;

		o << "{";
		while (node_iter != nullptr)
		{
			o << node_iter->data();
			node_iter = node_iter->prev();

			if (node_iter != nullptr)
				o << ", ";
		}
		o << "}";
		return o;
	}

	friend std::istream & operator >> (std::istream & is, Stack<T>& target)
	{
		int size;

		std::cout << "Elements to add: ";
		is >> size;

		for (int i = 0; i < size; i++)
		{
			T new_data;

			std::cout << i << ") ";
			is >> new_data;

			target.Push(new_data);
		}
		return is;
	}

private:
	int size_;
	GenericNode<T>* last_;
};

#endif
