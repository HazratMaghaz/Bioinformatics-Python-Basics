
user = (input("Enter your DNA Sequence: ")).upper()

def Dna_counts():
    counts = 0
    for i in user:
      counts += 1

    print(f"\n The total counts is : {counts}")  

def A_count_DNA():
    print( f" \n The 'A' Count is : {user.count('A')}")
    
def T_count_DNA():
    print( f" \n The T count is : {user.count('T')}")
    
def C_count_DNA():
    print( f" \n The C count is : {user.count('C')}")
    
def G_count_DNA():
    print( f" \n The G count is: {user.count('G')}")
    
# def DNA_validation():
#         if user == ['A','T','C','G']:
#             print("Valid DNA!")
#         else:
#             print("Non Valid DNA!")
# def non_valid_DNA():
#     NValid = []
#     # if user != ['A', 'T', 'C','G']:
#     #     print()
#     for i in user:
#         if user != ['A', 'T', 'C','G']:
#             i += 1
            
#     print(f"The Number of Non Valid sequence letter is: {NValid}")
def valid_seq():
    valid_bases = {'A', 'T', 'C', 'G'}
    # Use a set for efficient lookup
    
    # Check if every character in the user string is in the valid_bases set
    if all(base in valid_bases for base in user):
        print("\nValid sequence")
    else:
        print("\nIn valid sequence there")
    # print("Seq is Valid")    

# non_valid_DNA()
# DNA_validation()    


valid_seq()
A_count_DNA()
T_count_DNA()
C_count_DNA()
G_count_DNA()

Dna_counts()
    
    