skyline = [
            [0,0,0,0,1,0],
            [1,1,1,1,1,0],
            [1,1,1,1,1,1],
            [1,1,1,1,1,1],
            [1,1,1,1,1,1],
            [1,1,1,1,1,1]
          ]

def tallestSkyscraper(input):
    for i in range(len(input)): 
        if 1 in input[i]: return(len(input)- input.index(input[i]))
            
print(tallestSkyscraper(skyline))