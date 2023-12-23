import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from random import uniform
from random import randint
from random import gauss


class TGrass:
    def __init__(self, n0, NstarGrass, MaxGrassLength0):
        self.n = n0
        self.MaxGrassLength = MaxGrassLength0
        self.M = []
        for _ in range(n0):  # создаем матрицу
            self.M.append([0 for _ in range(n0)])

        for _ in range(NstarGrass):  # добавляем траву при старте
            self.M[randint(0, n0 - 1)][randint(0, n0 - 1)] = self.MaxGrassLength

    def grow(self, GrassPerStep):
        for _ in range(GrassPerStep):
            i = randint(0, self.n - 1)
            j = randint(0, self.n - 1)
            if self.M[i][j] < self.MaxGrassLength:
                self.M[i][j] += 1


class THare:
    def __init__(self, grass, x, y, bb):
        self.age = 0
        self.x = x
        self.y = y
        self.energy = 100
        self.grass = grass
        self.bb = bb

    def go(self):
        dx = uniform(-self.bb.maxHareJump, self.bb.maxHareJump)
        dy = uniform(-self.bb.maxHareJump, self.bb.maxHareJump)
        if self.x + dx > 1:
            self.x -= 2
        elif self.x + dx < -1:
            self.x += 2
        else:
            self.x += dx
        if self.y + dy > 1:
            self.y -= 2
        elif self.y + dy < -1:
            self.y += 2
        else:
            self.y += dy
        self.eat()
        self.rep()
        self.energy -= self.bb.EnergySpendingHare
        self.age += 1

    def eat(self):
        if self.energy < 100 - self.bb.hareGetsEnergyFromGrass:
            i = round((self.x + 1) * (self.grass.n - 1) / 2) - 1
            j = round((1 - self.y) * (self.grass.n - 1) / 2) - 1
            # print(i, j)
            if self.grass.M[i][j] > 0:
                self.grass.M[i][j] -= 1
                self.energy += self.bb.hareGetsEnergyFromGrass

    def rep(self):
        if self.age >= self.bb.ReproductionHareAge and self.energy >= self.bb.minHareEnergyToReproduce:
            n = round(gauss(self.bb.AverageBirthRate, 0.001))
            for i in range(n):
                self.bb.hares.append(THare(self.grass, self.x, self.y, self.bb))
                self.energy //= 2


class BB:
    def __init__(self):
        self.n = 15
        self.MaxGrassLength = 10
        self.NstarGrass = 100
        self.GrassPerStep = 10
        self.grass = TGrass(self.n, self.NstarGrass, self.MaxGrassLength)
        self.maxHareAge = 20  # максимальный ворзраст зайца
        self.ReproductionHareAge = 10  # - возраст для размножения
        self.AverageBirthRate = 2  # - средняя рождаемость
        self.hareGetsEnergyFromGrass = 20  # - const - количество прибавляемой энергии за травинку
        self.maxHareJump = 0.08  # - максимальное перемещение по оси
        self.EnergySpendingHare = 5  # - уменьшение энергии за ход
        self.minHareEnergyToReproduce = 80  # - минимальная величина энергии для размножения
        self.NstarHare = 10
        self.hares = []
        for i in range(self.NstarHare):
            self.hares.append(THare(self.grass, uniform(-1, 1), uniform(-1, 1), self))

    def draw(self):
        glBegin(GL_QUADS)

        for i in range(self.n):
            for j in range(self.n):
                h = 2 / self.n
                x = i * h - 1
                y = - j * h + 1
                glColor3fv((0, 1 / self.MaxGrassLength * self.grass.M[i][j], 0))
                glVertex3fv((x, y, 0))
                glVertex3fv((x + h, y, 0))
                glVertex3fv((x + h, y - h, 0))
                glVertex3fv((x, y - h, 0))
        glEnd()
        glBegin(GL_QUADS)
        for i in self.hares:
            h = 0.005 * i.age / 2
            glColor3fv((0.01 * i.energy, 0.01 * i.energy, 0.01 * i.energy))
            glVertex3fv((i.x - h, i.y + h, 0))
            glVertex3fv((i.x + h, i.y + h, 0))
            glVertex3fv((i.x + h, i.y - h, 0))
            glVertex3fv((i.x - h, i.y - h, 0))
        glEnd()

    def go(self):
        self.grass.grow(self.GrassPerStep)
        for i in self.hares:
            i.go()

        i = 0  # удаление мертвых зайцев
        while i < len(self.hares):
            if self.hares[i].age > self.maxHareAge or self.hares[i].energy <= 0:  #
                self.hares.pop(i)
            else:
                i += 1


pygame.init()
display = (800, 800)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
glTranslatef(0.0, 0.0, -2.8)
mb = BB()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    mb.draw()
    mb.go()
    print(len(mb.hares), sum([sum(i) for i in mb.grass.M]))
    pygame.display.flip()
    pygame.time.wait(100)
