def age_assignment(*args, **kwargs):
    persons = {}
    for name in args:
        persons[name] = kwargs[name[0]]

    persons = sorted(persons.items())

    result = []
    for name, age in persons:
        result.append(f"{name} is {age} years old.")

    return "\n".join(result)


print(age_assignment("Peter", "George", G=26, P=19))
