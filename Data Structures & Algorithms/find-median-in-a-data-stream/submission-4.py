class MedianFinder:

    def __init__(self):
        # maxheap za brojeve manji od medijane
        # minheap za brojeve vece od medijane
        # medijana uvek ili jedan od vrhova ili prosek vrhova
        self.left = [0]
        self.right = [0]

    def addLeft(self, num):
        self.left.append(num)
        current = len(self.left) - 1
        while current > 1:
            if self.left[current] > self.left[current//2]:
                self.left[current], self.left[current//2] = self.left[current//2], self.left[current] 
                current = current//2
            else:
                break
            
    def addRight(self, num):
        self.right.append(num)
        current = len(self.right) - 1
        while current > 1:
            if self.right[current] < self.right[current//2]:
                self.right[current], self.right[current//2] = self.right[current//2], self.right[current] 
                current = current//2
            else:
                break

    def popLeft(self):
        last = len(self.left) - 1
        current = 1
        self.left[last], self.left[current] = self.left[current], self.left[last]
        toReturn = self.left.pop()

        while current*2 < len(self.left):
            if (current*2) + 1 >= len(self.left):
                if self.left[current] < self.left[current*2]:
                    self.left[current], self.left[current*2] = self.left[current*2], self.left[current]
                    current = current*2
                else:
                    break
            else:
                if self.left[current*2] >= self.left[(current*2) + 1]:
                    if self.left[current] < self.left[current*2]:
                        self.left[current], self.left[current*2] = self.left[current*2], self.left[current]
                        current = current*2
                    else:
                        break
                else:
                    if self.left[current] < self.left[(current*2) + 1]:
                        self.left[current], self.left[(current*2) + 1] = self.left[(current*2) + 1], self.left[current]
                        current = (current*2) + 1
                    else:
                        break
        return toReturn

    def popRight(self):
        last = len(self.right) - 1
        current = 1
        self.right[last], self.right[current] = self.right[current], self.right[last]
        toReturn = self.right.pop()

        while current*2 < len(self.right):
            if (current*2) + 1 >= len(self.right):
                if self.right[current] > self.right[current*2]:
                    self.right[current], self.right[current*2] = self.right[current*2], self.right[current]
                    current = current*2
                else:
                    break
            else:
                if self.right[current*2] <= self.right[(current*2) + 1]:
                    if self.right[current] > self.right[current*2]:
                        self.right[current], self.right[current*2] = self.right[current*2], self.right[current]
                        current = current*2
                    else:
                        break
                else:
                    if self.right[current] > self.right[(current*2) + 1]:
                        self.right[current], self.right[(current*2) + 1] = self.right[(current*2) + 1], self.right[current]
                        current = (current*2) + 1
                    else:
                        break

        return toReturn


    def addNum(self, num: int) -> None:
        if num <= self.findMedian():
            #print("Adding " + str(num) + " to left")
            self.addLeft(num)
        else:
            #print("Adding " + str(num) + " to right")
            self.addRight(num)
        
        if len(self.left) - len(self.right) >= 2:
            #print("Left is too big, switching to right")
            self.addRight(self.popLeft())
        elif len(self.right) - len(self.left) >= 2:
            #print("Right is too big, switching to left")
            self.addLeft(self.popRight())

    def findMedian(self) -> float:
        leftLen = len(self.left)
        rightLen = len(self.right)

        if leftLen > rightLen:
            return self.left[1]
        elif rightLen > leftLen:
            return self.right[1]
        elif leftLen==rightLen==1:
            return 0
        else:
            return (self.left[1] + self.right[1])/2
        