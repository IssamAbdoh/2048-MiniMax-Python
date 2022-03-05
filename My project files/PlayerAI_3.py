from random import randint
from BaseAI_3 import BaseAI
import math
from ComputerAI_3 import ComputerAI

defaultProbability = 0.9

"""
3.10.0
python
started 30/01/2022
finished 01/02/2022

I will make it a maximization problem ,
The more the heuristic value , the better the state is

this is why difference_between_adjacent_tiles function returns a negative value
"""

mx = 0

class PlayerAI(BaseAI):
    def getMove(self, grid):
        return self.minimax(grid,-math.inf,math.inf,6)

    def isEqual(self,grid1,grid2):
        size = grid1.size
        for i in range(size):
            for j in range(size):
                if grid1.getCellValue((i,j)) != grid2.getCellValue((i,j)):
                    return False

        return True

    def minimax(self,grid,alpha,beta,max_depth=8):
        next_grid ,_ = self.maximize(grid,alpha,beta,max_depth)
        moves = grid.getAvailableMoves()

        clones = [0,0,0,0]
        for index,move in enumerate(moves):
            clones[index] = grid.clone()
            clones[index].move(move)
            if self.isEqual(next_grid,clones[index])==True:
                return move

    def minimize(self, grid,alpha,beta,depth):
        if depth <=0 or not grid.canMove():
            return None , self.evaluate(grid)

        minChild , minUtility = None,math.inf

        for child in self.computer_children(grid):

            _ , utility = self.maximize(child,alpha,beta,depth -1)
            if utility < minUtility:
                minChild,minUtility = child,utility

            if minUtility <=alpha:
                break
                
            if minUtility < beta:
                beta = minUtility

        return minChild,minUtility

    def maximize(self, grid,alpha,beta,depth):
        if depth <=0 or not grid.canMove():
            return None , self.evaluate(grid)

        maxChild , maxUtility = None, - math.inf

        for child in self.optimized_children(grid):

            _ , utility = self.minimize(child,alpha,beta,depth -1)
            if utility > maxUtility:
                maxChild,maxUtility = child,utility

            if maxUtility >=beta:
                break
                
            if maxUtility > alpha:
                alpha = maxUtility

        return maxChild,maxUtility

    def optimized_children(self, grid):
        available_Moves = grid.getAvailableMoves()
        """
        vertical_current = self.potential_for_merging_similar_tiles_vertically(grid)
        horizontal_current = self.potential_for_merging_similar_tiles_horizontally(grid)

        chosen = []
        #chosen = available_Moves
        
        if vertical_current > horizontal_current:
            chosen = list(filter(lambda x: x<2, available_Moves))
        else:
            chosen = list(filter(lambda x: x>1, available_Moves))
        
        if len(chosen)== 0:
            chosen = available_Moves
        """
        chosen = available_Moves

        children = []
        clones = [0,0,0,0]#دائما اقصى عدد للأولاد هو 4
        for index,move in enumerate(chosen):
            clones[index] = grid.clone()
            clones[index].move(move)
            children.append(clones[index])

        children = sorted(children, key=lambda child: self.evaluate(child),reverse=True)
            
        return children

    def computer_children(self, grid):
        max_number_of_children = 1
        i = 0

        clones = [0] * max_number_of_children
        while max_number_of_children >i:
            clones[i] = grid.clone()
            move = ComputerAI.getMove(None,clones[i])
            clones[i].setCellValue(move, self.getNewTileValue())
            i+=1

        children = sorted(clones, key=lambda child: self.evaluate(child),reverse=False)

        return children

    def getNewTileValue(self):#2 or 4
        possibleNewTiles = [2,4]
        if randint(0,99) < 100 * defaultProbability:
            return possibleNewTiles[0]
        else:
            return possibleNewTiles[1]

    def evaluate(self, grid):
        evalation = 0
        #evalation += (self.potential_for_merging_similar_tiles_vertically(grid)/4)*100 * 1 * 1.5
        #evalation += (self.potential_for_merging_similar_tiles_horizontally(grid)/4)*100 * 1 * 1.5
        evalation += (self.is_win(grid)/1) * 100 * 52
        evalation += (self.is_lost(grid)/1) * 100 * 26
        evalation += (self.number_of_empty_tiles(grid)/15)*100 *2.7 * 1.5
        evalation += (self.difference_between_adjacent_tiles(grid)/24528) * 100 * 1 * 1.5
        evalation += (math.log(self.max_tile(grid),2)/11)*100 *1 * 1.5
        evalation += (self.monotonicity(grid)/33)*100 * 1 * 1.5
        evalation += ((self.potential_for_merging_similar_tiles_horizontally(grid)+self.potential_for_merging_similar_tiles_vertically(grid))/8)*100 * 1 * 1.5
        evalation += (self.sum_of_values(grid)/(2124.2608695652175))*100 * 1

        return evalation

    #the absolute value of tiles
    def sum_of_values(self, grid):#large sum is good , because it has a better chance to get a higher tile
        s = 0
        for i in range(grid.size):
            for j in range(grid.size):
                value = grid.getCellValue((i,j))
                if value not in (None,0):
                    s+=value

        return s

    #the difference in value between adjacent tiles
    def difference_between_adjacent_tiles(self, grid):#the less the difference , the better
        """
        The worst case that I considered while calculating the maximum value of this function is:
        2     1024  2     1024
        1024  2     1024  2
        2     1024  2     1024
        1024  2     1024  2

        the difference was =  24528
        """
        difference = 0

        for i in range(grid.size):
            for j in range(grid.size):
                if grid.getCellValue((i-1,j)) not in (None,0):#current and up
                    difference+=abs(grid.getCellValue((i-1,j)) - grid.getCellValue((i,j)))

                if grid.getCellValue((i+1,j)) not in (None,0):#current and down
                    difference+=abs(grid.getCellValue((i+1,j)) - grid.getCellValue((i,j)))

                if grid.getCellValue((i,j+1)) not in (None,0):#current and right
                    difference+=abs(grid.getCellValue((i,j+1)) - grid.getCellValue((i,j)))

                if grid.getCellValue((i,j-1)) not in (None,0):#current and left
                    difference+=abs(grid.getCellValue((i,j-1)) - grid.getCellValue((i,j)))

        return -difference//2#because we add the same value twice for each tile

    def potential_for_merging_similar_tiles_vertically(self, grid):#The more the better
        #columns = [[],[],[],[]]
        columns = [[] for i in range(grid.size)]
        for i in range(grid.size):
            for j in range(grid.size):
                if grid.getCellValue((j,i)) not in (None,0):
                    columns[i].append(grid.getCellValue((j,i)))

        ans = 0
        for column in columns:
            for i in range(len(column)-1):
                if column[i] == column[i+1]:
                    ans+=1
                    break

        return ans

    def potential_for_merging_similar_tiles_horizontally(self, grid):#The more the better
        #rows = [[],[],[],[]]
        rows = [[] for i in range(grid.size)]
        for i in range(grid.size):
            for j in range(grid.size):
                if grid.getCellValue((i,j)) not in (None,0):
                    rows[i].append(grid.getCellValue((i,j)))

        ans = 0
        for row in rows:
            for i in range(len(row)-1):
                if row[i] == row[i+1]:
                    ans+=1
                    break

        return ans

    def number_of_empty_tiles(self, grid):#the more , the better
        return len(grid.getAvailableCells())

    def is_win(self, grid):#the more the better
        if grid.getMaxTile() >= 2048:
            return 1
        return 0

    def max_tile(self, grid):#The more the better
        return grid.getMaxTile()

    def is_lost(self, grid):#The less the better
        if (len(grid.getAvailableCells())==0):
            return -1
        return 0

    #measures how monotonic the grid is. This means the values of the tiles are strictly increasing
    #or decreasing in both the left/right and up/down directions
    def monotonicity(self, grid):#The more the better
        #scores for all four directions
        totals = [0,0,0,0]

        #up/down direction
        for x in range(len(totals)):
            current = 0
            nextt = current + 1
            while nextt < len(totals):
                while nextt<len(totals) and grid.getCellValue((x,nextt))==0:
                    nextt+=1
                if nextt>=len(totals):
                    nextt-=1
                #min = a if a < b else b
                current_value  = math.log(grid.getCellValue((x,current)),2) if  grid.getCellValue((x,current))!=0 else 0
                next_value = math.log(grid.getCellValue((x,nextt)),2) if  grid.getCellValue((x,nextt))!=0 else 0

                if current_value > next_value:
                    totals[0]+=next_value-current_value
                elif next_value > current_value:
                    totals[1]+=current_value-next_value
                current = nextt
                nextt+=1

        #left/right direction
        for y in range(len(totals)):
            current = 0
            nextt = current + 1
            while nextt < len(totals):
                while nextt<len(totals) and grid.getCellValue((nextt,y))==0:
                    nextt+=1
                if nextt>=len(totals):
                    nextt-=1
                #min = a if a < b else b
                current_value  = math.log(grid.getCellValue((current,y)),2) if  grid.getCellValue((current,y))!=0 else 0
                next_value = math.log(grid.getCellValue((nextt,y)),2) if  grid.getCellValue((nextt,y))!=0 else 0

                if current_value > next_value:
                    totals[2]+=next_value-current_value
                elif next_value > current_value:
                    totals[3]+=current_value-next_value
                current = nextt
                nextt+=1

        return max(totals[0],totals[1]) + max(totals[2],totals[3])
