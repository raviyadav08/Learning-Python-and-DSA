"""
Exercise: Commandline Argument Processing using argparse
Take subject marks as command line arguments
example: 
    python3 cmd.py --physics 60 --chemistry 70 --maths 90
Find average marks for the three subjects using command line input of marks.
"""
import argparse

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--phys",help="Marks of physics")
    parser.add_argument("--chem",help="Marks of chem")
    parser.add_argument("--math",help="Marks of maths")

    args = parser.parse_args()
    print("\n")
    print("Maths: ",args.math)
    print("Physics: ",args.phys)
    print("Chemistry",args.chem)
    print("\nResults : ", round((float(args.phys) + float(args.chem) + float(args.math))/3,2))
    print("\n")



"""
import argparse

if __name__ == '__main__':
    print('\n')
    #Adding 3 optional arguments for entering marks of 3 subjects
    parser = argparse.ArgumentParser()
    parser.add_argument("--physics",help="Enter marks of physics")
    parser.add_argument("--chemistry",help="Enter marks of chemistry")
    parser.add_argument("--maths",help="Enter marks of maths")
    
    #Parsing marks of 3 subjects
    args = parser.parse_args()
    print('Physics:',args.physics)
    print('Chemistry:',args.chemistry)
    print('Maths:',args.maths)

    phys = int(args.physics)
    chem = int(args.chemistry)
    math = int(args.maths)

    # Averaging the 3 marks.
    # Avg = round((phys+chem+math)/3,2)
    # print('Avg of marks: ',Avg,'\n')

    print("Results : ",(
        int(args.physics) + int(args.chemistry) + int(args.maths))/3)     
"""

