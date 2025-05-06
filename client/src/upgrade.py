import pygame
from settings import *

class Upgrade:
    def __init__(self,player):
        # Configuración general
        self.display_surface = pygame.display.get_surface()  # Superficie donde se dibuja la interfaz
        self.player = player  # Referencia al jugador
        self.attribute_nr = len(player.stats)  # Número de atributos que se pueden mejorar
        self.attribute_names = list(player.stats.keys())  # Nombres de los atributos
        self.max_values = list(player.max_stats.values())  # Valores máximos de los atributos
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)  # Fuente para los textos

        # Creación de los ítems del menú de mejora
        self.height = self.display_surface.get_size()[1] * 0.8
        self.width = self.display_surface.get_size()[0] // 6
        self.create_items()

        # Sistema de selección
        self.selection_index = 0  # Índice del atributo seleccionado actualmente
        self.selection_time = None  # Momento en que se hizo la última selección
        self.can_move = True  # Controla si se puede mover la selección

    def input(self):
        keys = pygame.key.get_pressed()

        # Navegación entre atributos y selección de mejora
        if self.can_move:
            if keys[pygame.K_RIGHT] and self.selection_index < self.attribute_nr - 1:
                self.selection_index += 1
                self.can_move = False
                self.selection_time = pygame.time.get_ticks()
            elif keys[pygame.K_LEFT] and self.selection_index >= 1:
                self.selection_index -= 1
                self.can_move = False
                self.selection_time = pygame.time.get_ticks()

            if keys[pygame.K_SPACE]:
                self.can_move = False
                self.selection_time = pygame.time.get_ticks()
                self.item_list[self.selection_index].trigger(self.player)  # Intenta mejorar el atributo seleccionado

    def selection_cooldown(self):
        # Controla el tiempo entre movimientos de selección para evitar cambios rápidos
        if not self.can_move:
            current_time = pygame.time.get_ticks()
            if current_time - self.selection_time >= 300:
                self.can_move = True

    def create_items(self):
        self.item_list = []

        # Crea un objeto Menu_Item por cada atributo
        for item, index in enumerate(range(self.attribute_nr)):
            # Posición horizontal
            full_width = self.display_surface.get_size()[0]
            increment = full_width // self.attribute_nr
            left = (item * increment) + (increment - self.width) // 2
            
            # Posición vertical
            top = self.display_surface.get_size()[1] * 0.1

            # Crear el objeto Menu_Item
            item = Menu_Item(left,top,self.width,self.height,index,self.font)
            self.item_list.append(item)

    def display(self):
        self.input()
        self.selection_cooldown()

        # Dibuja cada ítem del menú de mejora
        for index, item in enumerate(self.item_list):
            name = self.attribute_names[index]
            value = self.player.get_value_by_index(index)
            max_value = self.max_values[index]
            cost = self.player.get_cost_by_index(index)
            item.display(self.display_surface,self.selection_index,name,value,max_value,cost)

class Menu_Item:
    def __init__(self,l,t,w,h,index,font):
        self.rect = pygame.Rect(l,t,w,h)  # Rectángulo que representa el área del ítem
        self.index = index  # Índice del atributo
        self.font = font  # Fuente para los textos

    def display_names(self,surface,name,cost,selected):
        color = TEXT_COLOR_SELECTED if selected else TEXT_COLOR

        # Renderiza el nombre del atributo y el costo de mejora
        title_surf = self.font.render(name,False,color)
        title_rect = title_surf.get_rect(midtop = self.rect.midtop + pygame.math.Vector2(0,20))

        cost_surf = self.font.render(f'{int(cost)}',False,color)
        cost_rect = cost_surf.get_rect(midbottom = self.rect.midbottom - pygame.math.Vector2(0,20))

        surface.blit(title_surf,title_rect)
        surface.blit(cost_surf,cost_rect)

    def display_bar(self,surface,value,max_value,selected):
        # Dibuja la barra de progreso del atributo
        top = self.rect.midtop + pygame.math.Vector2(0,60)
        bottom = self.rect.midbottom - pygame.math.Vector2(0,60)
        color = BAR_COLOR_SELECTED if selected else BAR_COLOR

        full_height = bottom[1] - top[1]
        relative_number = (value / max_value) * full_height
        value_rect = pygame.Rect(top[0] - 15,bottom[1] - relative_number,30,10)

        pygame.draw.line(surface,color,top,bottom,5)
        pygame.draw.rect(surface,color,value_rect)

    def trigger(self,player):
        # Lógica para mejorar el atributo si el jugador tiene suficiente experiencia y no ha llegado al máximo
        upgrade_attribute = list(player.stats.keys())[self.index]

        if player.exp >= player.upgrade_cost[upgrade_attribute] and player.stats[upgrade_attribute] < player.max_stats[upgrade_attribute]:
            player.exp -= player.upgrade_cost[upgrade_attribute]
            player.stats[upgrade_attribute] *= 1.2
            player.upgrade_cost[upgrade_attribute] *= 1.4

        # Asegura que el atributo no supere su valor máximo
        if player.stats[upgrade_attribute] > player.max_stats[upgrade_attribute]:
            player.stats[upgrade_attribute] = player.max_stats[upgrade_attribute]

    def display(self,surface,selection_num,name,value,max_value,cost):
        # Dibuja el fondo del ítem según si está seleccionado o no
        if self.index == selection_num:
            pygame.draw.rect(surface,UPGRADE_BG_COLOR_SELECTED,self.rect)
            pygame.draw.rect(surface,UI_BORDER_COLOR,self.rect,4)
        else:
            pygame.draw.rect(surface,UI_BG_COLOR,self.rect)
            pygame.draw.rect(surface,UI_BORDER_COLOR,self.rect,4)
    
        self.display_names(surface,name,cost,self.index == selection_num)
        self.display_bar(surface,value,max_value,self.index == selection_num)