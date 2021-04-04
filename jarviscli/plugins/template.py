from plugin import plugin
from colorama import Fore
import os
from os.path import expanduser



@plugin("template")
def template(jarvis, s):
    """
    Creates project templates in the language specified
    template -l <language name> -n <project name> -p <path to project>
    """
    args = { 'lang': None, 'name': None, 'path': None }

    if s == "":
        # prompt user for arguments
        args['name'] = input("Project name: ")
        args['lang'] = input("Language: ")
        args['path'] = expanduser(input("Project path: "))
    else:
        # parse args passed by user
        s_args = s.split(' ')
        i = 0
        while i < len(s_args):
            if s_args[i].lower() == '-n':
                args['name'] = s_args[i + 1]
                i += 1
            elif s_args[i].lower() == '-l':
                args['lang'] = s_args[i + 1]
                i += 1
            elif s_args[i].lower() == '-p':
                args['path'] = expanduser(s_args[i + 1])
                i += 1
            else:
                jarvis.say(f'Invalid argument: {s_args[i]}', Fore.RED)
                if len(s_args) < i + 1:
                    if '-' not in s_args[i + 1]:
                        i += 1
            i += 1

    # prompt user for missing arguments
    for key in args:
        if args[key] == None:
            new_arg = ""
            if key == 'lang':
               new_arg = input('Language: ')
            elif key == 'name':
                new_arg = input('Project name: ')
            else:
                new_arg = expanduser(input('Project path: '))
            
            args[key] = new_arg
    
    # continuse prompting for path until a valid one is given
    while True:
        if not os.path.exists(args['path']):
            jarvis.say("Invalid path!", Fore.RED)
            args['path'] = expanduser(input("Project path: "))
        else:
            break

    if args['lang'].lower() == 'python':
        python_template(args)
    elif args['lang'].lower() == 'java':
        java_template(args)
    elif args['lang'].lower() == 'c':
        c_template(args)
    elif args['lang'].lower() == 'node':
        node_template(args)
    elif args['lang'].lower() == 'rust':
        rust_template(args)
    else:
        jarvis.say(f"No template available for: {args['lang']}")

    jarvis.say("Template created!", Fore.GREEN)

# template for python
def python_template(args):
    py_template = """#!/usr/bin/env python3 
    
def main():
    pass

if __name__ == '__main__':
    main()"""

    os.system(f"""\
        cd {args['path']}\
        && mkdir {args['name']}\
        && cd {args['name']}\
        && touch main.py\
    """)

    with open(f"{args['path']}/{args['name']}/main.py", "w") as f:
        f.write(py_template)
        f.close()

# java main class template
def java_template(args):
    classname = args['name'].capitalize()

    java_template = "public class %s\n{\n\tpublic static void main(String[] args)\n\t{\n\t\tSystem.out.println(\"Hello world!\");\n\t}\n}" % classname

    os.system(f"""\
        cd {args['path']}\
        && mkdir {args['name']}\
        && cd {args['name']}\
        && touch {classname}.java\
    """)

    with open(f"{args['path']}/{args['name']}/{classname}.java", "w") as f:
        f.write(java_template)
        f.close()

# c main file template and Makefile
def c_template(args):
    makefile = f"""CC = gcc
CFLAGS = -Wall -Wextra -std=c99
SOURCES = main.c
LIBS =
OBJECTS = $(subst .c, .o, $(SOURCES))
BIN = {args['name']}

{args['name']}: $(OBJECTS)
    $(CC) $(CFLAGS) $^ $(LIBS) -o $@
    
%.o : %.c
    $(CC) $(CFLAGS) -c $<

all: $(BIN)

clean:
    rm -f $(OBJECTS) $(BIN) *~"""

    mainfile = """#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{


    return 0;
}"""

    os.system(f"""\
        cd {args['path']}\
        && mkdir {args['name']}\
        && cd {args['name']}\
        && touch Makefile\
        && touch main.c\
    """)

    with open(f"{args['path']}/{args['name']}/Makefile", "w") as f:
        f.write(makefile)
        f.close()

    with open(f"{args['path']}/{args['name']}/main.c", "w") as f:
        f.write(mainfile)
        f.close()

# nodejs template with index.html and main.js
def node_template(args):
    index_html = """<!DOCTYPE html>
<html>
    <head>
    </head>
    <body>
        <div id='root'></div>
    </body>
    <script src="main.js"></script>
</html>
"""

    os.system(f"""\
        cd {args['path']}\
        && mkdir {args['name']}\
        && cd {args['name']}\
        && npm init -y\
        && touch index.html\
        && touch main.js\
    """)

    with open(f"{args['path']}/{args['name']}/index.html", "w") as f:
        f.write(index_html)
        f.close()

# create a new rust project
def rust_template(args):
    os.system(f"""\
        cd {args['path']}\
        && cargo new --bin {args['name']}\
    """)