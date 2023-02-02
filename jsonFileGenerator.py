import json
import random

data = [[i for i in range(1000)], 
        [i for i in range(2000)], 
        [i for i in range(3000)],  
        [i for i in range(4000)],   
        [i for i in range(5000)],   
        [i for i in range(6000)], 
        [i for i in range(7000)], 
        [i for i in range(8000)],  
        [i for i in range(9000)],   
        [i for i in range(10000)],   
        ]

with open("ordered.json", "w") as InF:
    json.dump(data, InF)