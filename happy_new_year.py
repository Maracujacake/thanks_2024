import curses
import random
import time

# Arte ASCII específica
ascii_art = [
    [
    "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠎⠉⢂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
    "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠎⠀⡄⠈⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
    "⠀⠀⠀⠀⠀⠀⠀⠀⠀⡎⠉⠀⠀⠀⠀⡰⢳⡀⠈⠉⠀⠀⠒⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
    "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠢⠀⠈⠫⡅⠀⠀⢈⠽⠋⠀⡠⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
    "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠃⢀⣇⠤⠤⣺⠀⠰⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⠁⠀⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
    "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡜⠀⠈⠀⣠⢄⠈⠁⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠊⢀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
    "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠣⠤⠒⠉⠀⠀⠁⠢⠀⠜⠀⠀⠀⡖⠐⠂⠠⠄⣀⠀⠀⠀⠀⠀⠀⡠⠊⠀⡠⠊⡇⠀⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
    "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⡀⠀⢤⢀⣀⠀⠁⠐⠂⠠⠎⠀⡠⠊⠀⠀⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
    "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⡄⠈⢆⠀⠉⠑⠒⠠⠤⡠⠞⠀⠀⠀⠀⠀⠀⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
    "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠄⠈⢢⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠀⠘⠢⢄⡀⠀⠀⠀⠀⠀⠀⠀",
    "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢄⠀⢣⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠒⠤⣀⠀⠁⠂⠄⡀⠀⠀⠀",
    "⠀⠀⠀⠀⠀⠀⠔⠂⠢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡨⠂⢀⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠒⢤⡀⠀⠉⠂⡄",
    "⠀⠀⠀⠀⠀⠀⢀⠀⢀⠈⠢⠀⠀⠀⠀⠀⠀⠀⡀⠤⠀⢄⠀⠀⠀⠀⠀⡔⠁⢠⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠠⠔⠒⠉⠁⣀⠤⠄⠒⠁",
    "⠀⠀⠀⠀⠀⠀⢸⠀⢸⠳⢄⠀⠑⠄⠤⠐⠈⠁⢀⠀⢀⠎⠀⠀⠀⢀⠎⠀⡰⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡎⠉⢀⡀⠤⠐⠂⠉⠀⠀⠀⠀⠀",
    "⠀⠀⠀⠀⠀⠀⢸⠀⢸⠀⠀⠑⢄⣀⡠⠤⠒⢩⠃⠀⡌⠀⠀⠀⡠⠃⢀⣞⣀⠤⠤⠔⠒⠒⠉⠲⡀⠀⠀⠀⢠⠇⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
    "⠀⠀⠀⠀⠀⡀⠜⠀⢀⠀⠀⠀⠀⠀⠀⠀⢀⠆⠀⡜⠀⠀⠀⠔⠀⠀⠀⢀⣀⡀⠤⠄⠐⠒⠢⡀⠈⢆⠀⠀⢸⠀⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
    "⠀⢀⠠⠒⠉⢀⡠⠔⠉⠀⠀⠀⠀⠀⠀⠀⣎⠀⠸⡁⠀⠀⠀⠈⠀⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠈⢄⠀⠱⡄⠘⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
    "⡎⠀⠀⠐⠪⠥⣀⣐⠀⠀⠀⠀⠀⠀⠀⠀⠈⠢⡀⠈⢂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⡀⠈⠇⠀⡎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
    "⠈⠀⠒⠀⠤⢀⣀⠀⠉⢱⠀⠀⠀⢀⠤⠤⠀⣀⣘⣄⠀⠑⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢂⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
    "⠀⠀⠀⠀⠀⠀⠀⠘⡄⠀⡆⠀⡠⠃⢀⡀⢀⣀⡀⠀⠀⠀⠈⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
    "⠀⠀⠀⠀⠀⠀⠀⠀⢃⠀⢡⡐⠁⢠⠎⠀⠀⠀⠀⠀⠀⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
    "⠀⠀⠀⠀⠀⠀⠀⠀⠸⠀⠈⠀⡠⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
    "⠀⠀⠀⠀⠀⠀⠀⠀⠀⢇⠀⡔⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"
        # Mais linhas se necessário...
    ],
    [

    "       *         '       *       .  *   '     .           * * ",
   "                                                            ' ",
   "         *                *'          *          *        ' ",
   ".         *               |               / ",
"              '.         |    |      '       |   '     * ",
"                \*        \   \             / ",
"       '          \     '* |    |  *        |*                *  *",
"            *      `.       \   |     *     /    *      '",
"  .                  \      |   \          /               *",
"     *'  *     '      \      \   '.       |",
"        -._            `                  /         *",
"  ' '      ``._   *                           '          .      '",
"   *           *\*          * .   .      *",
"*  '        *    `-._                       .         _..:='        *",
"             .  '      *       *    *   .       _.:--'",
"          *           .     .     *         .-'         *",
"   .               '             . '   *           *         .",
"  *       ___.-=--..-._     *                '               '",
"                                  *       *",
"                *        _.'  .'       `.        '  *             *",
"     *              *_.-'   .'            `.               *",
"                   .'                       `._             *  '",
"   '       '                        .       .  `.     .",
"       .                      *                  `",
"               *        '             '                          .",
"     .                          *        .           *  *",
"             *        .                                    '"
    ],
    [

"        _..od88888bo.._ ",
"      .d'''   888   '''b. ",
"    .d''      888      ''b. ",
"   d''        888        ''b ",
"  d'          888          'b ",
" 88          88888          88 ",
"(88         8888888         88) ",
" 88        888888888        88 ",
"  YI      888 888 888      IP ",
"   YI    888  888  888    IP ",
"    '9. 888   888   888 .P' ",
"      '888    888    888' ",
"       '''Y8888888P''' "
    ],
    [
"   .--.       .-.     .--.    ,-----.  ",
" ;  _  \   /    \   ;  _  \  |   ___) ",
"(___)` |  |  .-. ; (___)` |  |  |     ",
"     ' '  | |  | |      ' '  |  '-.   ",
"    / /   | |  | |     / /   '---.  . ",
"   / /    | |  | |    / /     ___ `  \ ",
"  / /     | '  | |   / /     (   ) | |",
" / '____  '  `-' /  / '____   ; `-'  /",
"(_______)  `.__,'  (_______)   '.__.' "
    ],
    [
"███████╗███████╗██╗     ██╗███████╗", 
"██╔════╝██╔════╝██║     ██║╚══███╔╝" , 
"█████╗  █████╗  ██║     ██║  ███╔╝"   ,
"██╔══╝  ██╔══╝  ██║     ██║ ███╔╝"    ,
"██║     ███████╗███████╗██║███████╗"  ,
"╚═╝     ╚══════╝╚══════╝╚═╝╚══════╝",
"                           "         , 
" █████╗ ███╗   ██╗ ██████╗"           ,
"██╔══██╗████╗  ██║██╔═══██╗"         ,
"███████║██╔██╗ ██║██║   ██║"         ,
"██╔══██║██║╚██╗██║██║   ██║"         ,
"██║  ██║██║ ╚████║╚██████╔╝"          ,
"╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝",
"                                    ",
"███╗   ██╗ ██████╗ ██╗   ██╗ ██████╗",
"████╗  ██║██╔═══██╗██║   ██║██╔═══██╗",
"██╔██╗ ██║██║   ██║██║   ██║██║   ██║",
"██║╚██╗██║██║   ██║╚██╗ ██╔╝██║   ██║",
"██║ ╚████║╚██████╔╝ ╚████╔╝ ╚██████╔╝",
"╚═╝  ╚═══╝ ╚═════╝   ╚═══╝   ╚═════╝"
    ]
]

# Função para mostrar a arte ASCII
def show_ascii_art(stdscr, art, start_y, start_x, color_pair):
    """Exibe a arte ASCII no terminal."""
    for i, line in enumerate(art):
        try:
            stdscr.addstr(start_y + i, start_x, line, curses.color_pair(color_pair))
        except curses.error:
            pass  # Ignora erros quando a arte excede os limites da tela
    stdscr.refresh()
    time.sleep(1)

# Função para simular os fogos de artifício
def animate_fireworks(stdscr, num_fireworks):
    curses.curs_set(0)  # Esconde o cursor
    stdscr.clear()
    
    # Inicializa as cores
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)   # Par de cores (vermelho no fundo preto)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Verde
    curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)   # Azul
    curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK) # Amarelo

    height, width = stdscr.getmaxyx()

    for _ in range(num_fireworks): 
        # Posição inicial do foguete, centralizada horizontalmente
        center_x = width // 2
        x = random.randint(center_x - width // 4, center_x + width // 4)  # Centraliza o range
        y = height - 1

        # Trajetória do foguete subindo
        for _ in range(height // 2):
            stdscr.clear()
            stdscr.addstr(y, x, '|')
            y -= 1
            stdscr.refresh()
            time.sleep(0.05)

        # Explosão
        explode_firework(stdscr, y, x)

        # Seleção e exibição da arte ASCII
        chosen_art = random.choice(ascii_art)
        stdscr.clear()
        start_y = max(0, y - len(chosen_art) // 2)
        start_x = max(0, x - max(len(line) for line in chosen_art) // 2)

        color_pair = random.randint(1, 4)
        show_ascii_art(stdscr, chosen_art, start_y, start_x, color_pair)

        time.sleep(0.5)

    # Exibe a mensagem "FELIZ 2025"
    stdscr.clear()  # Limpa a tela
    msg = "FELIZ 2025"
    start_y = height // 2
    start_x = width // 2 - len(msg) // 2  # Centraliza o texto
    stdscr.addstr(start_y, start_x, msg)
    stdscr.refresh()

    time.sleep(3)  # Exibe a mensagem por 3 segundos

# Função de explosão
def explode_firework(stdscr, y, x):
    """Simula uma explosão genérica com um único caractere '*' por vez, seguida pela arte ASCII."""
    # Padrão da explosão com apenas um '*'
    stdscr.clear()
    stdscr.addstr(y, x, "*")
    stdscr.refresh()
    time.sleep(0.2)  # Exibe um único '*' por um curto tempo


def main():
    # Quantidade de fogos de artifício
    num_fireworks = 10
    
    # Inicia a animação
    curses.wrapper(animate_fireworks, num_fireworks)

if __name__ == "__main__":
    main()
