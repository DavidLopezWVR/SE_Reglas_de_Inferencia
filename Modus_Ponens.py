def modus_ponens(P, P_implies_Q):
    if P and P_implies_Q:
        return True  # Q es verdadero
    return False  # No podemos concluir Q

# Premisas
P = True  # Está lloviendo
P_implies_Q = True  # Si llueve, el suelo se moja

# Conclusión
Q = modus_ponens(P, P_implies_Q)
print(f"¿El suelo está mojado? {Q}")  # True
