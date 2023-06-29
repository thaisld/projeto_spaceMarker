import pygame
import tkinter as tk
from tkinter import simpledialog
import json
pygame.init()

tamanho = (900, 600)
preto = (0, 0, 0)
fundo = pygame.image.load("galaxia.png")
display = pygame.display.set_mode(tamanho)
pygame.display.set_caption("SPACE MARKER")
running = True
def estrelas_marcadas(pos):
    root = tk.Tk()
    root.withdraw()
    nome = simpledialog.askstring("Nome da Estrela", "Digite o nome da estrela:")
    if nome:
        print(f"Nome da estrela: {nome}")
        print(f"Posição do clique: {pos}")
def salvarMarcacoes():
    with open("marcacoes.json", "w") as arquivo:
         json.dump(estrelas_marcadas, arquivo)
         print("As marcações foram salvas com sucesso!")
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Botão esquerdo do mouse
                mouse_pos = pygame.mouse.get_pos()
                estrelas_marcadas(mouse_pos)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  # Tecla ESC para sair
                salvarMarcacoes()
                running = False
    display.fill(preto)
    display.blit(fundo, (0, 0))
    pygame.display.update()
pygame.quit()