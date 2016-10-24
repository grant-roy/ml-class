from random import randint

def probability_of_breaking(n):
   clumsy=0.
   # five dishes...need to 'dish' them out randomly
   for i in range(n):

       dishwashers = [0, 0, 0, 0, 0]
       dishes = 5
       while dishes > 0:
           dishwashers[randint(0,4)]+=1
           dishes-=1
       if dishwashers[0] > 3:
           clumsy+=1.

   return clumsy/n
