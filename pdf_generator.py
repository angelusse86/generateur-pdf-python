from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

document = SimpleDocTemplate("rapport.pdf")

styles = getSampleStyleSheet()

contenu = []

contenu.append(Paragraph("Rapport Python", styles["Title"]))
contenu.append(Spacer(1, 12))

contenu.append(
    Paragraph(
        "Ce document a été généré automatiquement avec Python.",
        styles["BodyText"]
    )
)

document.build(contenu)

print("PDF créé avec succès.")

contenu.append(
    Paragraph(
        "Auteur : Seb Las",
        styles["BodyText"]
    )
)

from datetime import datetime

date_du_jour = datetime.now().strftime("%d/%m/%Y")

contenu.append(
    Paragraph(
        f"Date : {date_du_jour}",
        styles["BodyText"]
    )
)
