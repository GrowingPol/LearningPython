import textwrap

def wrap(string, max_width):
    wraper = textwrap.TextWrapper(width= max_width)
    wrap = wraper.wrap(text= string)
    wrap = "/n".join(wrap)
    return wrap

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)