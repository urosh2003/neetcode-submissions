class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        current = 1
        while self.stack and self.stack[-1][0] <= price:
            oldPrice, days = self.stack.pop()
            current += days
              
        self.stack.append((price, current))
        return self.stack[-1][1]



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)