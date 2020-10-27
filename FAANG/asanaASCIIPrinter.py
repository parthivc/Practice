from collections import deque


class Printer:

    # Optimizations: 
    # Use a doubly-linked list + hashmap for better cell performance
    # Implement bounds checking

    def __init__(self):
        grid = []
        for _ in range(6):
            grid.append([deque() for x in range(10)])
        self.grid = grid
        self.counter = 0

    # parse command
    def parseCommand(self, arg):
        args = arg.split()
        if args:
            command = args[0]
            if command == "DRAW_RECTANGLE":
                self.drawRectangle(*args[1:])
            elif command == "ERASE_AREA":
                self.erase(*args[1:])
            elif command == "DRAG_AND_DROP":
                self.dragAndDrop(*list(map(int, args[1:])))
            elif command == "BRING_TO_FRONT":
                self.bringToFront(*list(map(int, args[1:])))
            elif command == "PRINT_CANVAS":
                self.printCanvas()
            else:
                print("\nInvalid command, please try again")
        else:
            print("\nInvalid command, please try again")

    def printCanvas(self):
        print("\n    ", end="")
        for x in range(len(self.grid[0])):
            print(x, end="   ")
        print()
        print("  ", end="-")
        for x in range(len(self.grid[0])):
            print("----", end="")
        print()
        for index, row in enumerate(self.grid):
            print(index, end=" | ")
            for elem in row:
                print(elem[0][0] if elem else " ", end=" | ")
            print()
            print("  ", end="-")
            for x in range(len(self.grid[0])):
                print("----", end="")
            print()

    def drawRectangle(self, char, topLeftX, topLeftY, bottomRightX, bottomRightY):
        topLeftX, topLeftY, bottomRightX, bottomRightY = int(topLeftX), int(topLeftY), int(bottomRightX), int(bottomRightY)
        for y in range(topLeftX, bottomRightX + 1):
            for x in range(topLeftY, bottomRightY + 1):
                self.grid[x][y].appendleft((char, self.counter))
        self.counter += 1

    def erase(self, topLeftX, topLeftY, bottomRightX, bottomRightY):
        topLeftX, topLeftY, bottomRightX, bottomRightY = int(topLeftX), int(topLeftY), int(bottomRightX), int(bottomRightY)
        for y in range(topLeftX, bottomRightX + 1):
            for x in range(topLeftY, bottomRightY + 1):
                self.grid[x][y].clear()

    def bringToFront(self, y, x):
        current = self.grid[x][y][0]
        gridID = current[1]
        for row in self.grid:
            for elem in row:
                for index in range(len(elem)):
                    if elem[index][1] == gridID:
                        del elem[index]
                        elem.appendleft(current)
                        break
    
    def dragAndDrop(self, startY, startX, endY, endX):
        current = (self.grid[startX][startY][0][0], self.counter)
        gridID = self.grid[startX][startY][0][1]
        xDif = -abs(startX - endX)
        yDif = abs(startY - endY)
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):
                elem = self.grid[row][col]
                for index in range(len(elem)):
                    if elem[index][1] == gridID:
                        del elem[index]
                        self.grid[row + xDif][col + yDif].append(current)
                        break
        self.counter += 1


def main():
    p = Printer()
    while True:
        args = input("\nEnter command: ")
        if args.lower().strip() == "exit":
            break
        p.parseCommand(args)
    print()


if __name__ == "__main__":
    main()