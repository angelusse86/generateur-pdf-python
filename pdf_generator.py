from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table
from reportlab.lib.styles import getSampleStyleSheet

document = SimpleDocTemplate("facture.pdf")
styles = getSampleStyleSheet()

contenu = []

contenu.append(Paragraph("Facture", styles["Title"]))
contenu.append(Spacer(1, 20))

contenu.append(Paragraph("Client : Entreprise Exemple", styles["BodyText"]))
contenu.append(Paragraph("Auteur : Seb Las", styles["BodyText"]))
contenu.append(Spacer(1, 20))

donnees = [
    ["Produit", "Quantité", "Prix"],
    ["Service Python", "1", "50 €"],
    ["Automatisation Excel", "1", "80 €"],
]

tableau = Table(donnees)
contenu.append(tableau)

contenu.append(Spacer(1, 20))
contenu.append(Paragraph("Total : 130 €", styles["Heading2"]))

document.build(contenu)

print("Facture PDF créée avec succès.")
