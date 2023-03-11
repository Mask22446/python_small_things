import numpy as np
import matplotlib.pyplot as plt

pmin, pmax, qmin, qmax = -2.5, 1.5, -2, 2
# c = p + iq и p меняется в диапозоне от pmin до pmax,
# а q от qmin до qmax
ppoints, qpoints = 200, 200
#размеры отображения в точках
max_iterations = 300
#ограничение итерации
infinity_border = 100
#дальше этого значения бесконечность

image = np.zeros((ppoints, qpoints))
#двумерный массив изначльно заполненый нулями в заданных границах

for ip, p in enumerate(np.linspace(pmin, pmax, ppoints)):
    for iq, q in enumerate(np.linspace(qmin, qmax, qpoints)):
        c = p + 1j * q
        #j это мнимая еденица: т.к. это комплексное число для восприятия
        #питоном записываем как 1j, а не j

        z = 0
        for k in range(max_iterations):
            z = z ** 2 + c
            #та самая формула

            if abs(z) > infinity_border:
                #если z ушла за предел, то считаем что уже ушла
                #либо уйдет в  бесконечность
                image[ip, iq] = 1
                break

plt.xticks([])
plt.yticks([])
#отключение меток на осях

plt.imshow(-image.T, cmap='Greys')
# транспонирование картинки для коретктного отображения осей
# перед image минус для отрисовки чёрным
plt.show()