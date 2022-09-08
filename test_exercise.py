
def str_to_bool(value):

    try:
        value = value.lower()
    except AttributeError:
        raise AttributeError(f"{value} must be of type string")

    true_values = ['y', 'yes']
    false_values = ['n', 'no']

    if value in true_values:
        return True
    elif value in false_values:
        return False
