from pyscript import display, document

def check_intramurals(event):
    document.getElementById("output").innerHTML = ""

    is_registered = document.getElementById("reg_yes").checked
    has_medical = document.getElementById("med_yes").checked
    grade = int(document.getElementById("grade").value)
    section = document.getElementById("section").value

    if not is_registered:
        display("Please complete the online registration.", target="output")
    elif not has_medical:
        display("Please secure a medical clearance.", target="output")
    elif grade < 7 or grade > 10:
        display("You are not eligible for Intramurals.", target="output")
    else:
        if grade == 7:
            team = "Blue Bears"
            img_file = "blue_bears.jpg"
        elif grade == 8:
            team = "Red Bulldogs"
            img_file = "red_bulldogs.jpg"
        elif grade == 9:
            team = "Yellow Tigers"
            img_file = "yellow_tigers.jpg"
        else:
            team = "Green Hornets"
            img_file = "green_hornets.jpg"

      
        display(f"Congratulations! You are part of the {team} (Grade {grade} {section}).", target="output")
        img_element = document.createElement("img")
        img_element.src = img_file
        img_element.width = 350
        document.getElementById("output").appendChild(img_element)
