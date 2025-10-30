# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name:  Deep Patel
#        Chris Voelkel
#        Karl Nolte
#        David Reynolds
# Section: 412
# Assignment: Lab Topic 10 box of chocolates
# Date: 29 October 2025
def make_boxes(chocolates):
    import random
    
    boxes = []
    used_truffles = []
    
    # Make 25 boxes
    box_number = 0
    while box_number < 25:
        box = []
        
        # Try to fill one box with 4 truffles
        tries = 0
        while len(box) < 4:
            tries = tries + 1
            if tries > 1000:
                # Start over if stuck
                boxes = []
                used_truffles = []
                box_number = 0
                box = []
                tries = 0
            
            # Pick a random truffle
            truffle_id = random.randint(1, 100)
            
            # Skip if already used
            if truffle_id in used_truffles:
                continue
            
            # Get truffle info
            chocolate_type = chocolates[truffle_id][0]
            shape = chocolates[truffle_id][1]
            filling = chocolates[truffle_id][2]
            topping = chocolates[truffle_id][3]
            
            # Check if truffle can go in box
            can_add = True
            
            # Check against each truffle already in box
            i = 0
            while i < len(box):
                other_id = box[i]
                other_type = chocolates[other_id][0]
                other_shape = chocolates[other_id][1]
                other_filling = chocolates[other_id][2]
                other_topping = chocolates[other_id][3]
                
                # Check if exact duplicate
                if chocolate_type == other_type and shape == other_shape and filling == other_filling and topping == other_topping:
                    can_add = False
                
                # Check caramel and vanilla rule
                if filling == "caramel" and other_filling == "vanilla":
                    can_add = False
                if filling == "vanilla" and other_filling == "caramel":
                    can_add = False
                
                # Check nuts and sprinkles rule
                if topping == "nuts" and other_topping == "sprinkles":
                    can_add = False
                if topping == "sprinkles" and other_topping == "nuts":
                    can_add = False
                
                # Check rectangle and square rule
                if shape == "rectangle" and other_shape == "square":
                    can_add = False
                if shape == "square" and other_shape == "rectangle":
                    can_add = False
                
                i = i + 1
            
            # Add truffle to box if it's okay
            if can_add == True:
                box.append(truffle_id)
        
        # Check dark chocolate rule
        dark_count = 0
        j = 0
        while j < len(box):
            if chocolates[box[j]][0] == "dark":
                dark_count = dark_count + 1
            j = j + 1
        
        # If box has dark chocolate, must have 2 or 3
        has_dark = False
        if dark_count > 0:
            has_dark = True
        
        box_is_good = True
        if has_dark == True:
            if dark_count < 2 or dark_count > 3:
                box_is_good = False
        
        # Keep box if it's good
        if box_is_good == True:
            boxes.append(box)
            k = 0
            while k < len(box):
                used_truffles.append(box[k])
                k = k + 1
            box_number = box_number + 1
    
    return boxes
