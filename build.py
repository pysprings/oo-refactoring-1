import glob

import markdown

def main():
    for path in paths():
        write_compiled(path)

def paths():
    return glob.glob('*.markdown')

def read(path):
    return open(path).read()

def compile(path):
    return markdown.markdown(read(path))

def new_path(path):
    return path.replace('.markdown', '.html')

def write_compiled(path):
    open(new_path(path), 'w').write(compile(path))


if __name__ == '__main__':
    main()
