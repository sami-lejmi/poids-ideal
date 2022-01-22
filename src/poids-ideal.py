# Indice de masse corporelle (IMC) ou indice de Quetelet
def imc(t: float, p: float) -> float:
    r = p / t ** 2
    return round(r, 1)


# Formule de Broca
def broca(t: float) -> float:
    p = t - 100
    return round(p, 3)


# Formules de Lorentz
def lorentz(t: float, s: str) -> float:
    if s == "m":
        p = t - 100 - (t - 150) / 4
    elif s == "f":
        p = t - 100 - (t - 150) / 2.5
    else:
        raise ValueError("function lorentz() : error using arguments")
    return round(p, 3)


# Formules de Devine
def devine(t: float, s: str) -> float:
    if s == "m":
        p = 50 + 2.3 * (t - 60)
    elif s == "f":
        p = 45.5 + 2.3 * (t - 60)
    else:
        raise ValueError("function devine() : error using arguments")
    return round(p, 3)


# Formule de Perrault
def perrault(t: float, a: float) -> float:
    p = t - 100 + a / 10 * 0.9
    return round(p, 3)


# Formule de Creff
def creff(t: float, a: float, m: str = "normale") -> float:
    if m == "normale":
        p = (t - 100 + a / 10) * 0.9
    elif m == "large":
        p = (t - 100 + a / 10 * 0.9) * 1.1
    elif m == "gracile":
        p = (t - 100 + a / 10 * 0.9) * 0.9
    else:
        raise ValueError("function creff() : error using arguments")
    return round(p, 3)


# Formule de Monnerot-Dumaine
def monnerot_dumaine(t: float, c: float) -> float:
    p = (t - 100 + 4 * c) / 2
    return round(p, 3)


# Formule de Bornhardt
def bornhardt(t: float, c: float) -> float:
    p = t * c / 240
    return round(p, 3)


def main():
    pass


if __name__ == "__main__":
    main()
