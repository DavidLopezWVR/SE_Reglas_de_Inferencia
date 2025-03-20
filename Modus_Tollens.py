def modus_tollens(Q, P_implies_Q):
    if not Q and P_implies_Q:
        return False  # P es falso
    return None  # No podemos concluir nada

# Premisas
Q = False  # No hay humo
P_implies_Q = True  # Si hay fuego, hay humo

# Conclusión
P = modus_tollens(Q, P_implies_Q)
print(f"¿Hay fuego? {P}")  # False
