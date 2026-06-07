dna = input("Please enter short dna sequence you want to tranlate: ").upper()

seq = ""
def dna_converter():
    global seq
    for i in dna:
        if i == "A":
            seq += "T"
        elif i == "C":
            seq += "G"
        elif i == "T":
            seq += "A"
        elif i == "G":
            seq += "C"
        else:
            print("The Sequence has error please try with valid sequence there")
                        
   


def virtualized_dna():
    print(f"Your DNA Sequence: {dna}")
    print(f"\n The complement DNA are : {seq}")

dna_converter() 
virtualized_dna()
