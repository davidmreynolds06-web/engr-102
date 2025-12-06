import si_conversion
import cube_shape

side_in_cm = int(input())

surface_area_cm2 = cube_shape.surface_area_cm2(side_in_cm)
surface_area_mm2 = si_conversion.cm2_to_mm2(surface_area_cm2)

print(f"Cube surface area is {surface_area_cm2} cm^2 or {surface_area_mm2} mm^2.")