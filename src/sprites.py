import pygame
def pegar_sprite(sheet, x, y, width, height, scale=1):
    """
    Recorta um sprite individual de uma spritesheet BMP e aplica transparência. A função extrai uma região específica da spritesheet e remove o fundo escuro (tons de preto), convertendo em transparência. Também permite redimensionar o sprite final.

    Parâmetros:
        sheet (pygame.Surface): Spritesheet carregada.
        x (int): Coordenada X inicial do recorte.
        y (int): Coordenada Y inicial do recorte.
        width (int): Largura do sprite.
        height (int): Altura do sprite.
        scale (float): Escala aplicada ao sprite. Padrão = 1.

    Retorno:
        pygame.Surface: Sprite recortado, com transparência aplicada e redimensionado.
    """
    image = pygame.Surface((width, height), pygame.SRCALPHA)
    image.blit(sheet, (0, 0), (x, y, width, height))

    for px in range(width):
        for py in range(height):
            r, g, b, *_ = image.get_at((px, py))

            if r < 7 and g < 7 and b < 7:
                image.set_at((px, py), (0, 0, 0, 0))

    if scale != 1:
        novo_largura = int(width * scale)
        novo_altura = int(height * scale)
        image = pygame.transform.scale(image, (novo_largura, novo_altura))
    return image

def carregar_animacao(caminho, frames, scale = 0.5):
    """
    Carrega uma sequência de sprites a partir de uma spritesheet. A função abre a imagem da spritesheet e recorta todos os frames definidos na lista da animação, retornando uma animação completa.

    Parâmetros:
        caminho (str): Caminho do arquivo da spritesheet.
        frames (list): Lista de tuplas (x, y, largura, altura) dos frames.
        scale (float): Escala aplicada a todos os sprites.

    Retorno:
        list[pygame.Surface]: Lista contendo todos os frames da animação.
    """
    sheet = pygame.image.load(caminho).convert()
    return [
        pegar_sprite(sheet, x, y, w, h, scale=scale)
        for x, y, w, h in frames
    ]