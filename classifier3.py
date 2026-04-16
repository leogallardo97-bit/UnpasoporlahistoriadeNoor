import os
import shutil

directories = [
    r"C:\Users\leoga\Desktop\Noor\Estudio Zotero Por Siglos\Siglo Xll",
    r"C:\Users\leoga\Desktop\Noor\Estudio Zotero Por Siglos\Siglo Xlll"
]

categories = ["Económico", "Social", "Cultural", "Político"]

for base_dir in directories:
    if not os.path.exists(base_dir):
        print(f"Directory not found: {base_dir}")
        continue
        
    for cat in categories:
        os.makedirs(os.path.join(base_dir, cat), exist_ok=True)

    for file in os.listdir(base_dir):
        if not file.lower().endswith(".pdf"):
            continue

        cats = set()
        name = file.lower()

        # Económico / Economic
        if any(k in name for k in ["economic", "economy", "coin", "dirham", "mint", "commerce", "trade", "market", "tariff", "export", "treasure", "agricultural", "agriculture", "agrarian", "rural", "irrigation", "glass", "metallurgy", "production", "hoard", "almojarifazgo", "merchants", "artisans", "farming", "crop", "supply", "económico", "comercio", "producción"]):
            cats.add("Económico")
            
        # Social
        if any(k in name for k in ["social", "society", "peasant", "gender", "urban", "settlement", "slavery", "migration", "population", "domestic", "communities", "cities", "evolution", "urbanism", "food", "dietary", "slaves", "eunuchs", "concubines", "children", "arrabal", "alimentacion", "alimentación", "consumo", "población"]):
            cats.add("Social")
            
        # Político / Political
        if any(k in name for k in ["power", "state", "conquest", "uprising", "revolt", "caliphate", "caliphal", "diplomacy", "policy", "border", "military", "fort", "castle", "fortress", "frontier", "legitimation", "sovereignty", "rebel", "succession", "king", "ruler", "jihad", "piracy", "hegemony", "battle", "campaign", "emirate", "court", "politi", "guerra", "poder", "rey", "califa", "alcazar", "alcazaba"]):
            cats.add("Político")
            
        # Cultural
        if any(k in name for k in ["religion", "visual", "architecture", "architectural", "church", "basilica", "poem", "poetry", "literature", "translation", "hebrew", "jewelry", "ivory", "islamic", "islamisation", "mosque", "art", "heritage", "cross", "martyr", "education", "school", "science", "scientific", "book", "culture", "cultural", "poetic", "civilization", "sacred", "sanctuary", "burial", "funerary", "inscription", "epigraphy", "mezquita", "arte", "literatura", "religión", "mito"]):
            cats.add("Cultural")

        # Specific multi-category topics
        if "food" in name or "gastronomy" in name or "alimentación" in name or "cooking" in name or "dietary" in name or "sugar" in name or "consumption" in name:
            cats.update(["Social", "Cultural", "Económico"])
            
        if "water" in name or "hydraulic" in name or "irrigation" in name:
            cats.update(["Económico", "Social"])
            
        if "tax" in name or "almojarifazgo" in name:
            cats.update(["Económico", "Político"])

        if "archaeology" in name or "archaeological" in name or "site" in name or "excavation" in name or "ceramicas" in name or "ceramics" in name or "pottery" in name or "glaze" in name:
            cats.update(["Cultural", "Social", "Económico"])

        if "identit" in name or "identidad" in name or "tradition" in name:
            cats.update(["Cultural", "Social"])

        # Fallback
        if not cats:
            cats.add("Cultural")

        src = os.path.join(base_dir, file)
        if os.path.isfile(src):
            for cat in cats:
                dst = os.path.join(base_dir, cat, file)
                shutil.copy2(src, dst)
    print(f"Processed {base_dir}")
