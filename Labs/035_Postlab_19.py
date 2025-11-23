def z_transform_unit_step(z):
    result = 1 / (1 - 1/z)
    print(f"Z-transform of unit step at z={z}: {result}")
    return result

z_transform_unit_step(7)

#Task -2 
import numpy as np
def system_stability(poles):
    if all(abs(p) < 1 for p in poles):
       print("System is: Stable")
    else:
        print("System is: Unstable")

poles = np.array([0.6, 0.4])
system_stability(poles)        
