# Print out all the state names from the csv
# Showing the "functional" style

f = open('2012_US_election_state.csv', 'r')
print "Opened file:"

all_lines = f.readlines()

# this is a really clever way to do things!
# this is another useful comment
names = [line.split(",")[1] for line in all_lines]

for name in names:
    print name

print "done ("+str(len(all_lines))+" lines)"