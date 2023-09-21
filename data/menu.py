import pygame as pg

class Menu:
    def __init__(self, screen_rect):
        self.screen_rect = screen_rect
        self.font_init(self.screen_rect)
         
    def font_init(self, screen_rect):
        self.text_size = 15
        self.text_color = (255,255,255)
        self.font = pg.font.SysFont('Arial', self.text_size)
         
    def make_text(self, message, pos):
        text = self.font.render(message,True,self.text_color)
        rect = text.get_rect(topleft=pos)
        return text, rect
         
    def draw(self):
        pass
        
class GameOverText(Menu):
    def __init__(self, screen_rect):
        super().__init__(screen_rect)
        self.screen_rect = screen_rect
        self.game_over()
    def draw(self,surf):
        surf.blit(self.game_over_text, self.game_over_rect)
    def game_over(self):
        game_over_font = pg.font.SysFont('Arial', 45)
        self.game_over_text = game_over_font.render('Game Over',True,(255,0,0))
        self.game_over_rect = self.game_over_text.get_rect(center=self.screen_rect.center)
        
class TopLeftText(Menu):
    def __init__(self, pos, msg, arg, screen_rect):
        super().__init__(screen_rect)
        self.pos = pos
        self.msg = msg
        self.update()
    def update(self, arg=None):
        self.damage, self.damage_rect = self.make_text(self.msg.format(arg), self.pos)
    def draw(self, surf):
        surf.blit(self.damage, self.damage_rect)

class MainMenu(Menu):
    def __init__(self, screen_size, arg, screen_rect):
        super().__init__(screen_rect)
        self.screen_size = screen_size
        self.main()
    def update(self, arg=None):
        self.quite, self.quit_button = self.make_text('quit', (0, self.screen_size/100))
        self.pausee, self.pause_button = self.make_text('pause', (0, self.screen_size/50))
    def draw(self, surf):
        surf.blit(self.quit_button_text, self.quit_button_rect)    
    def main(self):
        quit_button_font = pg.font.SysFont('Arial', 15)
        pause_button_font = pg.font.SysFont('Arial', 15)
        self.quit_button_text = quit_button_font.render('Quit',True,(0,0,0))
        self.quit_button_rect = self.quit_button_text.get_rect(center = ((self.screen_size/50)+20,self.screen_size/100))

class Button:
    """Create a button, then blit the surface in the while loop"""
    def __init__(self, screen, text,  pos, font, bg="black", feedback=""):
        self.x, self.y = pos
        self.screen = screen
        self.font = pg.font.SysFont("Arial", font)
        if feedback == "":
            self.feedback = "text"
        else:
            self.feedback = feedback
        self.change_text(text, bg)
    def change_text(self, text, bg="black"):
        """Change the text whe you click"""
        self.text = self.font.render(text, 1, pg.Color("White"))
        self.size = self.text.get_size()
        self.surface = pg.Surface(self.size)
        self.surface.fill(bg)
        self.surface.blit(self.text, (0, 0))
        self.rect = pg.Rect(self.x, self.y, self.size[0], self.size[1])
    def show(self):
        self.screen.blit(button1.surface, (self.x, self.y))
    def click(self, event):
        x, y = pg.mouse.get_pos()
        if event.type == pg.MOUSEBUTTONDOWN:
            if pg.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    self.change_text(self.feedback, bg="red")



