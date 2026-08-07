type MinStack struct {
    stack *linkedliststack.Stack
}

func Constructor() MinStack {
    return MinStack{stack: linkedliststack.New()}
}

func (this *MinStack) Push(val int) {
    this.stack.Push(val)
}

func (this *MinStack) Pop() {
    this.stack.Pop()
}

func (this *MinStack) Top() int {
    top, _ := this.stack.Peek()
    return top.(int)
}

func (this *MinStack) GetMin() int {
    tmp := linkedliststack.New()
    min := this.Top()

    for !this.stack.Empty() {
        val, _ := this.stack.Pop()
        min = getMin(min, val.(int))
        tmp.Push(val)
    }

    for !tmp.Empty() {
        val, _ := tmp.Pop()
        this.stack.Push(val)
    }

    return min
}

func getMin(a, b int) int {
    if a < b {
        return a
    }
    return b
}
