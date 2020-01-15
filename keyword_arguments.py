# Document at least 3 use cases of the * and ** operators


def sum_all(*args):
    """Adds arbitrary numbers in a list or passed as an arguments."""
    try:
        if isinstance(args[0], list):
            return sum(args[0])
        return sum(list(args))
    except TypeError:
        raise TypeError('Takes a list or arguments')


def bio_data(**kwargs):
    """This function gives and ID, and assign role to new user created: name='John Doe', status='[admin, user]'"""
    import random
    _id = random.randint(1000, 9999)
    try:
        for key, value in kwargs.items():
            if kwargs["status"].lower() == 'admin':
                return f'Administrator role has been set for {value} with ID: {_id}'
            elif kwargs["status"].lower() == 'user':
                return f'User role has been set for {value} with ID: {_id}'
            else:
                return f'The role "{kwargs["Status"]}" is not understood'
    except KeyError:
        raise KeyError('use small letters only for keys')


def unknown(*args, **kwargs):
    """Return data type and size of object"""
    data = {'dataType': None, 'content': '', 'size': ''}
    if kwargs:
        data['dataType'] = type(kwargs)
        data['content'] = [kwargs]
        data['size'] = str(kwargs.__sizeof__())+' bytes'
        print(data)

    if args:
        if len(args) > 1:
            data['dataType'] = []
            data['size'] = []
            for x in list(args):
                data['dataType'].append(type(x))
                data['content'] = args
                data['size'].append(str(args.__sizeof__())+' bytes')
        else:
            data['dataType'] = type(*args)
            data['content'] = args
            data['size'] = args.__sizeof__()

    return data


print(unknown({1,2,3},1,2, j=9, b=12))

