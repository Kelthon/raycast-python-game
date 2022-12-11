from game.src.utils import *
from game.src.facade import *
from game.src.writer import *
from game.src.item import Item
from game.src.enemy import Enemy
from game.src.level import Level
from game.src.window import Window
from game.src.raycast import Raycaster
from game.src.player import Collider, Player

items_size = Vector2(100, 100)
tela_size = Vector2(800, 600)
tela_bg_color = Color(0, 0, 0)
tela_background_image = pygame.image.load("./game/public/textures/skybox_2.png")


tela = Window(tela_size, tela_bg_color, tela_background_image)


tela_center = tela.center()

skybox = Item.get_surface_by_filepath("./game/public/textures/skybox.png")
aux_digital = Item.get_surface_by_filepath("./game/public/textures/auxilio_digital.png")
aux_oculos = Item.get_surface_by_filepath("./game/public/textures/auxilio_oculos.png")
bolsa_petista = Item.get_surface_by_filepath("./game/public/textures/bolsa_petista.png")
cachaca51_1 = Item.get_surface_by_filepath("./game/public/textures/cachaca51_1.png")
cachaca51_2 = Item.get_surface_by_filepath("./game/public/textures/cachaca51_2.png")
coin = Item.get_surface_by_filepath("./game/public/textures/coin.png")
marlboro = Item.get_surface_by_filepath("./game/public/textures/marlboro.png")
meat = Item.get_surface_by_filepath("./game/public/textures/meat.png")
money_1 = Item.get_surface_by_filepath("./game/public/textures/money_1.png")
money_1 = Item.get_surface_by_filepath("./game/public/textures/money_2.png")
money_bag = Item.get_surface_by_filepath("./game/public/textures/money_bag.png")
purse = Item.get_surface_by_filepath("./game/public/textures/purse.png")
small_purse = Item.get_surface_by_filepath("./game/public/textures/small_purse.png")
suitcase = Item.get_surface_by_filepath("./game/public/textures/suitcase.png")
xicara = Item.get_surface_by_filepath("./game/public/textures/xicara_cafe.png")

ref = center(center(tela.center()))

map_1 = [
    draw.rect(tela.surface, [160]*3, (0, 0, 5, 120)),
    draw.rect(tela.surface, [160]*3, (5, 0, 115, 5)),
    draw.rect(tela.surface, [160]*3, (0, 120, 70, 5)),
    draw.rect(tela.surface, [160]*3, (120, 0, 5, 70)),
    draw.rect(tela.surface, [160]*3, (120, 0, 5, 70)),
    draw.rect(tela.surface, [160]*3, (120, 0, 5, 70)),
    draw.rect(tela.surface, [160]*3, (tela.size.x - 5, 0, 5, 120)),
    draw.rect(tela.surface, [160]*3, (tela.size.x - 120, 0, 115, 5)),
    draw.rect(tela.surface, [160]*3, (tela.size.x - 125, 0, 5, 70)),
    draw.rect(tela.surface, [160]*3, (tela.size.x - 70, 120, 70, 5)),
    draw.rect(tela.surface, [160]*3, (0, tela.size.y - 120, 5, 120)),
    draw.rect(tela.surface, [160]*3, (5, tela.size.y - 5, 115, 5)),
    draw.rect(tela.surface, [160]*3, (120, tela.size.y - 70, 5, 70)),
    draw.rect(tela.surface, [160]*3, (5, tela.size.y - 120, 70, 5)),
    draw.rect(tela.surface, [160]*3, (tela.size.x - 5, tela.size.y - 120, 5, 120)),
    draw.rect(tela.surface, [160]*3, (tela.size.x - 120, tela.size.y - 5, 115, 5)),
    draw.rect(tela.surface, [160]*3, (tela.size.x - 120, tela.size.y - 70, 5, 70)),
    draw.rect(tela.surface, [160]*3, (tela.size.x - 70, tela.size.y - 120, 70, 5)),
    draw.rect(tela.surface, [160]*3, (tela_center.x - 150, tela_center.y - 100, 70, 5)),
    draw.rect(tela.surface, [160]*3, (tela_center.x - 35, tela_center.y - 100, 70, 5)),
    draw.rect(tela.surface, [160]*3, (tela_center.x + 80, tela_center.y - 100, 70, 5)),
    draw.rect(tela.surface, [160]*3, (tela_center.x - 155, tela_center.y - 100, 5, 200)),
    draw.rect(tela.surface, [160]*3, (tela_center.x + 150, tela_center.y - 100, 5, 200)),
    draw.rect(tela.surface, [160]*3, (tela_center.x - 155, tela_center.y + 100, 100, 5)),
    draw.rect(tela.surface, [160]*3, (tela_center.x + 55, tela_center.y + 100, 100, 5)),
]

map_2 = [
    draw.rect(tela.surface, [160]*3, (ref, Vector2(60, 60))),
    draw.rect(tela.surface, [160]*3, (Vector2(ref.x*6 + 60, ref.y), Vector2(60, 60))),
    draw.rect(tela.surface, [160]*3, (Vector2(ref.x, ref.y*6), Vector2(60, 60))),
    draw.rect(tela.surface, [160]*3, (Vector2(ref.x*6 + 60, ref.y*6), Vector2(60, 60))),
    draw.rect(tela.surface, [160]*3, (tela.size.x - 5, tela.size.y - 120, 5, 120)),
    draw.rect(tela.surface, [160]*3, (tela.size.x - 120, tela.size.y - 5, 115, 5)),
    draw.rect(tela.surface, [160]*3, (tela.size.x - 120, tela.size.y - 70, 5, 70)),
    draw.rect(tela.surface, [160]*3, (tela.size.x - 70, tela.size.y - 120, 70, 5)),
    draw.rect(tela.surface, [160]*3, (tela_center.x - 150, tela_center.y - 100, 70, 5)),
    draw.rect(tela.surface, [160]*3, (tela_center.x + 80, tela_center.y - 100, 70, 5)),
    draw.rect(tela.surface, [160]*3, (tela_center.x - 155, tela_center.y - 100, 5, 200)),
    draw.rect(tela.surface, [160]*3, (tela_center.x + 150, tela_center.y - 100, 5, 200)),
    draw.rect(tela.surface, [160]*3, (tela_center.x - 155, tela_center.y + 100, 100, 5)),
    draw.rect(tela.surface, [160]*3, (tela_center.x + 55, tela_center.y + 100, 100, 5)),
]

binds = [
    {
        "dir": Vector2(0, -1),
        "key": local.K_w,
        "col": Collider.top
    },
    {
        "dir": Vector2(0, 1),
        "key": local.K_s,
        "col": Collider.down
    },
    {
        "dir": Vector2(-1, 0),
        "key": local.K_a,
        "col": Collider.left
    },
    {
        "dir": Vector2(1, 0),
        "key": local.K_d,
        "col": Collider.right
    }
]


items = [aux_digital, aux_oculos, bolsa_petista, cachaca51_1, cachaca51_2, coin, marlboro, meat, money_1, money_1, money_bag, purse, small_purse, suitcase, xicara]


mixer.music.load("game/public/sound effects/ShotGun-Cocking_background.wav")
mixer.music.set_volume(0.7)


color_white = (255, 255, 255)
color_light = (128, 128, 128)
color_dark = (0, 0, 0)

impact_font = pygame.font.SysFont('Impact', 30)

text_1 = impact_font.render('JOGAR', True, color_white)
text_2 = impact_font.render('QUIT', True, color_white)
text_3 = impact_font.render('HELP',True, color_white)

button_size = Vector2(140, 40)

button_jogar_position = Vector2(tela.size.x/2 - button_size.x/2, tela.size.y/2 + 100)
button_quit_position = Vector2(tela.size.x/2 - button_size.x/2, tela.size.y/2 + 150)
button_help_position = Vector2(tela.size.x/2 - button_size.x/2, tela.size.y/2 + 200)

collider = Collider()
player = Player(tela.center(), 1, 10, collider, binds)
enemy_1  = Enemy(Vector2(200,80), player)
enemy_2  = Enemy(Vector2(200,300), player)
enemies = [enemy_1, enemy_2]
phase_1 = Level(map_1, player, [enemy_1], suffle_items(items))
phase_2 = Level(map_2, player, enemies, suffle_items(items))

writer = Writer()