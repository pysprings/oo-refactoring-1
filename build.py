import glob

import markdown

def main():
    for path in paths():
        Page(path).write_compiled()

def paths():
    return glob.glob('*.markdown')

class Page:
    def __init__(self, path):
        self.path = path

    def read(self):
        return open(self.path).read()

    def compile(self):
        return markdown.markdown(self.read())

    def new_path(self):
        return self.path.replace('.markdown', '.html')

    def write_compiled(self):
        open(self.new_path(), 'w').write(self.compile())


if __name__ == '__main__':
    main()
