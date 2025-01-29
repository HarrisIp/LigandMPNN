import string
import numpy as np

def generate_residue_groups(chain_lengths, num_components, symmetry_order):
    import string
    chains = list(string.ascii_uppercase)
    
    if len(chain_lengths) != num_components:
        raise IndexError(f'Number of components does not match the length of chain_lengths')
    
    all_Chain = []
    chain_index = 0
    M = 1
    
 
    for i in range(symmetry_order):
        
        for j in range(num_components):
            chain = []  
            for L in range(chain_lengths[j]):
                residue = f"{chains[chain_index]}{M}"
                chain.append(residue)
                M += 1
            chain_index += 1  
            all_Chain.append(chain)
    output = ''
    for z in range(max(chain_lengths)):  
        line = ''  
        for x in range(num_components):  
            group = ''  
            for y in range(symmetry_order):  
                if z < chain_lengths[x]:  # Ensure we don't go out of bounds for shorter chains
                    extract = all_Chain[x + y * num_components][z]
                    group += extract + ','
            if group:  # Only add non-empty groups to the line
                line += group.rstrip(',') + '|'
        output += line  
    output += output.rstrip('|')
    return output.strip()

def normalize_residue_groups(output):
    groups = output.split('|')
    
    normalized_output = []
    
    for group in groups:
        if group:  # Ensure the group is not empty
            entries = group.split(',')
            normalized_value = 1 / len(entries)
            # Create a new group where each entry is replaced by the normalized value
            normalized_group = ','.join([f"{normalized_value:.2f}"] * len(entries))
            normalized_output.append(normalized_group)
    return '|'.join(normalized_output)
    

print(generate_residue_groups([100, 120, 80], 3, 3))

print(normalize_residue_groups(generate_residue_groups([100, 120, 80], 3, 3)))