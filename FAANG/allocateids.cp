#include <bits/stdc++.h>
using namespace std;

class IDAllocator{
public:
	// constructor 
	IDAllocator(int _max_size){
		tree.resize(2*_max_size, false);
		max_size = _max_size;
		curr_size = 0;
	}
	
	// allocate ID
	int allocateID(){
		if(curr_size == max_size)
			throw("Error: All IDs have been allocated");
		int index = 0, left_child = 0, right_child = 0;
		while(index < max_size-1){
			left_child = (2 * index) + 1;
			right_child = (2 * index) + 2;
			if(tree[left_child] == false)
				index = left_child;
			else if(tree[right_child] == false)
				index = right_child;
			else 
				throw("Error: Error in Tree");
		}
		tree[index] = true;
		updateTree(index);
		curr_size++;
		return index - max_size + 2;
	}
	
	// release ID
	void releaseID(int ID){
		if(ID <= 0 || ID > max_size)
			throw("Error: Given ID is out of range of IDs");
		int index = ID + max_size - 2;
		if(tree[index] == false)
			throw("Error: Given ID to release not allocated");
		tree[index] = false;
		updateTree(index);
		curr_size--;
	}
	
	// update tree()
	void updateTree(int index){
		int parent = (index - 1) / 2; 
		while(parent > 0){
			if(tree[2 * parent + 1] == true && tree[2 * parent + 2] == true)
				tree[parent] = true;
			else
				tree[parent] = false;
			parent = (parent - 1) / 2;
		}
		tree[0] = tree[1] & tree[2];
	}
	
private:
	vector<bool> tree;
	int max_size, curr_size;
};

int main(){
	int n;
	cin >> n;
	IDAllocator test(n);
	for(int i = 0; i < n; i++){
		try{
			cout << test.allocateID() << endl;
		}catch (const char* msg){
			cout << msg << endl;
		}
	}
	for(int i = n-1; i >= 5; i--){
		try{
			test.releaseID(i);
		}catch (const char* msg){
			cout << msg << endl;
		}
	}
	for(int i = 5; i < n; i++){
		try{
			cout << test.allocateID() << endl;
		}catch (const char* msg){
			cout << msg << endl;
		}
	}
	return 0;
}