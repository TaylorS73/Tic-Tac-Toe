

#if player wins crowd celebration activates
cheering_sound = pygame.mixer.Sound("SMALL_CROWD_APPLAUSE-Yannick_Lemieux-1268806408.wav")


#if player loses sad music plays
sadViolin_sound = pygame.mixer.Sound("Sad_Violin.wav")


#background music to the game
pygame.mixer.music.load("KabookiZ - Beach House [Chill Trap Release].mp3")


def cheering():
    pygame.mixer.music.stop()
    pygame.mixer.sound.play(cheering_sound)



def SadViolin():
    pygame.mixer.music.stop()
    pygame.mixer.sound.play(sadViolin_sound)


#music will play on a loop
pygame.mixer.music.play(-1)

