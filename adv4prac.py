#Q-Convert a list into a vrticle string  
l=["7","14","21","28","35","42",'49',56,"63","70"]
l[7]=str(l[7])
verticle_string='\n'.join(l)
print(verticle_string)