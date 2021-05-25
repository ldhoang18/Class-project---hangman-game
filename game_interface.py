"""
Lam Hoang
Dai Nguyen
Project2 - Hangman

"""
import pygame
import os
import math
import random
from words import Words

allwords = Words()

class Game_Interface:
    
    """
    properties:
    - width, height of the screen
    - radius of the circle letter button, gap between each circle button
    - letters = [] to store letters that are later binded inside a circle button
    - hangman images = [] to store each hangman images based on the number.
    - letter_font displays the font and size of letters inside the circle button, word_font to display the whole word, 
      title_font to display the game title
    - hangman status = 0 where 0 (initially set) represent the index of the number indicated after "hangman" in each .png file 
    - guessed = [] to store each letter guesses.
    - black text, light_blue background, green and red game-over buttons

    """
    def __init__(self):
        self.width = 900
        self.height = 600
        self.radius = 20
        self.gap = 15
        self.frame_per_second = 60
        self.hangman_status = 0
        self.light_blue = (230, 249, 255)
        self.black = (0, 0, 0)
        self.green = (102, 255, 194)
        self.red = (255, 102, 102)
        self.letters = []
        self.hangman_images = []
        self.guessed = []
        self.random_word = random.choice(allwords.words)

        #initialize pygame and setting the width and height of the screen
        pygame.init()  
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Hangman Game")

        #displaying letters to the screen, later bind them inside a button. There are 26 alphabets, so we will have 2 rows of 13 each
        #x, y: x-y coordinate to place each letter in an appropriate position based on radius, gap, and initial xstart-ystart coordinate
        #Boolean value True indicates a letter being visible/seen in the interface
        xstart = round((self.width - (self.radius * 2 + self.gap) * 13) / 2)
        ystart = 400
        A = 65
        for i in range(26):
            x = xstart + self.gap * 2 + ((self.radius * 2 + self.gap) * (i % 13))  #i mod 13 will use counter i to create a row up to 13
            y = ystart + ((i // 13) * (self.gap + self.radius * 2))
            self.letters.append([x, y, chr(A + i), True])

        #loading hangman stages with images
        for img in range(8):
            selected_img = pygame.image.load("hangman" + str(img) + ".PNG")
            self.hangman_images.append(selected_img)

        #initialize letter fonts
        self.letter_font = pygame.font.SysFont('arial', 40)
        self.word_font = pygame.font.SysFont('arial', 40)
        self.title_font = pygame.font.SysFont('arial', 60)
        self.button_font = pygame.font.SysFont('bigNoodleTooOblique', 30)              
        self.message_font = pygame.font.SysFont('arial', 40)
        self.correct_word_font = pygame.font.SysFont('arial', 35)

    def draw(self):

        """
        Draw the design of the graphic to the screen

        ---------------------------------------------

        Pygame techniques:
        - screen.fill(color) - fill the background screen with color
        - pygame.font.SysFont.render(text, visible/seen?, color): display content of the text
        - screen.blit(text, (x-y coordinate)): display this text at an assigned position in the interface
        - pygame.draw.circle(screen_window, color, (x, y), radius, border_thickness): draw a circle in pygame. 
        Thickness = 0 means the circle is colored, < 0 means there is no border, and > 0 means there is border depending on thickness level
        - pygame.transform.scale: Adjust the size of an object in pygame
        - pygame.display.update: update the display into the light blue screen 

        """
        self.screen.fill(self.light_blue)

        #draw TITLE_FONT
        title_text = self.title_font.render("HANGMAN", 1, self.black)
        self.screen.blit(title_text, (self.width/2 - title_text.get_width()/2, 20))

        #draw word
        display_word = ""
        for letter in self.random_word:
            if letter in self.guessed:
                display_word += letter + " "
            else:
                display_word += "_ "
        word_text = self.word_font.render(display_word, 1, self.black)
        self.screen.blit(word_text, (400, 200))

        #draw letter buttons
        for letter in self.letters:
            x, y, ltr, seen = letter
            if seen: 
                pygame.draw.circle(self.screen, self.black, (x, y), self.radius, -1)
                letter_text = self.letter_font.render(ltr, 1, self.black)
                self.screen.blit(letter_text, (x - letter_text.get_width()/2, y - letter_text.get_height()/2))
        self.screen.blit(pygame.transform.scale(self.hangman_images[self.hangman_status], (200, 200)), (90, 150))

        pygame.display.update()     

    def display_game_over_message(self, message):

        """
        Display messages after playing the game

        ---------------------------------------
        Pygame techniques
        - screen.fill(color) - fill the background screen with color
        - pygame.font.SysFont.render(text, visible/seen?, color): display content of the text
        - screen.blit(text, (x-y coordinate)): display this text at an assigned position in the interface
        - pygame.display.update: update the display into the light blue screen 
        - pygame.time.delay(miliseconds) - will pause/delay an interface for an amount of time

        """
        pygame.time.delay(1000)
        self.screen.fill(self.light_blue)
        message_text = self.message_font.render(message, 1, self.black)
        self.screen.blit(message_text, [290, 200])
        correct_word = self.correct_word_font.render("The word is: %s" % self.random_word, 1, self.black)
        self.screen.blit(correct_word, [300, 250])
        pygame.display.update()
        pygame.time.delay(3000)     #see this text in 3 seconds

    def text_object_for_button(self, text, font): 

        """
        create a text that will be used for button
        ------------------------------------------
        Method:
        font.render.get_rect(): build a rectangle block to place text within its area.
        ------------------------------------------
        Returns: the text and its boundaries

        """
        textDetail = font.render(text, True, self.black)
        return textDetail, textDetail.get_rect()

    def button(self, message, x, y, rect_width, rect_height, inactive_color):   #, message2, x2, y2, rect_width2, rect_height2 action=None, active_color
        
        """
        utilizing text_object_for_button to set up the button. Text will be placed at the center of the button
        ------------------------------------------------------------------
        Returns: The updated screen display of the buttons

        """
        pygame.draw.rect(self.screen, inactive_color, (x, y, rect_width, rect_height))
        textSurface, textContent = self.text_object_for_button(message, self.button_font)
        textContent.center = ((x + (rect_width/2)), (y + (rect_height/2)))
        return self.screen.blit(textSurface, textContent)  

    def reset(self):

        """
        Reset the properties initially set after the game is over

        """
        self.hangman_status = 0
        self.letters = []
        self.hangman_images = []
        self.guessed = []
        self.random_word = random.choice(allwords.words)

        xreset = round((self.width - (self.radius * 2 + self.gap) * 13) / 2)
        yreset = 400
        A = 65
        for i in range(26):
            x = xreset + self.gap * 2 + ((self.radius * 2 + self.gap) * (i % 13))  #i mod 13 will use counter i to create a row up to 13
            y = yreset + ((i // 13) * (self.gap + self.radius * 2))
            self.letters.append([x, y, chr(A + i), True])

        for img in range(8):
            selected_img_reset = pygame.image.load("hangman" + str(img) + ".PNG")
            self.hangman_images.append(selected_img_reset)

    def hangman_game_loop(self):

        """
        Runs the hangman game. When the game is over, it displays the message and switch to button screen.

        """
        clock = pygame.time.Clock()
        running = True
        while running:
            clock.tick(self.frame_per_second)    #tick at the speed of FPS (frame per second)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    for letter in self.letters:
                        x, y, ltr, seen = letter
                        if seen:
                            distance = math.sqrt((x - mouse_x)**2 + (y - mouse_y)**2)
                            if distance < self.radius:
                                letter[3] = False
                                self.guessed.append(ltr)
                                if ltr not in self.random_word:
                                    self.hangman_status += 1

            self.draw()

            won = True
            for letter in self.random_word:
                if letter not in self.guessed:
                    won = False
                    break

            if won:
                self.display_game_over_message("YOU WIN! Top job, mate!")
                break

            if self.hangman_status == 7:
                self.display_game_over_message("YOU LOSE! Pathetic...")
                break
            
        self.play_again_or_quit()

    def play_again_or_quit(self):

        """

        Display a screen containing 2 buttons: one for playing again (1) and one for quitting (2)
        If (1) is selected, the screen is switched back to the game interface
        Otherwise, you exit the game.

        """
        self.screen.fill(self.light_blue)
        play_again = self.button("ONE MORE ROUND, BRUH?", 200, 250, 250, 50, self.green)
        quit_game = self.button("ENOUGH, BRUH?", 500, 250, 200, 50, self.red)
        button_running = True       
        while button_running:          
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    button_running = False
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0]:
                        if play_again.collidepoint(pygame.mouse.get_pos()):
                            self.reset()
                            self.hangman_game_loop()
                        if quit_game.collidepoint(pygame.mouse.get_pos()):
                            pygame.quit()
                            quit()
            pygame.display.update()

def hangman():

    """
    Calls methods necessary to play hangman
    
    """
    hangman_game = Game_Interface()
    hangman_game.hangman_game_loop()
    hangman_game.play_again_or_quit()

if __name__ == '__main__':
    hangman()