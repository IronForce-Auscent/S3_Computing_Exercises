'''
An online retailer sells two products: widgets and gizmos. Each widget weighs 75
grams. Each gizmo weighs 112 grams. Write a program that reads the number of
widgets and the number of gizmos in an order from the user. Then your program
should compute and display the total weight of the order
'''
def exercise_8():
  widget = 75
  gizmo = 112

  widget_count = int(input("Input number of widgets ordered: "))
  gizmo_count = int(input("Input number of gizmos ordered: "))

  total_mass = (widget_count * widget) + (gizmo_count * gizmo)
  print(total_mass)