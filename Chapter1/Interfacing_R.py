import os
from IPython.display import Image
import rpy2.robjects as robjects
import pandas as pd
from rpy2.robjects import pandas2ri
from rpy2.robjects import default_converter
from rpy2.robjects.conversion import localconverter

read_delim = robjects.r('read.delim')
seq_data = read_delim('sequence.index', header=True,
stringsAsFactors=False)
#In R:
# seq.data <- read.delim('sequence.index', header=TRUE,
#stringsAsFactors=FALSE)