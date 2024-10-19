runcount = 300 #unique name for run

# set the base as individual or group of bases
seat = "CA"
# CA or FO

# group would be separated by comma like this: baseList = ['IAH','IAD','DEN']
# individual would be baseList = ['IAH']
baseList = ['IAH']

# set the max number of people that can bid min credit
# contractually limited to 10% of line holders for a given base and position
# set to 0 if number of min credit bidders will not be restricted
maxMinCredit = 0

# add a prefix to the run
# this can be useful if you want to label runs with "test"
# if it's empty between the quotes then nothing will be added
prefix = "A"

# add a suffix to the end of the name of the run
# this is useful if you already did a set of runs so this will be added to the end to make it unique
# if it's empty between the quotes then nothing will be added
# not really necessary since timestamps are included
suffix = "LX"

# set the max stack height for unstacking on line holders
# maximimum stack height must be at least 6% of regular line holders
# for holidays, contractually limited to 50% of regular pilots (does not specify line holders so I interpret to mean bidding pilots)
# set to 0 if line holders will not be unstacked on
unstackLineHolders = 20
maxPasses = 20
pointOrDayStack = "day" #set this to either "point" or "day"

# set the max number of iterations
# Our default is set to 2,000,000. Help file says it should be between 5,000,000 and 10,000,000
two_mil = 2000000
five_mil = 5000000
ten_mil = 10000000
all_nines = 99999999
# maxIterations = 2000000
# maxIterations = 5000000
maxIterations = 10000000
# maxIterations = 99999999

# specify which server and credentials to use
# using the production server is normal and would be set to True
productionServer = True

# check each base to get a baseline
# can be set to "All", "None", "CA", or "FO"
# NOTE: if All is selected, the FO runs will possibly be based off of runs prior to the latest captain runs being complete
baselineTest = "None"

# set the testMode to True or False.
# If set to True, the program will go through the motions, but not actually start the run
testMode = True

# print detailed messages
verbose = True

# set the constants for fixed windows
minFloor = 77
minCeiling = 87
normalFloor = 83
normalCeiling = 93
maxFloor = 90
maxCeiling = 100