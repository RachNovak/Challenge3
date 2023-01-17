#File 
import os
import csv

pollfile = os.path.join('Resources','election_data.csv')

#open and read the file
with open(pollfile) as csvfile:
    polldata=csv.reader(csvfile,delimiter=',')
    csv_header = next(polldata)
#print(csv_header)

    #Start list of variables
    candidates=[] #name of candidates
    totalvotes=[] #total votes per candidate
    ballotid=[] #'ballot ID' column based on headers
    counties=[] #'counties' column based on headers
    candidatevotes=[]#'candidates' column based on headers
    candidatepercent=[] 
    results=[]   
    
    #Start conditions
    numofvotes=0 #total number of votes
    winnervotes=0 #winners total 
    loservotes=0 #losers total
    loop1=0 # firstloop search
    loop2=0 #secondloop search
    loop3=0 #thirdloop search
    loop4=0 #fourth loop search
    
    #read each line and assign data to correct location.
    for row in polldata:
        ballotids=row[0] #column 0 aissnged to 'ballot id'
        ballotid.append(ballotids)
        
        countynames=row[1] #column 1 assinged to 'counties'
        counties.append(countynames) # add next line
        
        candidatevote =row[2] #column 2 assigned to 'candidate votes'
        candidatevotes.append(candidatevote) # add next line
    
    #The total number of votes cast
    votecount = len(ballotid)
    #print(votecount)

candidates.append(candidatevotes[0])
#Loop through and find a complete list of candidates who received votes
for loop1 in range (votecount-1):
    if candidatevotes[loop1+1] != candidatevotes[loop1] and candidatevotes[loop1+1] not in candidates:
        candidates.append(candidatevotes[loop1+1])

votedfor=len(candidates)
#print(votedfor)

#second loop through to find candidates & matching total votes
for loop2 in range(votedfor):
    totalvotes.append(candidatevotes.count(candidates[loop2])) #count totall
#print(candidates)
#print(totalvotes)

#third loop now we can find the percentage per candidate
loservotes=votecount

for loop3 in range(votedfor):
    candidatepercent.append(f'{round((totalvotes[loop3]/votecount*100),3)}%')#find the percentage of votes that each candidate won [[votes per name  / votecount]]
    if totalvotes[loop3]>winnervotes: #candidate with highest count of votes cast
        winner=candidates[loop3]
        winnervotes=totalvotes[loop3]
    if totalvotes[loop3]<loservotes: #candidate with lowest count of votes cast
        loser=candidates[loop3]
        loservotes=totalvotes[loop3]
#print(candidatepercent)

#fourth loop to display voting results
# #The winner of the election based on popular vote.

for loop4 in range(votedfor):
    results.append(f'{candidates[loop4]} {candidatepercent[loop4]} ({totalvotes[loop4]})')

resultsreport='\n'.join(results)

analysis=f'\
Election Results\n\
----------------------------\n\
Total Votes: {votecount}\n\
----------------------------\n\
{resultsreport}\n\
----------------------------\n\
Winner: {winner}\n\
----------------------------\n'
print(analysis)


file2=open("pypoll.txt","w")
file2.writelines(analysis)
file2.close()