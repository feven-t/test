class Array:
    def __init__(self, size, datatype):
        self.datatype = datatype
        self.array = [None] * size
        self.currentSize = 0
        self.size = size

    def insert(self, item, index):
        if index >= self.size:
            raise IndexError("Index out of range " + str(index))
        if not isinstance(item, self.datatype):
            raise ValueError("Expected " + str(self.datatype))
        self.shift(index)
        self.array[index] = item

    def shift(self, base_index):
        if self.array[-1] != None:
            raise Exception("Final item will be lost")

        for i, item in enumerate(self.array[base_index:-1]):
            self.array[base_index + 1 + i] = item
        self.array[base_index] = None

    def __getitem__(self, item):
        return self.array[item]

    def reverse(self):
        for i in range(self.size // 2):
            self.array[i], self.array[self.size - i - 1] = self.array[self.size - i - 1], self.array[i]

    def remove(self, index):
        self.array[index] = None

    def __str__(self):
        return str(self.array)


class Stack:
    def __init__(self, size, datatype):
        self.top = 0
        self.size = size
        self.datatype = datatype
        self.newStack = Array(self.size,self.datatype)

    def Length(self):
        return self.size

    def isEmpty(self):
        if self.top == 0:
            return True
        else:
            return False

    def isFull(self):
        if self.top == self.size:
            return True
        else:
            return False

    def push(self, item):
        if self.top < self.size:
            self.newStack.insert(item, self.top)
            self.top += 1

    def pop(self):
        value = self.newStack[self.top - 1]
        self.top -= 1
        return value

    def peek(self):
        return self.newStack[self.top - 1]
def valin(inn):
    S=Stack(len(inn),str)
    for i in inn:   # iterate through every element of the file

        val=""  # variable for containing the start tag
        popper="<"   #variable for containing the end tag but intially have < because behuala '/' ignore argo compare lemareg endimechen new
        if i == "<": #the element < kehone
            y = inn.find(i)   # '<' yhenin yagegnehbetn index yazina le y stew
            x = inn.find(" ", y)   # the first space( ) after the < element stagegn yanin index yzeh le x stew
            z = inn.find(">", y)    # the next > after the < stagegn index yzeh le z stew
            if inn[y+1]!="/":   # yihe < tegegnto ketayu cxr / kalhone yhenin sira
                val+= (inn[y:x] + inn[z])   #update the val variable to kezih < jemro eske space dres + inn[z], which means the next >
                S.push(val)     #yhen val stack wist asgebaw
                val = ""         #make val empty
            elif inn[y+1]=="/":    # yihe < tegegnto ketayu cxr / kehone degmo yhenin sira
                popper+=inn[y+2:z+1]   #add on popper the cxrs after inn[y+2],which is after / until you get > cxr

                if S.peek()!=popper:      #the pooper and mecheresha lay push yarekew neger same kalhone raise exception
                    raise Exception ("html not right")
                                        #kezih behuala yalewn egziyabher new miyakew
                v = S.pop()
                print(v)
                popper="<"


    print(S.isEmpty())
inp= """<html>
<p>Hello</p>
</html>"""
valin(inp)