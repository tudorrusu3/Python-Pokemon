import citire
import matplotlib.pyplot as plt
import seaborn as sns

def genereaza_statistici_si_grafice(file_path):
    # Încarcă setul de date și tratează datele
    df = citire.incarca_date(file_path)
    df_tratat = citire.tratare_date(df)

    # Afișează statistici descriptive
    print("Statistici descriptive:")
    print(df_tratat.describe())

    # Grafice

    # Histograma pentru distribuția vitezei (Speed)
    plt.figure(figsize=(10, 6))
    sns.histplot(df_tratat['Speed'], bins=20, kde=True, color='skyblue')
    plt.title('Distribuția Vitezei Pokemon')
    plt.xlabel('Viteză')
    plt.ylabel('Număr de Pokemon')
    plt.show()

    # Diagrama de cutie pentru statistici de bază (HP, Attack, Defense)
    plt.figure(figsize=(12, 8))
    sns.boxplot(data=df_tratat[['HP', 'Attack', 'Defense']])
    plt.title('Statistici de Bază pentru HP, Attack, și Defense')
    plt.xlabel('Statistici de Bază')
    plt.ylabel('Valoare')
    plt.show()

    # Corelații între atribute numerice
    numeric_columns = df_tratat.select_dtypes(include=['number']).columns
    correlation_matrix = df_tratat[numeric_columns].corr()

    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Matrice de Corelație între Atributele Pokemon')
    plt.show()

    # Adăugăm logica pentru a permite navigarea la următoarea etapă sau să ieșim
    alegere = input("Doriți să vedeți următoarea etapă? (da/nu): ").lower()
    if alegere == 'da':
        # Adăugați aici codul pentru următoarea etapă sau set de date
        print("Implementați aici următoarea etapă sau set de date.")
    else:
        print("Programul se încheie.")

# Apelul funcției pentru generarea statisticilor și a graficelor
if __name__ == "__main__":
    file_path = 'Pokemon.csv'
    genereaza_statistici_si_grafice(file_path)