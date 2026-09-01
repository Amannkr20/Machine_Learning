from myfile import Ques

question=["National Bird of India\n(a)Peacock, \n(b)Sparrow, \n(c)Eagle\n",
"Largest Planet in the Solar System\n(a)Earth, \n(b)Jupiter, \n(c)Mars\n",
"What is the capital of India? \n(a)New Delhi, \n(b)Mumbai, \n(c)Kolkata\n",
"What is the largest desert in the world? \n(a)Sahara Desert, \n(b)Gobi Desert, \n(c)Kalahari Desert\n",
"Speed of sound in air is approximately\n(a)343 m/s, \n(b)300 m/s, \n(c)400 m/s \n",
"What is the capital of USA? \n(a)Washington D.C., \n(b)New York, \n(c)Los Angeles\n",  
"How many continents are there in the world? \n(a)5, \n(b)6, \n(c)7\n",
"What is the largest ocean in the world? \n(a)Atlantic Ocean, \n(b)Indian Ocean, \n(c)Pacific Ocean\n",
"What is the capital of France? \n(a)Berlin, \n(b)Madrid, \n(c)Paris\n"]
for i in question:
    print(i)
 
# q=Ques("dsfs","a")
ans=[Ques(question[0], "a"),
     Ques(question[1], "b"), 
     Ques(question[2], "a"), 
     Ques(question[3], "a"), 
     Ques(question[4], "a"), 
     Ques(question[5], "a"), 
     Ques(question[6], "c"), 
     Ques(question[7], "c"), 
     Ques(question[8], "c")]

for i in ans:
    ans=input(i.q)
    if ans==i.a:
        score=score+1

print("Total score is: ",score)

