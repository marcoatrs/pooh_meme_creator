import math
from argparse import ArgumentParser


parser = ArgumentParser()

parser.add_argument("-t", "--text", help="Texto a poner")


args = parser.parse_args()

pooh = r'''
                _.
    ,-.,-"`""-./  \
   /   \        `-.|
   \   /           `-._
   |                 "=\
   |        .=="    |o_|_
   |         _o.     ` (_)         _____________________________
   ;                     \\        |                           |
    \             _.     /|-.     <                            |
     \           ` `'---'/   \     \___________________________|
      \       .--._     /-'   |                    Exclamó pooh.
     ,-`.    /     `-._(     /
     `-._`-._\         `\   '\
       ( `    `'._  _,   |    \
       /    ~-.   `|     |    |
      /        `;-.|     |    |
    .'  \         /|     |    /
  .'-.   '.      | \     |  .'
  `-._     '.    |       /"` `\
   /  `"--.,_'-._\-.___.'_     ;
  /          `""";--'     `.   |
 /            .'`            \ /""-.
;            /                \""-, \
|           /                 |    \ |
\           |          '.           |/
 '.          \         .'`-.        /
   '._        '.,___,.;'    '-.___.'
      `"""----------'`
'''

def center_text(text: str, num: int) -> str:
    _len = num - len(text)
    if _len % 2 != 0:
        left = int(math.ceil(_len / 2))
        rigth = int(math.floor(_len / 2))
    else:
        left = _len // 2
        rigth = _len // 2
    return f"{' ' * left}{text}{' ' * rigth}"

def print_pooh(text: str):
    if len(text) >= 25:
        text_w = text.split(" ")
        text1 = " ".join(text_w[:len(text_w) // 2])
        text2 = " ".join(text_w[len(text_w) // 2:])
        dialog1 = f"|{center_text(text1, 27)}|"
        dialog2 = f"<{center_text(text2, 28)}|"
    else:
        dialog1 = "|                           |"
        dialog2 = f"<{center_text(text, 28)}|"
    new_pooh = pooh.replace("|                           |", dialog1)
    new_pooh = new_pooh.replace("<                            |", dialog2)
    print(new_pooh)

print_pooh(args.text)
