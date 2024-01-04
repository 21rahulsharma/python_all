def game():
    score=int(input("Enter the score"))
    return score


newscore=game()
with open('hi_score.txt','r') as f:
    r=f.read()
if r=='':
    if int(r)<newscore:
        with open('hi_score.txt','w') as f:
            f.write(str(newscore)) 
elif int(r)<newscore:
    with open('hi_score.txt','w') as f:
        f.write(str(newscore)) 
        print("Congratulations new high score created!!")
