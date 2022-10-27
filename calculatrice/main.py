def calculatrice():
    calcul = input('Veuillez entrer votre calcul: ')

    result = exe_calcul(calcul)
    if result:
        print("Le résultat est:  " + str())
    else:
        print("Calcul invalide")


def exe_calcul(calcul):
    try:
        return eval(calcul)
    except:
        return False


def main():
    calculatrice()


if __name__ == '__main__':
    main()
