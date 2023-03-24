# Do not modify these lines
__winc_id__ = "7b9401ad7f544be2a23321292dd61cb6"
__human_name__ = "arguments"

# Add your code after this line


def greet(name, template="Hello, <name>!"):
    replaced_text = template.replace("<name>", name)
    return replaced_text


print(greet("Sasha"))
print(greet("Bob", "What's up, <name>!"))


def force(mass, body="earth"):
    bodies = {
        "sun": 274,
        "jupiter": 24.9,
        "neptune": 11.2,
        "saturn": 10.4,
        "earth": 9.8,
        "uranus": 8.9,
        "venus": 8.9,
        "mars": 3.7,
        "mercury": 3.7,
        "moon": 1.6,
        "pluto": 0.6,
    }
    calculate = mass * bodies[body.lower()]
    return calculate


print(force(0.5, "Uranus"))


def pull(m1, m2, d):
    return 6.674 * 10**-11 * (m1 * m2 / d**2)


print(pull(800, 1500, 3))
