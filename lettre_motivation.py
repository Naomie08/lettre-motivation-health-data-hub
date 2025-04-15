class Candidate:
    def __init__(self):
        self.name = "Naomie"
        self.background = [
            "cadre de santé",
            "médico-social",
            "gestion d'équipe",
            "approche humaine du soin"
        ]
        self.skills = [
            "empathie",
            "résilience",
            "coordination",
            "apprentissage autonome"
        ]
        self.learning_curve = [
            "autoformation IA",
            "éthique des algorithmes",
            "python débutant",
            "vision centrée humain"
        ]
        self.objective = "Créer des ponts entre intelligence artificielle et intelligence humaine"

    def motivation(self):
        if "humain" in self.background and "technologie" in self.learning_curve:
            return "Utiliser mon vécu pour guider l’IA vers un impact humain, éthique et utile"
        else:
            return "Continuer à apprendre et explorer le champ de l’IA avec sens et engagement"

    def __str__(self):
        return f"Candidature spontanée de {self.name} – à la croisée des chemins entre soin et technologie"

def join_health_data_hub(candidate):
    if candidate.motivation():
        print(f"{candidate.name} souhaite rejoindre le Health Data Hub pour :")
        print(f"> {candidate.motivation()}")
        print("Elle ne vient pas du code, elle vient du réel. Et c’est exactement pour ça qu’elle a sa place ici.")
        print("Contact : naomie@exemple.com")
    else:
        print("Candidate en apprentissage, mais plus motivée que jamais.")

# Main
if __name__ == "__main__":
    naomie = Candidate()
    print(naomie)
    join_health_data_hub(naomie)
