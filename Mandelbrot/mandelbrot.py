import numpy as np
import matplotlib.pyplot as plt


# Re: real axis
# Im: imaginary axis
def mandelbrot(real, imag, max_iter):
    c = complex(real, imag)
    z = 0.0j

    for i in range(max_iter):
        z = z * z + c
        if (z.real * z.real + z.imag * z.imag) >= 4:
            return i

    return max_iter


columns = 2000
rows = 2000
result = np.zeros([rows, columns])
for row_index, re in enumerate(np.linspace(-2, 1, num=rows)):
    for column_index, im in enumerate(np.linspace(-1, 1, num=columns)):
        result[row_index, column_index] = mandelbrot(re, im, 100)

plt.figure()
# you might want to change the colormap https://matplotlib.org/3.1.0/tutorials/colors/colormaps.html
plt.imshow(result.T, cmap='twilight_shifted', interpolation='bilinear', extent=[-2, 1, -1, 1])
plt.axis("off")
plt.savefig('mandelbrot.png', bbox_inches='tight', pad_inches=0)
plt.show()
