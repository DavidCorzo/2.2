from operator import is_
import numpy as np

def is_ortogonal(v1,v2,sv1,sv2):
    mult = np.dot(v2, np.transpose(v1))
    if(mult[0][0]==0):
        print(f"{sv1} y {sv2} son ortogonales")
    else:
        print(f"{sv1} y {sv2} no son ortogonales")

def c_ortogonal(v):
    print(v1/np.linalg.norm(v1))

print(f"{'-'*30}a){'-'*30}")
v1 = [[1,1,1]]
v2 = [[1,-1,0]]
v3 = [[1,1,-2]]
print("\t1.")
#Verificando si son ortonormales
is_ortogonal(v1,v2,"v1","v2")
is_ortogonal(v1,v3,"v1","v3")
is_ortogonal(v2,v3,"v2","v3")
#Generando conjunto  ortonormal
print("\t2.")
c_ortogonal(v1)
c_ortogonal(v2)
c_ortogonal(v3)

print(f"{'-'*30}b){'-'*30}")
v1 = [[1,1,-1,-1]]
v2 = [[1,1,1,1]]
v3 = [[1,-1,0,0]]
v4 = [[0,0,-1,1]]
print("\t1.")
#Verificando si son ortonormales
is_ortogonal(v1,v2,"v1","v2")
is_ortogonal(v1,v3,"v1","v3")
is_ortogonal(v1,v4,"v1","v4")
is_ortogonal(v2,v3,"v2","v3")
is_ortogonal(v2,v4,"v2","v4")
is_ortogonal(v3,v4,"v3","v4")
#Generando conjunto  ortonormal
print("\t2.")
c_ortogonal(v1)
c_ortogonal(v2)
c_ortogonal(v3)
c_ortogonal(v4)
