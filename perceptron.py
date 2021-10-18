import random

class Perceptron():
    def __init__(self, cant_w, c):

        # tasa de aprendizaje
        self.c = c

        # asignacion aleatoria de los pesos
        self.w = [random.random() for i in range(cant_w)]

        # asignacion aleatoria del umbral de disparo
        self.h = random.random()


    def process_input(self, *x):

        # calculo de la variable auxiliar
        netj = sum([i[0] * i[1] for i in zip(self.w,x)])

        # funcion de respuesta
        sj = self.f(netj)

        return sj

    # definicion de la funcion de respuesta (funcion escalon)
    def f(self, netj):
        if netj >= self.h:
            return 1
        elif netj < self.h:
            return 0

    # compara sus resultados con resultados correctos basado en un input
    def learn(self, inputs, results):
        for i in range(len(inputs)):
            s = self.process_input(*inputs[i])
            if s == results[i]:
                pass
            else:
                self.change_weights(inputs[i], s, results[i])

    def change_weights(self, inputs, S, R):
        # regla del aprendizaje para cada peso
        for i in range(len(self.w)):
            self.w[i] = self.w[i] + self.c * (R-S) * inputs[i]


def main():

    p = Perceptron(3, 0.1)

    inputs = [
        (1, 0, 0),
        (1, 0, 1),
        (1, 1, 0),
        (1, 1, 1),

    ]

    results_or = [
        0,
        1,
        1,
        1,
    ]

    results_and = [
        0,
        0,
        0,
        1,
    ] 

    p.learn(inputs*100, results_or*100)

    print(p.process_input(1, 0, 0))
    print(p.process_input(1, 0, 1))
    print(p.process_input(1, 1, 0))
    print(p.process_input(1, 1, 1))
    print(p.process_input(1, 0, 0))



main()



# pregunta de examen
# que constante c se toma 