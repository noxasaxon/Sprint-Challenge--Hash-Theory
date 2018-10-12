def reconstruct_trip(tickets):
  itinerary = []

#solution without hash table
  # while len(itinerary) != len(tickets) - 1:
  #   for tripTuple in tickets: 
  #     arrival = tripTuple[0]
  #     destination = tripTuple[1]
  #     if arrival == None and destination not in itinerary: itinerary.insert(0,destination)
  #     elif destination == None and arrival not in itinerary: itinerary.append(arrival)
  #     elif destination and arrival in itinerary and destination not in itinerary : itinerary.insert(itinerary.index(arrival)+1, destination)
  #     elif arrival and destination in itinerary  and arrival not in itinerary : itinerary.insert(itinerary.index(destination), arrival)

  
  #create hash table
  ht = {}

  for tripTuple in tickets:
    arrival = tripTuple[0]
    destination = tripTuple[1]
    if arrival == None: itinerary.insert(0, destination)
    # elif destination == None: itinerary.append(arrival)
    else:
      ht[arrival] = destination
  
  #create itinerary
  arrival = 1 #default start
  destination = itinerary[0]
  while arrival != None:
    arrival = ht[destination]
    
    if arrival: 
      itinerary.append(arrival)
      destination = ht[arrival]
      if destination: itinerary.append(destination)


  return itinerary

if __name__ == '__main__':
  # You can write code here to test your implementation using the Python repl
  print(reconstruct_trip([
  ('PIT', 'ORD'),
  ('XNA', 'CID'),
  ('SFO', 'BHM'),
  ('FLG', 'XNA'),
  (None, 'LAX'), 
  ('LAX', 'SFO'),
  ('CID', 'SLC'),
  ('ORD', None),
  ('SLC', 'PIT'),
  ('BHM', 'FLG'),
]))
