from lib import some_func


def input_output():
    print("no console.log for me!")

    print("that's the standard output")

    print("but what about input?")

    color = input("what's my favorite color?")

    color_response = "You're favorite color is " + color + ". Great choice!"

    print(color_response)

    formatted_string = f"You're favorite color is {color}. Great choice!"

    print(formatted_string)

    runnerup_color = input("What's your second favorite color? ")

    faves_template = "Your two favorite colors are {} and {}. Great combo!".format(
        color_response, formatted_string
    )

    print(faves_template)

    print(faves_template.format(color, runnerup_color))


input_output()

# print(some_func())
