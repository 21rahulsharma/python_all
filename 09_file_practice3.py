print("Hello \n User ")
for i in range(2,4):
    with open(f"Multiplication_table_of_{i}",'w')as f:
        for j in range(1,11):
            f.write(f"{i} * {j}= {i*j} \n")
            
        
        
        
        