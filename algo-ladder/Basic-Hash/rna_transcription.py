# Given a DNA strand, return its RNA complement (per RNA transcription).

# Both DNA and RNA strands are a sequence of nucleotides. Here we're representing the sequences with single-letter characters (e.g. a sample strand may look like: "AGCA".)

# Given a string representing a DNA strand, provide its transcribed RNA strand, according to the following pattern:

# G becomes C
# C becomes G
# T becomes A
# A becomes U

# So based on all this, here's a sample input/output:

# Input: 'ACGTGGTCTTAA'
# Output: 'UGCACCAGAAUU'

def rna_transcribe(string):
    rna_hash = {
        "A": "U",
        "T": "A",
        "C": "G",
        "G": "C"
    }
    rna_string = ""
    for char in string:
        rna_string += rna_hash[char]
    return rna_string


print(rna_transcribe('ACGTGGTCTTAA'))
