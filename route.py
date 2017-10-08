import sys
import Queue
segmentfile = "road-segments.txt"
cityfile = "city-gps.txt"
graph = {}
total_distance = 0

with open(segmentfile,"r") as myfile:
    segmentlist = [line.rstrip('\n') for line in myfile]
rsegment = [i.split(" ") for i in segmentlist]

with open(cityfile,"r") as myfile:
    segmentlist = [line.rstrip('\n') for line in myfile]
masterdata_city = [i.split(" ") for i in segmentlist]

# Construction of adjacency list from the road-segments
for city in rsegment:
    if city[0] in graph.keys():
        graph[city[0]][city[1]]=city[2]
        if city[1] not in graph.keys():
            graph[city[1]]={}
            graph[city[1]][city[0]]=city[2]
        else:
            graph[city[1]][city[0]]= city[2]
    else:
        graph[city[0]]={}
        graph[city[0]][city[1]]=city[2]
        if city[1] not in graph.keys():
            graph[city[1]]={}
            graph[city[1]][city[0]]=city[2]
        else:
            graph[city[1]][city[0]]= city[2] 

tgraph = {}
for city in rsegment:
    if city[0] in tgraph.keys():
        tgraph[city[0]][city[1]]=city[3]
        if city[1] not in tgraph.keys():
            tgraph[city[1]]={}
            tgraph[city[1]][city[0]]=city[3]
        else:
            tgraph[city[1]][city[0]]= city[3]
    else:
        tgraph[city[0]]={}
        tgraph[city[0]][city[1]]=city[3]
        if city[1] not in tgraph.keys():
            tgraph[city[1]]={}
            tgraph[city[1]][city[0]]=city[3]
        else:
            tgraph[city[1]][city[0]]= city[3]

def BFS():
    if cost_function == "segment" or cost_function == "distance" or  cost_function == "time":
        BFSqueue = []
        BFSqueue.append((source_city,source_city))
        visited[source_city] = 1
        track = source_city
        while len(BFSqueue)>0:
            current_city,track = BFSqueue.pop(0)
            visited[current_city] = 1
            for reachable_city in graph[current_city]:
                if reachable_city == dest_city:
                    return (track+' '+reachable_city)
                else:
                    if visited[reachable_city]==0:
                        BFSqueue.append((reachable_city,(track+' '+reachable_city)))
        print "Sorry no route found"               
    else:
        print "Please enter valid cost function"

def UCF():

    if cost_function == "segment":
        visited[source_city] = 1
        UCFqueue = Queue.Queue()
        UCFresult = Queue.LifoQueue()
        track = []
        current_city = source_city

        if source_city==dest_city:
            return track.append(source_city)
        UCFqueue.put((0,source_city,source_city))

        while not UCFqueue.empty():
            cost, current_city, track = UCFqueue.get()
            visited[current_city]=1
            if current_city==dest_city:
                return track
            for reachable_city in graph[current_city]:
                if visited[reachable_city] == 0:
                    UCFqueue.put(((int(graph[current_city][reachable_city])+cost),reachable_city,(track+' '+reachable_city)))
        print "Sorry no route found"

    elif cost_function == "distance":
        visited[source_city] = 1
        UCFqueue = Queue.PriorityQueue()
        UCFresult = Queue.LifoQueue()
        track = []
        current_city = source_city

        if source_city==dest_city:
            return track.append(source_city)
        UCFqueue.put((0,source_city,source_city))

        while not UCFqueue.empty():
            cost, current_city, track = UCFqueue.get()
            visited[current_city]=1
            if current_city==dest_city:
                return track
            for reachable_city in graph[current_city]:
                if visited[reachable_city] == 0:
                    UCFqueue.put(((int(graph[current_city][reachable_city])+cost),reachable_city,(track+' '+reachable_city)))
        print "Sorry no route found"

    elif cost_function == "time":
        visited[source_city] = 1
        UCFqueue = Queue.PriorityQueue()
        UCFresult = Queue.LifoQueue()
        track = []
        current_city = source_city

        if source_city==dest_city:
            return track.append(source_city)
        UCFqueue.put((0,source_city,source_city))

        while not UCFqueue.empty():
            total_time, current_city, track = UCFqueue.get()
            visited[current_city]=1
            if current_city==dest_city:
                return track
            for reachable_city in graph[current_city]:
                if visited[reachable_city] == 0:
                    distance = int(graph[current_city][reachable_city])
                    speed =  int(tgraph[current_city][reachable_city])
                    if speed!=0 :
                        time = float(distance)/float(speed)
                        UCFqueue.put(((time+total_time),reachable_city,(track+' '+reachable_city)))
        print "Sorry no route found"

    else:
        print "Kindly enter valid cost function."

def print_path(track):

    path = []
    path = track.split(" ")
    total_distance = 0
    total_time = 0
    time_segment = 0
    distance_segment = 0
    speed_segment = 0
    total_speed = 0
    i=0
    while i<len(path):
        if i!=len(path)-1:
            distance_segment= float(graph[path[i]][path[i+1]])
            speed_segment = float(tgraph[path[i]][path[i+1]])
            if speed_segment!=0:
                time_segment = float(distance_segment / speed_segment)
            total_time += time_segment
            total_distance += distance_segment
        i = i+1
    print total_distance
    print round(total_time,4)
    for city in path:
        for mastercity in masterdata_city:
            if city in mastercity[0]:
                print city

                
#Set the visited to false for every city
#Set the previous city travered to -1 initially.
visited = {}
for city in graph.keys():
    visited[city]= 0
source_city = str(sys.argv[1])
dest_city = str(sys.argv[2])
algorithm = str(sys.argv[3])
cost_function = str(sys.argv[4])
if algorithm == "bfs" :
    track =BFS()
elif algorithm == "uniform":     
    track = UCF()
if(track):
    print_path(track)




