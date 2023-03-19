def greet4(first_name="John", last_name="Doe"):
    """
    Greet again
    :param first_name: first name of the person, default=John
    :param last_name: last name, default=Doe
    :return: None
    """
    print(f"Hello {first_name} {last_name}, this is pretty cool, right?")

greet4("Lucas", "Baptiste")
greet4()
greet4("James")

greet4("Michael", "Jordan")
greet4(last_name="Jordan", first_name="Michael")


