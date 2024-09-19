#TODO: Analyser la chaîne de caractères saisie et compter le nombre de médailles.
#      Attention si la chaîne est invalide, un message d'erreur est attendu.

#country = input("Résultat du pays : ")
#code_medals = ["G", "S", "", "B"]

def getCharCounts(char, sequence) -> tuple :
    count = 0

    for caractere in sequence :
        if char.lower() == caractere.lower() or char.upper() == caractere.upper() :
            count += 1

    return count

country = input("Pays concerné ? ")
sequence = input("Chaine représentant les médailles ? ")
code_medals = ["G", "S", "B"]

wrongSequence = False

for char in sequence :
    if char not in code_medals :
        wrongSequence = True
        print("Ceci est une chaine invalide.")

if not wrongSequence :
    countGold = getCharCounts(code_medals[0], sequence)
    countSilver = getCharCounts(code_medals[1], sequence)
    countBronze = getCharCounts(code_medals[2], sequence)

    exit = f"{country}:\n- {countGold} Or\n- {countSilver} Argent\n- {countBronze} Bronze"
    print(exit)