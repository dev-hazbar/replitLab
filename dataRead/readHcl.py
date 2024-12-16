import hcl

# Lee el archivo HCL
with open('data.hcl', 'r') as f:
    hcl_data = hcl.load(f)

print(hcl_data)
