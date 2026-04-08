#import shapes
from shapes import *

while True:
    print("\n--- Select Shape ---")
    print("1. Cube")
    print("2. Cuboid")
    print("3. Cylinder")
    print("4. Cone")
    print("5. Sphere")
    print("6. Hemisphere")
    print("7. Exit")

    choice = int(input("Enter choice: "))

    if choice == 7:
        break

    print("\n--- Select Operation ---")
    print("1. Curved Surface Area (CSA)")
    print("2. Total Surface Area (TSA)")
    print("3. Volume")

    op = int(input("Enter operation: "))

    # 🔹 Cube
    if choice == 1:
        a = float(input("Enter side: "))
        if op == 1:
            print("CSA =",cube_csa(a))
        elif op == 2:
            print("TSA =", cube_tsa(a))
        elif op == 3:
            print("Volume =", cube_volume(a))

    # 🔹 Cuboid
    elif choice == 2:
        l = float(input("Enter length: "))
        b = float(input("Enter breadth: "))
        h = float(input("Enter height: "))
        if op == 1:
            print("CSA =", cuboid_csa(l, b, h))
        elif op == 2:
            print("TSA =", cuboid_tsa(l, b, h))
        elif op == 3:
            print("Volume =", cuboid_volume(l, b, h))

    # 🔹 Cylinder
    elif choice == 3:
        r = float(input("Enter radius: "))
        h = float(input("Enter height: "))
        if op == 1:
            print("CSA =", cylinder_csa(r, h))
        elif op == 2:
            print("TSA =", cylinder_tsa(r, h))
        elif op == 3:
            print("Volume =", cylinder_volume(r, h))

    # 🔹 Cone
    elif choice == 4:
        r = float(input("Enter radius: "))
        l = float(input("Enter slant height: "))
        h = float(input("Enter height: "))
        if op == 1:
            print("CSA =", cone_csa(r, l))
        elif op == 2:
            print("TSA =", cone_tsa(r, l))
        elif op == 3:
            print("Volume =", cone_volume(r, h))

    # 🔹 Sphere
    elif choice == 5:
        r = float(input("Enter radius: "))
        if op == 1:
            print("CSA =", sphere_csa(r))
        elif op == 2:
            print("TSA =", sphere_tsa(r))
        elif op == 3:
            print("Volume =", sphere_volume(r))

    # 🔹 Hemisphere
    elif choice == 6:
        r = float(input("Enter radius: "))
        if op == 1:
            print("CSA =", hemisphere_csa(r))
        elif op == 2:
            print("TSA =", hemisphere_tsa(r))
        elif op == 3:
            print("Volume =", hemisphere_volume(r))

    else:
        print("Invalid choice!")


# 