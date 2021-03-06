"# 2048-MiniMax-Python" 

2048 Game using MiniMax in Python

Week 4 Project: Adversarial Search and Games | Week 4 Project: Adversarial Search and Games | CSMM.101x Courseware | edX

###########################################################################################################

I have ran my algorithm 25 times , and the results were as follows :

It reached those maximum tiles

512 , 7 times 
1024 , 13 times
2048 , 5 times

the summation was = 27136
and the average was = 1085.44

and as it was stated in the project , any avarage of 25 running times should be 
between 1024 <= avg <= 2048
and mine satisfies this condition

the accuracy of my algorithm is 20%
**every 5 times , one of them is guranteed to reach 2048

###########################################################################################################

The Heuristics :

evalation += (self.is_win(grid)/1) * 100 * 52

evalation += (self.is_lost(grid)/1) * 100 * 26

evalation += (self.number_of_empty_tiles(grid)/15)*100 *2.7 * 1.5

evalation += (self.difference_between_adjacent_tiles(grid)/24528) * 100 * 1 * 1.5

evalation += (math.log(self.max_tile(grid),2)/11)*100 *1 * 1.5

evalation += (self.monotonicity(grid)/33)*100 * 1 * 1.5

evalation += ((self.potential_for_merging_similar_tiles_horizontally(grid)+self.potential_for_merging_similar_tiles_vertically(grid))/8)*100 * 1 * 1.5

evalation += (self.sum_of_values(grid)/(2124.2608695652175))*100 * 1



** monotonicity
measures how monotonic the grid is. This means the values of the tiles are strictly increasing , or decreasing in both the left / right and up / down directions

if the algorithm has stopped working , decrease the maximum depth that is located in PlayerAI_3.py 
    def getMove(self, grid):
        return self.minimax(grid,-math.inf,math.inf,6) # <---

keep decreasing 6 by 1 until the algorithm work properly

###########################################################################################################

Here are some screenshots of the performance of my code :

![](https://github.com/IssamAbdoh/2048-MiniMax-Python/blob/main/My%20project%20files/Notes/Screenshot%20(794).png)



![](https://github.com/IssamAbdoh/2048-MiniMax-Python/blob/main/My%20project%20files/Notes/Screenshot%20(795).png)

###########################################################################################################

![](https://github.com/IssamAbdoh/2048-MiniMax-Python/blob/main/My%20project%20files/Notes/Screenshot%20(789).png)

###########################################################################################################

![](https://github.com/IssamAbdoh/2048-MiniMax-Python/blob/main/My%20project%20files/Notes/Screenshot%20(790).png)

###########################################################################################################

![](https://github.com/IssamAbdoh/2048-MiniMax-Python/blob/main/My%20project%20files/Notes/Screenshot%20(791).png)

###########################################################################################################

![](https://github.com/IssamAbdoh/2048-MiniMax-Python/blob/main/My%20project%20files/Notes/Screenshot%20(792).png)

###########################################################################################################

![](https://github.com/IssamAbdoh/2048-MiniMax-Python/blob/main/My%20project%20files/Notes/Screenshot%20(793).png)

###########################################################################################################
