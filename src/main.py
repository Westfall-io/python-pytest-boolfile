from yaml import load, SafeLoader
from yaml.constructor import ConstructorError

test_file = 'test.txt'
def read_bool(stream):
    data = stream.read().strip()
    if data.lower() in ['true','1']:
        val = True
    elif data.lower() in ['false','0']:
        val = False
    else:
        raise AttributeError
    return val

def test_read_bool(input_file='input.txt'):
    with open(input_file, 'r') as f:
        data = f.read()
        data = load(data, Loader=SafeLoader)
        with open(data['file'], 'r') as f2:
            val = read_bool(f2)
    assert val

def test_read_True():
    with open(test_file, 'w') as f:
        f.write('True')

    with open(test_file, 'r') as f:
        val = read_bool(f)
    assert val

def test_read_False():
    with open(test_file, 'w') as f:
        f.write('False')

    with open(test_file, 'r') as f:
        val = read_bool(f)
    assert not val
