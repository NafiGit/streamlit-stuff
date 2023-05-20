import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

# image = Image.open('dna_logo.png')

# st.image(image)

st.write("""

# DNA Neucleotide Webapp

This app counts the nucleotide composition of query DNA

""")
         

st.header('Enter DNA sequence: ')
sequence_input = """>DNA Query\n
AGCTGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATC\nAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTA\nCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATC\nTATATATATATATATATATATATATATATATATATATATATATATATATATATATATATAT\nGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCG\n
"""

sequence = st.text_area("Sequence Input", sequence_input, height=250)
sequence = sequence.splitlines()
sequence = sequence[1:] # Skips the sequence name (first line)
sequence = ''.join(sequence)
sequence = ''.join(sequence)



st.write('***')

st.header('Input (DNA Query) ')
sequence

st.header('Output (Neuclotide Count) ')

st.subheader('1. Print Dictionary')

def DNA_nucleotide_count(seq):
    counts = dict([
        ("A", seq.count('A')),
        ("C", seq.count('C')),
        ("T", seq.count('T')),
        ("G", seq.count('G'))
    ])
    return counts
    
X = DNA_nucleotide_count(sequence)

X

X_label = list(X)
X_values = list(X.values())


st.subheader('2. Print Text')

st.write(f"There are {X['A']} adenine (A)")
st.write(f"There are {X['C']} cytosine (C) ")
st.write(f"There are {X['T']} thymine (T) ")
st.write(f"There are {X['G']} guanine (G) ")

st.subheader("3. Display Dataframe")

df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0: 'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns = {'index': 'nucleotide'})
st.write(df)

# using altair
st.subheader("4. Display Bar Chart")
p = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count'
)

p = p.properties(
    width = alt.Step(80) # controls width of bar
)

st.write(p)

