
import matplotlib.pyplot as plt

# Pedir las coordenadas #
xA = float(input("x de A: "))
yA = float(input("y de A: "))
xB = float(input("x de B: "))
yB = float(input("y de B: "))
xC = float(input("x de C: "))
yC = float(input("y de C: "))

# Translacion
dx = float(input("dx: "))
dy = float(input("dy: "))
xA_t = xA + dx
yA_t = yA + dy
xB_t = xB + dx
yB_t = yB + dy
xC_t = xC + dx
yC_t = yC + dy

# Escalado
sx = float(input("Factor de escala X: "))
sy = float(input("Factor de escala Y: "))
xA_e = xA * sx
yA_e = yA * sy
xB_e = xB * sx
yB_e = yB * sy
xC_e = xC * sx
yC_e = yC * sy


# Dibujar triángulo original
# Triángulo original
plt.plot(
    [xA, xB, xC, xA],
    [yA, yB, yC, yA],
    color="blue",
    label="Original"
)

# Triángulo trasladado
plt.plot(
    [xA_t, xB_t, xC_t, xA_t],
    [yA_t, yB_t, yC_t, yA_t],
    color="green",
    label="Trasladado"
)

# Triángulo escalado
plt.plot(
    [xA_e, xB_e, xC_e, xA_e],
    [yA_e, yB_e, yC_e, yA_e],
    color="red",
    label="Escalado"
)

# Configuración de la gráfica

plt.title("Transformaciones 2D")

plt.xlabel("Eje X")

plt.ylabel("Eje Y")

plt.grid(True)

plt.legend()

plt.axhline(0)

plt.axvline(0)

plt.show()

