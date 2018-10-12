def reconstruct_trip(tickets):
  itinerary = []

  while len(itinerary) != len(tickets) - 1:
    for tripTuple in tickets: 
      arrival = tripTuple[0]
      destination = tripTuple[1]
      if arrival == None and destination not in itinerary: itinerary.insert(0,destination)
      elif destination == None and arrival not in itinerary: itinerary.append(arrival)
      elif destination and arrival in itinerary and destination not in itinerary : itinerary.insert(itinerary.index(arrival)+1, destination)
      elif arrival and destination in itinerary  and arrival not in itinerary : itinerary.insert(itinerary.index(destination), arrival)


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
