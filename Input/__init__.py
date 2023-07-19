s = input("Enter your input: ")
print ("Received input is:", s)
n=int(input("Enter your number: "))
grid = [(input()) for _ in range(n)] # get inputs in to a list ["..X", "...", "XX."]

grid1 = [list(input()) for _ in range(n)]# got inputs as below
#..X
#...
#XX.
print(grid1)#[['.', '.', 'X'], ['.', '.', '.'], ['X', 'X', '.']]

startX, startY, goalX, goalY = map(int, input().split()) # get inputs as 0 0 0 2


lst = [ ] 
n = int(input("Enter number of elements : ")) 
  
for i in range(0, n): 
    ele = [input(), int(input())] 
    lst.append(ele) 
      
print(lst)  #[['12', 13], ['23', 21]]


T=int(input()) # no of test cases
lst = [ ]  
for i in range(0, T): 
    lst.append(int(input())) #[23, 34]
      
print(lst)
