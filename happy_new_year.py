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
    ],
    [
"”˜˜”*°•. ˜”*°• . •°*”˜ .•°*”˜˜”*°•.",
".•°*”˜ HAPPY NEW YEAR ˜”*°•.",
"•°*”˜.•°*”˜.•°*”˜ ˜”*°•.˜”*°•.˜”*°",
"_______0__o_o__o_0_0_o_o__0",
"______0___o__o__o0_0__o_o__0",
"_____0___o__o_o__0_0__o___o__0",
"____0_o___o___o__0_0___o___o__0",
"____00o0000o00o0o0_0o00o00oo0oo0",
"___000o0o00000o000_000o00o0o000o0",
"___00000o000o000o0_000o000o00000o0",
"___0o00oo00o0o00o0__0000o0o0o00000",
"___0o0o00000o00o0___000o0o0o0o0o00",
"____0o0o0000o0o0_____0000o00o00o0",
"_____0000o0000________ 00o000o000",
"______0000000___________0000000",
"________00_________________00",
"_______00___________________00",
"______00_____________________00",
"_____00_______________________00",
"____00_________________________00",
"_00000000___________________00000000",
"---------------------------------------------------",
"-------------------♥♥♥Cheers!-------------------",
"---------------------------------------------------"
    ]
]

# Desenha o céu estrelado ;-)
def draw_starry_sky(stdscr):
    """Desenha um fundo com estrelas piscando aleatoriamente."""
    height, width = stdscr.getmaxyx()
    for _ in range(50):  # Ajuste o número de estrelas
        y = random.randint(0, height - 1)
        x = random.randint(0, width - 1)
        if random.choice([True, False]):  # Faz algumas estrelas piscarem
            stdscr.addstr(y, x, '.', curses.color_pair(random.randint(1, 4)))


# Simula sons dos fogos de artifício (texto ne)
def simulate_sound(stdscr, y, x):
    """Exibe sons simulados no terminal próximo à explosão."""
    sounds = ["BOOM!", "POW!", "FIUUMM!", "PEM!"]
    sound = random.choice(sounds)
    sound_y = y + random.randint(-1, 1)
    sound_x = x + random.randint(-len(sound) // 2, len(sound) // 2)
    try:
        stdscr.addstr(sound_y, sound_x, sound, curses.color_pair(random.randint(1, 4)))
        stdscr.refresh()
        time.sleep(0.3)
    except curses.error:
        pass


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

# Exibe a mensagem final
def show_final_message(stdscr):
    """Exibe a mensagem final com cores e movimento."""
    msg = "FELIZ 2025"
    height, width = stdscr.getmaxyx()
    start_y = 0
    end_y = height // 2
    start_x = width // 2 - len(msg) // 2

    for y in range(start_y, end_y + 1):
        stdscr.clear()
        draw_starry_sky(stdscr)  # Mantém o fundo com estrelas
        color_pair = random.randint(1, 4)
        try:
            stdscr.addstr(y, start_x, msg, curses.color_pair(color_pair))
        except curses.error:
            pass
        stdscr.refresh()
        time.sleep(0.1)

    # Pisca a mensagem no final
    for _ in range(5):
        stdscr.clear()
        draw_starry_sky(stdscr)
        color_pair = random.randint(1, 4)
        stdscr.addstr(end_y, start_x, msg, curses.color_pair(color_pair))
        stdscr.refresh()
        time.sleep(0.5)

# Função para simular os fogos de artifício
def animate_fireworks(stdscr, num_fireworks):
    curses.curs_set(0)  # Esconde o cursor
    
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
            stdscr.clear()  # Remove elementos antigos
            draw_starry_sky(stdscr)  # Redesenha o fundo estrelado
            stdscr.addstr(y, x, '|')  # Adiciona o foguete
            y -= 1
            stdscr.refresh()
            time.sleep(0.05)

        # Explosão
        stdscr.clear()
        draw_starry_sky(stdscr)  # Redesenha o fundo estrelado
        explode_firework(stdscr, y, x)

        # Seleção e exibição da arte ASCII
        chosen_art = random.choice(ascii_art)
        stdscr.clear()
        draw_starry_sky(stdscr)  # Redesenha o fundo estrelado
        start_y = max(0, y - len(chosen_art) // 2)
        start_x = max(0, x - max(len(line) for line in chosen_art) // 2)

        color_pair = random.randint(1, 4)
        show_ascii_art(stdscr, chosen_art, start_y, start_x, color_pair)

        time.sleep(0.5)

    # Exibe a mensagem "FELIZ 2025"
    stdscr.clear()
    draw_starry_sky(stdscr)  # Mantém o fundo estrelado
    show_final_message(stdscr)
    time.sleep(3)


# Função de explosão
def explode_firework(stdscr, y, x):
    """Simula uma explosão genérica com um único caractere '*' por vez, seguida pela arte ASCII."""
    # Padrão da explosão com apenas um '*'
    stdscr.clear()
    stdscr.addstr(y, x, "*")
    stdscr.refresh()
    simulate_sound(stdscr, y, x)
    time.sleep(0.2)  # Exibe um único '*' por um curto tempo


def main():
    # Quantidade de fogos de artifício
    num_fireworks = 10
    
    # Inicia a animação
    curses.wrapper(animate_fireworks, num_fireworks)

if __name__ == "__main__":
    main()
