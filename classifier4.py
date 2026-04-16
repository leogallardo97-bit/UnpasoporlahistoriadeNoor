import os
import shutil

directories = [
    r"C:\Users\leoga\Desktop\Noor\Estudio Zotero Por Siglos\Siglo XlV",
    r"C:\Users\leoga\Desktop\Noor\Estudio Zotero Por Siglos\Siglo XV",
    r"C:\Users\leoga\Desktop\Noor\Estudio Zotero Por Siglos\Siglo XVl",
    r"C:\Users\leoga\Desktop\Noor\Estudio Zotero Por Siglos\Siglo XVll",
    r"C:\Users\leoga\Desktop\Noor\Estudio Zotero Por Siglos\Siglo XVlll",
    r"C:\Users\leoga\Desktop\Noor\Estudio Zotero Por Siglos\Siglo XVllll- XlX"
]

categories = ["Económico", "Social", "Cultural", "Político"]

for base_dir in directories:
    if not os.path.exists(base_dir):
        print(f"[!] Directory not found: {base_dir}")
        continue

    for cat in categories:
        os.makedirs(os.path.join(base_dir, cat), exist_ok=True)

    count = 0
    for file in os.listdir(base_dir):
        if not file.lower().endswith(".pdf"):
            continue

        cats = set()
        name = file.lower()

        # ─── ECONÓMICO ───────────────────────────────────────────────────────────
        if any(k in name for k in [
            "economic", "economy", "coin", "dirham", "mint", "commerce", "trade",
            "market", "tariff", "export", "import", "treasure", "agricultural",
            "agriculture", "agrarian", "rural", "irrigation", "metallurgy",
            "production", "hoard", "almojarifazgo", "merchants", "artisans",
            "farming", "crop", "supply", "financial", "fiscal", "tribute",
            "tax", "revenue", "silk", "textile", "wool", "guild", "labor",
            "manufacture", "industry", "price", "wage", "land", "property",
            "económico", "comercio", "producción", "recursos", "hacienda",
            "moneda", "riqueza", "colonization", "plantation", "sugar", "spice",
            "silver", "gold", "wealth", "poverty", "famine", "grain"
        ]):
            cats.add("Económico")

        # ─── SOCIAL ──────────────────────────────────────────────────────────────
        if any(k in name for k in [
            "social", "society", "peasant", "gender", "urban", "settlement",
            "slavery", "slave", "migration", "population", "domestic",
            "communities", "community", "cities", "city", "evolution", "urbanism",
            "food", "dietary", "diet", "eunuchs", "concubines", "children",
            "arrabal", "alimentacion", "alimentación", "consumo", "población",
            "family", "marriage", "women", "men", "class", "status", "poor",
            "elite", "nobility", "peasantry", "serfdom", "serf", "freedom",
            "disease", "plague", "health", "medicine", "hospital", "census",
            "demography", "demographic", "housing", "neighbourhood", "mosque",
            "jews", "jewish", "muslim", "christian", "minority", "conversion",
            "ethnic", "race", "identity", "morisco", "converso", "mudéjar"
        ]):
            cats.add("Social")

        # ─── POLÍTICO ────────────────────────────────────────────────────────────
        if any(k in name for k in [
            "power", "state", "conquest", "uprising", "revolt", "caliphate",
            "caliphal", "diplomacy", "diplomatic", "policy", "border", "military",
            "fort", "castle", "fortress", "frontier", "legitimation", "legitimacy",
            "sovereignty", "rebel", "rebellion", "succession", "king", "ruler",
            "queens", "jihad", "crusade", "piracy", "hegemony", "battle",
            "campaign", "emirate", "court", "politi", "guerra", "poder", "rey",
            "califa", "alcazar", "alcazaba", "sultan", "empire", "imperial",
            "republic", "republic", "parliament", "cortes", "treaty", "war",
            "peace", "alliance", "election", "governance", "government",
            "administration", "inquisition", "expulsion", "reconquista",
            "crusade", "ottoman", "habsburgo", "habsburgs", "bourbon",
            "revolution", "independence", "constitution", "liberal", "colonial",
            "colonialism", "colony", "colonial"
        ]):
            cats.add("Político")

        # ─── CULTURAL ────────────────────────────────────────────────────────────
        if any(k in name for k in [
            "religion", "religious", "visual", "architecture", "architectural",
            "church", "basilica", "poem", "poetry", "literature", "translation",
            "hebrew", "jewelry", "ivory", "islamic", "islamisation", "mosque",
            "art", "arts", "heritage", "cross", "martyr", "martyrdom",
            "education", "school", "science", "scientific", "book", "culture",
            "cultural", "poetic", "civilization", "sacred", "sanctuary",
            "burial", "funerary", "inscription", "epigraphy", "paint",
            "painting", "music", "theatre", "theater", "manuscript", "codex",
            "philosophy", "theology", "mysticism", "sufism", "belief", "ritual",
            "ceremony", "feast", "festival", "myth", "legend", "narrative",
            "chronicle", "biography", "hagiography", "saint", "relic",
            "pilgrimage", "cathedral", "convent", "monastery", "synagogue",
            "humanist", "humanism", "renaissance", "baroque", "enlightenment",
            "reform", "reformation", "printing", "press", "university",
            "gastronomic", "gastronomy", "recipe", "culinary", "cooking",
            "mezquita", "arte", "literatura", "religión", "mito", "cultura",
            "saber", "filosof"
        ]):
            cats.add("Cultural")

        # ─── MULTI-CATEGORY OVERRIDES ─────────────────────────────────────────────
        if any(k in name for k in ["food", "gastronomy", "alimentación", "alimentacion", "cooking", "dietary", "diet", "sugar", "consumption", "recipe", "culinary"]):
            cats.update(["Social", "Cultural", "Económico"])

        if any(k in name for k in ["water", "hydraulic", "irrigation", "canal", "river"]):
            cats.update(["Económico", "Social"])

        if any(k in name for k in ["tax", "tribute", "almojarifazgo", "fiscal", "revenue"]):
            cats.update(["Económico", "Político"])

        if any(k in name for k in ["archaeology", "archaeological", "excavation", "ceramica", "ceramics", "pottery", "glaze", "material culture", "artefact", "artifact"]):
            cats.update(["Cultural", "Social", "Económico"])

        if any(k in name for k in ["identit", "identidad", "tradition", "memory", "memoria"]):
            cats.update(["Cultural", "Social"])

        if any(k in name for k in ["inquisition", "expulsion", "converso", "morisco", "heresy"]):
            cats.update(["Político", "Social", "Cultural"])

        if any(k in name for k in ["reconquista", "crusade", "jihad", "frontier", "border", "march"]):
            cats.update(["Político", "Cultural"])

        # ─── FALLBACK ─────────────────────────────────────────────────────────────
        if not cats:
            cats.add("Cultural")

        src = os.path.join(base_dir, file)
        if os.path.isfile(src):
            for cat in cats:
                dst = os.path.join(base_dir, cat, file)
                shutil.copy2(src, dst)
            count += 1

    print(f"[OK] {os.path.basename(base_dir)}: {count} files classified -> {list(cats)}")

print("\nDone.")
