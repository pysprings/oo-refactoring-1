import glob

import markdown

def main():
    paths = glob.glob('*.markdown')
    for path in paths:
        content = open(path).read()
        compiled = markdown.markdown(content)
        new_path = path.replace('.markdown', '.html')
        open(new_path, 'w').write(compiled)

if __name__ == '__main__':
    main()
