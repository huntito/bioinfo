import csv
import operator

""" Welcome Screen """
print (30*'\n')
print "\tThank you for using Hunter\'s Python Project Program v7.4.90!"
print (5*'\n')
print "\t\t Latest update: December - 7 - 2014"
print (24*'\n')

""" Classes and Defs """

""" Colors you can use to change terminal font color """
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
   
def csv_to_list(csv_file, delimiter=','):
    """ 
    Reads in a CSV file and returns the contents as list,
    where every row is stored as a sublist, and each element
    in the sublist represents 1 cell in the table.
    """
    with open(csv_file, 'rU') as csv_con:
        reader = csv.reader(csv_con, delimiter=delimiter)
        return list(reader)
    
def print_csv(csv_content):
    
    """ Prints CSV file to standard output."""
    print (50*'\n')
    print "\n\nHere\'s the data in ",file_to_analyze
    print(50*'-')
    print "GENE\t\t\t FUNCTION (IN PG'S?)"
    print
    for row in csv_content:
        row = [str(e) for e in row]
        print('\t'.join(row))
    print(50*'-')

def sort_hyp_protein(csv_content):
    
    """Prints only hypothetical proteins"""
    print (50*'\n')
    print "\n\nHere\'s a list of the genes making hypothetical proteins in ",file_to_analyze,':'
    print(50*'-')
    print "GENE\t\t\t FUNCTION (IN PG'S?)"
    print
    item = " hypothetical protein"
    for row in csv_content:
        row = [str(e) for e in row]
        if item in row:
            print('\t'.join(row))
    print(50*'-')

def sort_PG_proteins(csv_content):
    
    """Prints only potential plastoglobule-associated proteins"""
    print (50*'\n')
    print "\n\nHere\'s a list of potential PG-associated proteins in ",file_to_analyze,':'
    print(50*'-')
    print "GENE\t\t\t FUNCTION (IN PG'S?)"
    print
    item = "in PGs"
    for row in csv_content:
        if item in str(row):    
            row = [str(e) for e in row]
            print('\t'.join(row))
    print(50*'-')
    
def search_other(csv_content):
    
    """ Prints whatever the user wants to find in the list of proteins and genes """
    print (5*'\n')
    item = raw_input("What proteins or genes would you like me to search for? ")
    item = item.strip()
    print (50*'\n')
    print "Here's a list of things with","\"",item,"\"","in",file_to_analyze,':'
    print(50*'-')
    print "GENE\t\t\t FUNCTION (IN PG'S?)"
    print
    for row in csv_content:
        if item in str(row):    
            row = [str(e) for e in row]
            print('\t'.join(row))
    print(50*'-')

""" Main Program Starts Here """

file_to_analyze = raw_input('What is the name of the file you want to analyze? (Please use .csv extensions only) ')

csv_cont = csv_to_list(file_to_analyze)
print_csv(csv_cont)

while True:
    onOff = 0
    if onOff == 0:
        print (5*'\n')
        print "How would you like to sort the original data?\n"
        print "[1] Hypothetical Proteins"
        print "[2] Potential Plastoglobule-Associated Proteins (in PGs)"
        print "[3] Other (User Input) Proteins"
        print "[4] Original Data (no sorting)"
        print "[5] BLAST"
        print "[6] Quit"
        print
        
        myAnswer = raw_input("Please enter your choice now: ")
        
        if myAnswer == "1":
            print "\n"
            sort_hyp_protein(csv_cont)
                    
        elif myAnswer == "2":
            print "\n"
            sort_PG_proteins(csv_cont)
            
        elif myAnswer == "3":
            print "\n"
            search_other(csv_cont)
            
        elif myAnswer == "4":
            print "\n"
            print_csv(csv_cont)
            
        elif myAnswer == "5":
            print (50*'\n')
            print "We're working on this! Please check again when v7.4.91 comes out."
            print
            
        elif myAnswer == "6":
            print (50*'\n')
            print "\tThank you for using Hunter\'s Python Project Program v7.4.90!"
            print
            print "\t\t -Goodbye :)"
            print (20*'\n')
            break