import json, urllib.request, sys

event = sys.argv[1]
url="https://api.vexdb.io/v1/get_teams?sku="+event
response = urllib.request.urlopen(url)
eventteams = json.loads(response.read())

print("Teams,# of Comps,Rank: Avg of Last 3,Rank: Avg,Wins: Avg of Last 3,Wins: Avg,losses: Avg of Last 3,losses: Avg,Ties: Avg of Last 3,Ties: Avg,WP: Avg of Last 3,WP: Avg,AP: Avg of Last 3,AP: Avg,SP: Avg of Last 3,SP: Avg,Highest Score: (Last),TRSPs: Last,OPR: Last,DPR: Last,CCWM: Last")
for teamdata in eventteams["result"]:
   team = teamdata["number"] 

   url="https://api.vexdb.io/v1/get_rankings?season=current&team="+team
   response = urllib.request.urlopen(url)
   data = json.loads(response.read())
   totalap = 0
   totalwp = 0
   totalsp = 0
   totalrank = 0
   totalwins = 0
   totallosses = 0
   totalties = 0
   count = 0
   last3ap = 0
   avgap = 0
   avgwp = 0
   avgsp = 0
   avgrank = 0
   last3wp = 0
   last3sp = 0
   last3rank = 0
   last3wins = 0
   last3losses = 0
   last3ties = 0
   lastHighScore = 0
   lastTRSP = 0
   lastOPR = 0
   lastDPR = 0
   lastCCWM = 0
   for result in data["result"]:
      count = count + 1
      totalap = totalap + result["ap"]
      totalwp = totalwp + result["wp"]
      totalsp = totalsp + result["sp"]
      totalrank = totalrank + result["rank"] 
      totalwins = totalwins + result["wins"]
      totallosses = totallosses + result["losses"]
      totalties = totalties + result["ties"]
      if (count == 1):
         lastHighScore = result["max_score"]
         lastTRSP = result["trsp"]
         lastOPR = result["opr"]
         lastDPR = result["dpr"]
         lastCCWM = result["ccwm"]

      if (count == 3):
         last3ap = totalap / count
         last3wp = totalwp / count
         last3sp = totalsp / count
         last3rank = totalrank / count
         last3wins = totalwins / count
         last3losses = totallosses / count
         last3ties = totalties / count

   if (count > 0):
      avgap = totalap/count
      avgwp = totalwp/count
      avgsp = totalsp/count
      avgrank = totalrank/count
      avgwins = totalwins/count
      avglosses = totallosses/count
      avgties = totalties/count

      if (count < 3):
         last3ap=avgap
         last3wp=avgwp         
         last3sp=avgsp
         last3rank=avgrank
         last3wins=avgwins
         last3losses=avglosses
         last3ties=avgties

   print(team+","+str(count)+","+format(last3rank, '.2f')+","+format(avgrank, '.2f')+","+format(last3wins, '.2f')+","+format(avgwins, '.2f')+","+format(last3losses, '.2f')+","+format(avglosses, '.2f')+","+format(last3ties, '.2f')+","+format(avgties, '.2f')+","+format(last3wp, '.2f')+","+format(avgwp, '.2f')+","+format(last3ap, '.2f')+","+format(avgap, '.2f')+","+format(last3sp, '.2f')+","+format(avgsp, '.2f')+","+str(lastHighScore)+","+str(lastTRSP)+","+format(lastOPR,'.2f')+","+format(lastDPR,'.2f')+","+format(lastCCWM,'.2f'))


#To Run
#Open the terminal for your os
#Go to file location
#Type 'python vexap.py competition skew'
#Hit enter to run
#To save to file add '>filename.csv' after skew