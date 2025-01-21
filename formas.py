
import turtle

esguicho = turtle.Turtle()

# definindo as funções
def desenhe_forma():
    for _ in range(6):
        esguicho.forward(25)
        esguicho.right(90)

def pule(pixels):
    esguicho.penup()
    esguicho.forward(pixels)
    esguicho.pendown()


# Aqui é o código principal
for _ in range(6):
    for _ in range(2):
        for _ in range(4):
            desenhe_forma()
            pule(80)
        pule(-25)
        esguicho.right(60)
        pule(25)
        esguicho.right(130)
    pule(-25)
    esguicho.left(50)
    pule(50)
    esguicho.right(50)