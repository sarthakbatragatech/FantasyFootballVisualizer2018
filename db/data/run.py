from collectData import collect
from cleanData import clean
from plotData import plot
import sys

position = str(sys.argv[1])

collect(position)
clean(position)
plot(position)
print("Done!")
