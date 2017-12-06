#ifndef _GENERIC_NODE_H_
# define _GENERIC_NODE_H_

# include <iostream>

template <typename T>
class GenericNode {
public:
	T& data() { return data_; }
	GenericNode* next() const { return next_; }
	GenericNode* prev() const { return prev_; }

	void set_data(T new_data) { data_ = new_data; }
	void set_next(GenericNode* new_next) { next_ = new_next; }
	void set_prev(GenericNode* new_prev) { prev_ = new_prev; }

	GenericNode(T data)
	{
		next_ = nullptr;
		prev_ = nullptr;
		data_ = data;
	}

private:
	GenericNode<T>* next_;
	GenericNode<T>* prev_;

	T data_;
};

#endif