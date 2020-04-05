

# Parameters and Sets ---------
set I;						# Districts
set J;						# Sites

param p{I} >=0;				# Population
param d{I, J} >=0;			# Distance between a site and center of a district
param c{J} >=0;				# Cost of serving population at a district
param f{J} >= 0;			# Fixed cost of building a firehouse at a given site

param B >=0;				# Budget for entire project

# Variables -------------

var bud >=0;			
var y{J} binary;			# Whether or not a firehouse is built at site j
var x{I, J} binary;			# Whether or not a district i is assigned to firehouse j
var z binary; 				# binary for high risk sites

var s{J}	>=0;			# Population that will be served by a particular site J

var D 		>= 0;

# Objective ---------
minimize distance: D;					# Longest distance from centroid


# Constraints ----------

subject to center{i in I}: D >= sum{j in J} d[i,j] * x[i,j];		# The longest distance is the max of every distance

subject to service{i in I}: sum{j in J} x[i, j] = 1; 				# Every district should be assigned to exactly one firehouse

subject to unused{j in J}: sum{i in I}  x[i, j] <= y[j]*card(I);  	# No district should be assigned to an "unused" site

subject to high_risk1: y[1] + y[2] >= 2*z;							# Central area needs either sites 1 and 2 

subject to high_risk2: y[3] + y[4] >= 2*(1 - z);					# Or 3 and 4

subject to pop{j in J}: s[j] = sum{i in I} p[i]*x[i,j];				# The s variable is the sum of the population of a district times whether or not that district is served by a given firehouse 

subject to budget: bud <= B;

subject to Spent: bud = sum{j in J} (c[j] * s[j] + f[j]*y[j]);		# The sum of the fixed cost of building at site j times the service cost at j must be lower than budget

# -----------------


