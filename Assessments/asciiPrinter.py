from collections import deque

class Printer:

    def __init__(self):
        self.grid = [[deque() for x in range(10)] for y in range(6)]
        self.gridID = 0

    def parseCommand(self, arg):
        args = arg.split()
        if args:
            command = args[0]
            if command == "DRAW_RECTANGLE":
                args.append(False)
                self.drawRectangle(*args[1:])
            elif command == "ERASE_AREA":
                args.insert(0, ' ')
                args.append(True)  # Used to indicate erase behavior
                self.drawRectangle(*args[1:])
            elif command == "DRAG_AND_DROP":
                args.append(True)
                self.moveRectangle(*list(map(int, args[1:])))
            elif command == "BRING_TO_FRONT":
                args += [0, 0, False]
                self.moveRectangle(*list(map(int, args[1:])))
            elif command == "PRINT_CANVAS":
                self.printCanvas()
            else:
                print("\nInvalid command, please try again")
        else:
            print("\nInvalid command, please try again")

    def inBounds(self, x, y):
        return x > -1 and x < 10 and y > -1 and y < 6

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

    
    # Will not perform any action unless the entire action is valid (all or nothing)
    def errorMessage(self):
        print("\nInvalid operation - index out of bounds")

    def drawRectangle(self, char, startX, startY, endX, endY, command):
        startX, startY, endX, endY = int(startX), int(startY), int(endX), int(endY)
        if self.inBounds(startX, startY) and self.inBounds(endX, endY):
            for y in range(startX, endX + 1):
                for x in range(startY, endY + 1):
                    if command:  # Erase
                        self.grid[x][y].clear()
                    else:
                        self.grid[x][y].appendleft((char, self.gridID))
            if not command:
                self.gridID += 1
        else:
            self.errorMessage()
    
    def moveRectangle(self, startY, startX, endY, endX, command):
        if self.inBounds(startY, startX) and self.inBounds(endY, endX):
            current = (self.grid[startX][startY][0][0], self.gridID)
            gridID = self.grid[startX][startY][0][1]
            xDif, yDif = 0, 0
            if command:  # Drag and Drop
                xDif = -abs(startX - endX)
                yDif = abs(startY - endY)
                # Validate that the operation is possible at all
                for row in range(len(self.grid)):
                    for col in range(len(self.grid[0])):
                        elem = self.grid[row][col]
                        for index in range(len(elem)):
                            if elem[index][1] == gridID:
                                if not self.inBounds(col + yDif, row + xDif):
                                    self.errorMessage()
                                    return
            # Perform the operation given that it's possible
            for row in range(len(self.grid)):
                for col in range(len(self.grid[0])):
                    elem = self.grid[row][col]
                    for index in range(len(elem)):
                        if elem[index][1] == gridID:
                            del elem[index]
                            if command:  # Drag and Drop
                                self.grid[row + xDif][col + yDif].append(current)
                            else:
                                self.grid[row][col].appendleft(current)
                            break
            if command:
                self.gridID += 1
        else:
            self.errorMessage()


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