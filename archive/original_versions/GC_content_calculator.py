DNA_sequence = input("Enter the DNA Seq: ").upper()


def GC_content():
    G_content = DNA_sequence.count('G')
    C_content = DNA_sequence.count('C')
    gc = G_content + C_content * 100 / len(DNA_sequence)
    print(gc)
    
    
GC_content()    
    