import os
import shutil

base_dir = r'C:\Users\leoga\Desktop\Noor\Estudio Zotero Por Siglos\Siglo Xl'

categories = ['Económico', 'Social', 'Cultural', 'Político']
for cat in categories:
    os.makedirs(os.path.join(base_dir, cat), exist_ok=True)

classification = {
    'Brankov y Lovre - 2017 - FOOD SECURITY IN THE FORMER YUGOSLAV REPUBLICS.pdf': ['Económico', 'Político'],
    'Cateura y Melis - 2024 - Food, society, culture and politics in the Medieval West.pdf': ['Social', 'Cultural', 'Político'],
    'Colominas Aparicio - 2021 - Divine Logos and Translation among Iberian Muslims From Ibn Hazm (d. 456H1064CE) to Ahmad al-Hanaf.pdf': ['Cultural'],
    'De Angelis et al. - 2020 - Food at the heart of the Empire dietary reconstruction for Imperial Rome inhabitants.pdf': ['Social', 'Cultural'],
    'Ferrer Maestro - 2012 - The market in Ancient Rome and farming economy in times of crisis.pdf': ['Económico'],
    'Garcia - 2023 - Pork consumption, gastro-politics and social Islamisation in early al-Andalus (eighth to tenth centu.pdf': ['Político', 'Social', 'Cultural'],
    'Garcia - 2025 - Food, religion, and gender in medieval and early modern Iberia A theoretical and conceptual framewo.pdf': ['Cultural', 'Social'],
    "Garcia-Contreras Ruiz et al. - 2025 - Andrew M. Watson's legacy in al-Andalus new perspectives on the Islamic Green Revolution.pdf": ['Económico', 'Cultural'],
    'Jimenez-Castillo - 2022 - The Agricultural Expansion in Sarq al-Andalus.pdf': ['Económico'],
    'Kase y Glomb - 2023 - Affluence, agricultural productivity and the rise of moralizing religion in the ancient Mediterranea.pdf': ['Económico', 'Cultural'],
    "Lacoste y Skewes - 2025 - The palace of Palermo, River Plate's Versalles soft power and heritage in the times of Rosas and Sa.pdf": ['Político', 'Cultural'],
    'Lirola Delgado - 2019 - Al-Sumaysir, satirical poet and witness to the Taifa kingdoms.pdf': ['Cultural'],
    'Melis - 2024 - Juan Vicente. 2022. Food consumption in Medieval Iberia. A socio-economic analysis, 13th-15th centur.pdf': ['Social', 'Económico'],
    'Portass - 2022 - Peasants, Market Exchange and Economic Agency in North-Western Iberia, c.850-c.1050.pdf': ['Económico', 'Social'],
    'Retamero - 2006 - The formalisation of power in the coins of the muluk of Denia (V to XI century AD).pdf': ['Económico', 'Político'],
    'Scapini - 2016 - Studying Roman Economy and Imperial Food Supply. Conceptual and Historical Premises of the Study of.pdf': ['Económico', 'Político'],
    'Silva - 2026 - Andalusi cities in the southeast of the Iberian Peninsula (11th-13th centuries) urban evolution and.pdf': ['Social', 'Económico'],
    'Stergar - 2024 - “Yugoslavia is worthless . . . you can get neither sugar nor kerosene.” Food Supply and Political Le.pdf': ['Político', 'Económico'],
    'Taylor et al. - 2018 - The andalusi archaeological sequence (11th-12th centuries) of La Dehesilla cave (sierra de Cadiz, Sp.pdf': ['Cultural', 'Social'],
    'Taylor-Poleskey - 2020 - Food, Religion and Communities in Early Modern Europe.pdf': ['Cultural', 'Social'],
    "Vega - 2025 - Franco's Villages The Myth and History of Agrarian Colonization in Spain, 1939-1975.pdf": ['Político', 'Económico'],
    'dos Reis - 2016 - Civilizational dynamics and gastronomic diversity - some contributions from Book II of the Enarratio.pdf': ['Cultural']
}

for file, cats in classification.items():
    src = os.path.join(base_dir, file)
    if os.path.exists(src):
        for cat in cats:
            dst = os.path.join(base_dir, cat, file)
            shutil.copy2(src, dst)
            print(f"Copied {file} to {cat}")
    else:
        print(f"File not found: {file}")
