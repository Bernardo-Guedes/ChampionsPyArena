import pygame
def pegar_sprite(sheet, x, y, width, height, scale=1):
    
    """Corta um único elemento de uma spritesheet BMP e remove o fundo."""
    # 1. Carrega o BMP e usa .convert() (sem alpha) para otimizar a velocidade
    # 2. Cria uma superfície padrão para o recorte (não precisa de SRCALPHA aqui)
    image = pygame.Surface((width, height), pygame.SRCALPHA)
    # 3. Copia o pedaço da folha BMP para a nossa nova imagem
    image.blit(sheet, (0, 0), (x, y, width, height))

    # 4. CONFIGURAÇÃO DA TRANSPARÊNCIA (O segredo para o BMP)
    for px in range(width):
        for py in range(height):
            r, g, b, *_ = image.get_at((px, py))

            if r < 7 and g < 7 and b < 7:
                image.set_at((px, py), (0, 0, 0, 0))

    # 5. Aplica o redimensionamento, se houver
    if scale != 1:
        novo_largura = int(width * scale)
        novo_altura = int(height * scale)
        image = pygame.transform.scale(image, (novo_largura, novo_altura))
    return image

def carregar_animacao(caminho, frames, scale = 0.5):
    sheet = pygame.image.load(caminho).convert()
    return [
        pegar_sprite(sheet, x, y, w, h, scale=scale)
        for x, y, w, h in frames
    ]