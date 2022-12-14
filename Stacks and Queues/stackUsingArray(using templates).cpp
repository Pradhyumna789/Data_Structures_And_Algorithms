stemplate<typename T>

class stackUsingArray {

private:
T *data;
int capacity;
int nextIndex;

public:
stackUsingArray() {

 data = new T[4] // suppose for now the size of the stack in the form of array is 4
 nextIndex = 0;
 capacity = 4;

}

int size() {

 return nextIndex;   

}

bool isEmpty() {

if (nextIndex == 0) {

return true;

}

else {

return false;

}

// shorter form of the above if-else code would be - [return nextIndex == 0;]

}


void push(int element) {

if (nextIndex == capacity) {

T *newData = new T[2 * capacity];

for (int i = 0; i < capacity; i++) {

newData[i] = data[i];

}

delete [] data;
data = newData;
capacity = 2 * capacity;

}


data[nextIndex] = element;
nextIndex++;


}


T pop() {

if (isEmpty()) {

cout << "Stack is empty" << endl;
return INT_MIN;

}

}

nextIndex--;
return data[nextIndex];


}

T top() {

if (isEmpty()) {

cout << "Stack is empty" << endl;
return INT_MIN;

}

return data[nextIndex - 1];

}
