import os
import shutil
from pathlib import Path

dest_base = Path(r"G:\Mi unidad\Noor_ 2026_archivos\Análisis_bibliométrico_temática_aplicada\Siglo X Wos 2026")

categories = {
    "Akguel - 2020 - The Most Recent Findings Related to the Early Iron Age at the Eastern Black Sea Mountains.pdf": "Otros contextos",
    "Almagro - 2008 - The Caliphal gate of Gormaz Castle.pdf": "Político",
    "Alvarado et al. - 2021 - The archaeological site Retes (C-378 Re), an exceptional find in the flank of the Irazu volcano duri.pdf": "Otros contextos",
    "Alvarez et al. - 2022 - On the edges of Ilbira Emirate and Caliphate pottery in the southern district of the madina.pdf": "Cultural",
    "Anderson - 2014 - Sign of the Cross contexts for the Ivory Cross of San Millan de la Cogolla.pdf": "Cultural",
    "Antonia Martinez-Nunez - 2015 - Umayyad Funerary Inscription Appeared in Madrid (308921).pdf": "Cultural",
    "Arce-Sainz - 2015 - The Alleged Basilica of Saint Vincent of Cordoba From a Historical Myth to an Obstinacy of Historio.pdf": "Cultural",
    "Ariza Armada - 2019 - New Monetary Typology of `Abd al-Rahman III from Madinat al-Zahra' Mint with Hebrew Inscription.pdf": "Económico",
    "Arnold - 2018 - Mathematics and the Islamic Architecture of Cordoba.pdf": "Cultural",
    "Aydin - 2024 - Fiqh Works in Turkey on the Indian Subcontinent An Overview.pdf": "Otros contextos",
    "Azuar - 2016 - On Mozarabic Archaeology. II. About churches and epigraphic documents.pdf": "Cultural",
    "Azuar - 2023 - THE METALLIC EWERCANTARA WITH LID FROM THE CALIPHAL TREASURE â€œPARQUE CRUZ CONDEâ€  (CORDOBA).pdf": "Cultural",
    "Azzazy - 2018 - Exploratory palynological studies at the Tell el-Daba'a-Avaris archaeological site.pdf": "Otros contextos",
    "Barcelo - 2018 - Emiral Arab epigraphy (9th century). The gravestone of Tudela and the stele of an Umayyad woman.pdf": "Cultural",
    "Barcelo - 2020 - The Caliphal Painting of Bedar (Almeria, 355966).pdf": "Cultural",
    "Bellon - 2025 - Two place names, the same city Segontia and Medinaceli in historical and documentary sources betwee.pdf": "Económico",
    "Blanco Guzman - 2007 - MADINAT QURTUBA AFTER FITNA. AN APPROACH THROUGH THE HISTORIOGRAPHY.pdf": "Político",
    "Blanco-Guzman - 2019 - The Umayyad shadow. Cordova and the Almohads of the second half of the VIXII century.pdf": "Político",
    "Boone y Worman - 2007 - Rural settlement and soil erosion from the late roman period through the medieval Islamic period in.pdf": "Social",
    "Bosanquet - 2023 - How the Umayyads Lost the Islamic West Contrasting Depictions of the Uprising of 122740 by Arab Hi.pdf": "Político",
    "Bourke et al. - 2009 - THE BEGINNING OF THE EARLY BRONZE AGE IN THE NORTH JORDAN VALLEY NEW 14C DETERMINATIONS FROM PELLA.pdf": "Otros contextos",
    "Buresi - 2010 - FROM ONE PENINSULA TO THE OTHER CORDOVA, `UTHMAN (644-656) AND THE ARABS DURING THE ALMOHAD PERIOD.pdf": "Político",
    "Calvo Capilla - 2012 - Madinat al-Zahra ` and the observation of time the rebirth of Classical Antiquity in the Cordoba of.pdf": "Cultural",
    "Calvo Capilla - 2018 - The Visual Construction of the Umayyad Caliphate in Al-Andalus through the Great Mosque of Cordoba.pdf": "Cultural",
    "Camacho Cruz y Valera Perez - 2022 - Ceramicas con decoracion figurada en los arrabales occidentales de Madinat Qurtuba (Cordoba).pdf": "Cultural",
    "Camuera et al. - 2023 - Drought as a possible contributor to the Visigothic Kingdom crisis and Islamic expansion in the Iber.pdf": "Social",
    "Carballeira Debasa - 2017 - The Use of Charity as a Means of Political Legitimation in Umayyad al-Andalus.pdf": "Social",
    "Cardoso - 2023 - `Syria Rises to Receive the Caliph' Umayyad Caliphal Titles from Cordoba to Damascus.pdf": "Político",
    "Cardoso - 2025 - Court, doors, crowns, turbans, and thrones insignia, models, and rituals from the Visigothic Kingdo.pdf": "Cultural",
    "Carraz - 2015 - â€œA Specific and Marginal Realityâ€  Saracen Piracy on the Gulf of Lion from the 11th to the 13th Cent.pdf": "Social",
    "Carretero y Enamorado - 2025 - Cloth appliquÃ©s in al-Andalus the piece from Arraijanal medieval site in Mijas (Malaga).pdf": "Cultural",
    "Carrillo-Calderero - 2025 - The Adoption of Eastern Models in Jewelry from Al-Andalus During the Tenth and Eleventh Centuries P.pdf": "Cultural",
    "Carvajal Lopez - 2019 - After the conquest ceramics and migrations.pdf": "Social",
    "Celestino Perez y Rodriguez Gonzalez - 2018 - Cerro Borreguero. An archaeological site for the transition from the Final Bronze Age to the Tartess.pdf": "Otros contextos",
    "Chalmeta - 2018 - The seals of the umayyad conquest and the formation of al-Andalus (711-756).pdf": "Político",
    "Charloux et al. - 2024 - A Bronze Age town in the Khaybar walled oasis Debating early urbanization in Northwestern Arabia.pdf": "Otros contextos",
    "Chevance et al. - 2019 - Mahendraparvata an early Angkor-period capital defined through airborne laser scanning at Phnom Kul.pdf": "Otros contextos",
    "Christys - 2018 - Educating the Christian Elite in Umayyad Cordoba.pdf": "Social",
    "Christys y Fierro - 2024 - Rulers Making Boundaries Clear in the Medieval Islamic West The Cordoban Umayyads and the Almohads.pdf": "Político",
    "Clapes Salmoral - 2019 - Formation and evolution of the suburban landscape in islamic times an example from the western subu.pdf": "Social",
    "Clapes Salmoral - 2020 - The architecture of power The umayyad buildings from â€œTablero Altoâ€  and their integration into the.pdf": "Político",
    "Clark et al. - 2022 - Urbanscape, Land Use Change and Centralization in the Region of Uruk, Southern Mesopotamia from the.pdf": "Otros contextos",
    "Coll Conesa - 2014 - Technique, Courtliness and Social Distinction in the Medieval Ceramics.pdf": "Cultural",
    "Crego Gomez - 2021 - Ronda in Al-Muqtabis 2b and 2c.pdf": "Social",
    "Cressier y Gonzalez-Villaescusa - 2025 - A Look Back at the Irrigated Areas of the Medieval Town of TÄ mdult (Morocco).pdf": "Económico",
    "Cuenca-Abellan - 2024 - The Tripartite Qibla Wall as a Visual Form of Embodied Belief From Al-Andalus to Mudejar and Morisc.pdf": "Cultural",
    "Davis - 2013 - â€œMinding the Gapâ€  A Problem in Eastern Mediterranean Chronology, Then and Now.pdf": "Otros contextos",
    "Daza Pardo - 2018 - Brick construction in the periphery of al-Andalus to AD 1000. Caliphal border activity and the â€œston.pdf": "Político",
    "de Felipe - 2025 - The collective portrait of the Banu Birzal.pdf": "Político",
    "De Juan Ares et al. - 2021 - Composition and origins of decorated glass from Umayyad Cordoba (Spain).pdf": "Cultural",
    "de la Puente - 2023 - Al-Hakam I in the Andalusi Sources His Slaves, Eunuchs, and Concubines.pdf": "Social",
    "de Villar Iglesias - 2020 - THE ECONOMIC ASPECTS OF THE BATTLE FOR THE MAGHREB BETWEEN UMAYYADS AND FATIMIDS CONTROLLING THE AC.pdf": "Económico",
    "Del Cueto et al. - 2023 - First Approach to the Pollen Preserved in a Megalithic Monument of the Western Cantabrian Mountains.pdf": "Otros contextos",
    "Duque - 2022 - THE PASSIO OF MONK GEORGE AND THE LITURGY OF MARTYRDOMIN TENTH-CENTURY CRDOBA.pdf": "Cultural",
    "Elhadri - 2006 - The coinages of the first Hudide Sulayman al-Musta'in.pdf": "Económico",
    "Elices-Ocon - 2024 - Antique Sculpture at Madinat al-Zahra' Transcultural Collecting and the Assertion of Caliphal Power.pdf": "Cultural",
    "Emanov - 2023 - The Chronotope of the Rurikid Polity (911-987).pdf": "Otros contextos",
    "Eroglu Bilgin - 2022 - A GIFT FROM FATHER TO SON GIRONA CASKET.pdf": "Cultural",
    "Fernandez-Puertas - 2009 - III. The Mosque of Cordoba. The design of the inner facade of the Bab al-Wuzara'. The Doorway of the.pdf": "Cultural",
    "Fierro - 2004 - The religious politics of Abd!Al-Rahman III.pdf": "Político",
    "Freudenhammer - 2022 - Exarachellos Dirhams in Tenth-Century Barcelona.pdf": "Económico",
    "Freudenhammer - 2025 - Evidence of Early Medieval Grain Exports from Barcelona to Al-Andalus.pdf": "Económico",
    "Frey Sanchez - 2016 - Was the Western Islamic Political Crisis of the 13th Century Due to climatic Change a Historical Ap.pdf": "Político",
    "Fuentes - 2019 - The Islamic Crossed-Arch Vaults in the Mosque of Cordoba.pdf": "Cultural",
    "Gallon - 2024 - From Saqaliba to Ciclaues. An Arabism and Some Eunuchs in the Christian Principalities of the Iberia.pdf": "Social",
    "GarcÃ­a SÃ¡nchez - 1996 - La alimentaciÃ³n popular urbana en al-Andalus.pdf": "Social",
    "Garcia - 2020 - The Qhapaq Nan in the Calingasta valley (San Juan).pdf": "Otros contextos",
    "Garcia - 2023 - Pork consumption, gastro-politics and social Islamisation in early al-Andalus (eighth to tenth centu.pdf": "Social",
    "Garcia - 2023 - Social islamisation and livestock improvement in Qurtuba in Early al-Andalus (8th-10th centuries).pdf": "Económico",
    "Garcia Blanquez - 2015 - The (islamic) water-lifting wheels of the andalusi hydraulic system in Murcia (Senda de Granada). Te.pdf": "Económico",
    "Garcia Ortega - 2021 - FORMAL INVESTIGATIONS INTO THE CALIPHAL ARCHITECTURE OF CORDOBA BASED ON AN ENIGMATIC DRAWING FROM 1.pdf": "Cultural",
    "Gil Crespo et al. - 2018 - Fortified Construction Techniques in al-Tagr al-Awsa, 8th-13th Centuries.pdf": "Económico",
    "Gomez Munoz - 2007 - THE PROPHET KING SOLOMON AND THE IMAGE OF ISLAMIC SOVEREIGN FROM AN UNPUBLISHED PIECE FROM CORDOBA.pdf": "Cultural",
    "Gomis y Gomez - 2024 - The bell of Abbot Samson of Cordoba (10th century) a unique vestige of the soundscape of early medi 1.pdf": "Cultural",
    "Gonzalez Arce - 2014 - THE COMPOSITION OF THE MANORIAL ALMOJARIFAZGOS OF THE KINGDOM OF SEVILE, 13TH- 15TH CENTURIES.pdf": "Económico",
    "Gonzalez Arce - 2014 - The Evolution of the Almojarifazgo Tariff in Cordoba between the 13th and the 15th Centuries.pdf": "Económico",
    "Gonzalez Cavero - 2018 - The Almohad Caliphate A Look at Al-Andalus through Arabic Documentation and Their Artistic Manifest.pdf": "Político",
    "Gonzalez Gutierrez - 2018 - The Role and Meaning of Religious Architecture in the Umayyad State Secondary Mosques.pdf": "Cultural",
    "Gonzalez-Gutierrez - 2023 - Religious Buildings in Early al-Andalus Origins, Consolidation and Prevalence in Urban Contexts.pdf": "Cultural",
    "Govantes-Edwards et al. - 2024 - The glass from the arrabal of Arrixaca (Murcia, 12th-13th centuries).pdf": "Cultural",
    "Gozalbes Cravioto - 1991 - Algunos datos sobre el comercio entre al-Andalus y el norte de Ã frica en la Ã©poca omeya (I) los pue.pdf": "Económico",
    "Gurriaran Daza - 2020 - Building techniques in the medieval walls of Almeria.pdf": "Cultural",
    "Ihnat - 2024 - Beyond Hagiography Gender and Violence in the Earliest Liturgy for Pelagius.pdf": "Cultural",
    "Jaouhari - 2018 - A Fragment of a Forgotten Dictionnary Essai on Dating Parisinus arabicus 4235 of BnF.pdf": "Cultural",
    "Jimenez Puertas et al. - 2023 - A rural settlement from the umayyad period in the Vega of Granada Manzanil (Loja). Limits and possi.pdf": "Social",
    "Jimenez-Brobeil et al. - 2022 - Introduction of sugarcane in Al-Andalus (Medieval Spain) and its impact on children's dental health 1.pdf": "Social",
    "Kampf et al. - 2010 - Gayite, a new dufrenite-group mineral from the Gigante granitic pegmatite, Cordoba province, Argenti.pdf": "Otros contextos",
    "Khanipour y Nishiaki - 2024 - Dating the beginning of the Pottery Neolithic in South Iran Radiocarbon dates from Tol-e Sangi, the.pdf": "Otros contextos",
    "Khansa - 2025 - A Review of the Escorial Codex Ã rabe 1876 A Collection of Fourteen Short Stories from North Africa.pdf": "Cultural",
    "Khoury - 2019 - Education during the Arab Renaissance and Its Path to the West.pdf": "Social",
    "Kuzudisli - 2025 - Identification of Rihle in Classical Rijal Works Sources, Methods, and Proposals.pdf": "Cultural",
    "Labarta - 2015 - THE CASKET OF HISAM ITS EPIGRAPHY.pdf": "Cultural",
    "Leon-Munoz - 2018 - Mixed constructive techniques in stone in umayyad Cordova.pdf": "Cultural",
    "Lopez Martinez de Marigorta - 2015 - Coin Minting of al-Andalus in the First Half of the FifthEleventh Century The End of a Model, the.pdf": "Económico",
    "Lopez-Brenes y Marin-Guzman - 2020 - Bobastro a hisn of permanent settlement and a fortress for resistance for the rebel `Umar ibn Hafsu.pdf": "Político",
    "Lopez-Marigorta - 2023 - How al-Andalus wrapped itself in a silk cocoon the iraz between Umayyad economic policy and Medite.pdf": "Económico",
    "Lorenzo-Jimenez - 2022 - The book of stratagems.pdf": "Político",
    "Mandala - 2012 - A NEW SOURCE FOR THE HISTORY OF ISLAMIC SICILY A PASAGE OF IBN HAYYAN'S AL-MUQTABIS V ON THE REVOLT.pdf": "Político",
    "MarÃ­n - 2004 - From al-Andalus to Spain Arab traces in Spanish cooking..pdf": "Social",
    "Marin - 2011 - A GALLERY OF ROYAL PORTRAITS ANDALUSI UMAYYAD SOVEREIGNS (2TH-4TH8TH-10TH CENTURIES) IN ARAB CHRON.pdf": "Político",
    "Martinez Delgado - 2016 - Samplers of Andalusi Strofic and Metrics as Reflected by Hebrew Poetry.pdf": "Cultural",
    "Martinez Delgado - 2019 - Study and Teaching of Biblical Hebrew in the Caliphate of Cordoba (929-1031).pdf": "Cultural",
    "Mederos Martin - 2018 - EMILIO CAMPS CAZORLA, ASSISTANT PROFESSOR OF GOMEZ-MORENO AND ELECTED DIRECTOR OF THE NATIONAL ARCHA.pdf": "Otros contextos",
    "Mestre-Ruiz et al. - 2025 - Geological Source of the Construction Materials of the Gelida Castle (Catalonia, Spain). Historical.pdf": "Otros contextos",
    "Miguel Naranjo - 2020 - Calatrava la Vieja (Carrion de Calatrava, Ciudad Real) in the Late Bronze Age (c. 1200-750 BC).pdf": "Otros contextos",
    "Molera et al. - 2018 - Glazes, colourants and decorations in early Islamic glazed ceramics from the Vega of Granada (9th to.pdf": "Cultural",
    "Molina - 2005 - The â€œhistory of the Omeyans in Andaluciaâ€  in the Masalik Al-Absar.pdf": "Político",
    "Moreno - 2023 - The Tombs of the Umayyad Rulers at the Rawda of the Alcazar of Cordoba and Their Symbolic Meaning.pdf": "Cultural",
    "Moreno - 2025 - The Early Islamization of the Urban Topography of Cordoba.pdf": "Social",
    "Morillo Cerdan et al. - 2019 - Glazed Roman Pottery from Early Empire Contexts of the Legionary Fortress at Leon (Spain).pdf": "Otros contextos",
    "Negre Perez y Marti Castello - 2015 - URBANISM IN THE EASTERN MARCH OF AL-ANDALUS DURING THE CALIPHATE (940-974) THE EXAMPLE OF MADINA TU.pdf": "Social",
    "Negre y Sune - 2019 - TERRITORY, TAX POLICIES AND MILITARY ACTIVITY DURING THE FORMATION OF A FRONTIER SPACE. THE CONSOLID.pdf": "Económico",
    "Ocon - 2020 - VIRIATHUS AND NUMANTIA RISE UP IN ARMS IN AL-ANDALUS THE DISCOURSE ON HISPANICS DURING THE TENTH CE.pdf": "Cultural",
    "Ocon - 2023 - Between East and West The Spoils of the Conquest as â€œTriggers of Memoryâ€  in Umayyad al.pdf": "Político",
    "Ocon - 2025 - Agents of spoliation spolia value and meaning manufacture in al-Andalus and IfrÄ«qÄ«ya.pdf": "Cultural",
    "Olavide - 2020 - Algunos moros muy sabidores Virtuous Muslim Kings in Examples 30 and 41 of El conde Lucanor.pdf": "Cultural",
    "Oliver PÃ©rez - 2001 - On the meaning of mawla in the Umayyad history of al-Andalus.pdf": "Social",
    "Palomar et al. - 2023 - Historical restorations of the Maqsurah glass mosaics from the Great Mosque of CÃ³rdoba.pdf": "Cultural",
    "Palomo y Escudero - 2022 - Coins in archeological context in Marida (8th-9th centuries). Study and interpretation.pdf": "Económico",
    "Patarnello - 2020 - The Islamic West in the Work of al-Mukaddasi 1.pdf": "Político",
    "Peinado - 2012 - La producciÃ³n textil en al-Andalus origen y desarrollo.pdf": "Económico",
    "Perez de Guzman et al. - 2017 - On Archeology and Architecture in Medina Azahara. Interview with Rafael Manzano Martos.pdf": "Cultural",
    "Pizarro Berengena - 2013 - The Elevated Passageways between the Mosque and the Umayyad Alcazar of Cordoba. Archaeological study.pdf": "Cultural",
    "Quesada Sanz et al. - 2014 - GRINDING MILLS FROM THE SITE AT `CERRO DE LA CRUZ' (ALMEDINILLA, CORDOBA). CLASSIFICATION AND ANALYS.pdf": "Cultural",
    "Retamero - 2006 - The formalisation of power in the coins of the muluk of Denia (V to XI century AD).pdf": "Económico",
    "Rosado-Llamas - 2024 - Book of the Hidden Pearl Among the [Literary] Jewels of kurat Bulkuna. Study and Translation of the.pdf": "Cultural",
    "Rouco Collazo et al. - 2021 - Building Archaeology of the Alcazaba of Guadix (Granada, Spain) An Example of Implanting Power in t.pdf": "Político",
    "SÃ¡nchez - 2011 - AlimentaciÃ³n y paisajes agrÃ­colas en al-Andalus.pdf": "Social",
    "Salinas - 2021 - Merchants, artisans and ulamas. The cities of the Coras of Ilbira and Pechina in Umayyad times.pdf": "Social",
    "Salinas et al. - 2019 - Glaze production at an early Islamic workshop in al-Andalus.pdf": "Económico",
    "Salinas et al. - 2019 - Tracing the tin-opacified yellow glazed ceramics in the western Islamic world the findings at Madna.pdf": "Cultural",
    "Salinas et al. - 2022 - Technological changes in the glazed wares of northern Tunisia in the transition from Fatimid to Ziri.pdf": "Económico",
    "Salinas Pleguezuelo y Amoros-Ruiz - 2024 - Tackling early medieval circulation of glazed ware in Sharq al-Andalus using a multidisciplinary app.pdf": "Económico",
    "Salinas y Pradell - 2018 - The transition from lead transparent to tin-opacified glaze productions in the western Islamic lands.pdf": "Cultural",
    "Salinas y Pradell - 2020 - Madinat al-Zahra' or Madinat Qurtuba First evidences of the Caliphate tin glaze production of `verd.pdf": "Cultural",
    "Sanal - 2023 - Arabic-Speaking Christians The Contribution of the Mozarabs to the Scientific Life in Al-Andalus (T.pdf": "Social",
    "Sanchez Saus - 2022 - THE MARTYRDOM MOVEMENT OF CRDOBA (850-859)CAUSES AND HISTORICAL CONTEXT.pdf": "Político",
    "Sanchez y Asensio - 2024 - Livestock patterns and cultural inferences in the islamic city Qartayanna (Cartagena, Spain).pdf": "Social",
    "Sanchez y Castillo - 2023 - Domestic Architecture and Urban Expansion Central Courtyard Elementary Houses in the arrabales of C.pdf": "Social",
    "Sanhueza et al. - 2020 - SAYWAS AND SACRED GEOGRAPHY IN THE QHAPAQ NAN OF THE DESPOBLADO DE ATACAMA.pdf": "Otros contextos",
    "Schibille et al. - 2020 - Ex novo development of lead glassmaking in early Umayyad Spain.pdf": "Cultural",
    "Shchavelev - 2018 - THE DATES OF DIPLOMATIC LETTERS OF HASDAI IBN SHAPRUT.pdf": "Político",
    "Silva Santa-Cruz - 2014 - Precious Ivory Presents Politics of Gift in the Andalusi Umayyad Court.pdf": "Político",
    "Suarez et al. - 2018 - Virtual acoustic environment reconstruction of the hypostyle mosque of Cordoba.pdf": "Cultural",
    "Sune Arce - 2018 - The Andalusians Husud during the Umayyad Emirate (756-929) An Ambiguous Term Used for the Gathering.pdf": "Social",
    "Sune-Arce - 2025 - `Amirid Jihad, the Religious Radicalisation of the Catalans, and the Loss of Andalusi Hegemony.pdf": "Político",
    "Tomber - 2007 - Rome and Mesopotamia - importers into India in the first millennium AD.pdf": "Otros contextos",
    "Urena - 2022 - THE MODEL OF MILITARY ORGANIZATION OF MAR BETWEEN THE 9TH AND 11TH CENTURIES.pdf": "Político",
    "Usachev - 2023 - Who Was Patriarch Joasaphus (1634-40) in His Worldly Lifet.pdf": "Otros contextos",
    "Ustun et al. - 2026 - THE POETÄ°CS OF CÄ°VÄ°LÄ°ZATÄ°ON FROM CONQUEST TO COLLAPSE Ä°N ANDALUSÄ°AN ARABÄ°C POETRY.pdf": "Cultural",
    "Valadez - 2025 - ABOUT THE THEORIES ON THE TRANSFORMATION OF CHRISTIAN PRE-ISLAMIC SACRED SPACES OF ILBIRA'S TERRITOR.pdf": "Cultural",
    "Vallejo Triano y Montilla-Torres - 2019 - Caliphs, Elites, and Servants in the Qasr of Madnat Al-Zahra' in the Light of Its Residential Archit.pdf": "Social",
    "Vega MartÃ­n y Pena MartÃ­n - 2002 - The hoard of emirate-era dirhams in Domingo Perez (Iznalloz, Granada).pdf": "Económico",
    "Velo-Gala et al. - 2022 - Islamic gold sandwich glass vessels evidences from al-Andalus.pdf": "Cultural",
    "Wasserstein - 2002 - Inventing tradition and constructing identity The genealogy of Umar Ibn Hafsun between Christianity.pdf": "Social",
    "Wasserstein - 2015 - A Man Who Never Was Talut and The Jew Again.pdf": "Social",
}

search_roots = [
    Path(r"G:\Mi unidad\Noor_ 2026_archivos"),
    Path(r"C:\Users\leoga\Desktop\Noor")
]

moved_counts = {
    "Cultural": 0,
    "Económico": 0,
    "Político": 0,
    "Social": 0,
    "Otros contextos": 0
}

moved_files = set()

# Since filenames may have encoding artifacts when saved to dict, let's normalize check using substring or just attempt
# We will iterate through PDF files in the roots, and match their names against categories.
# Some filenames have Ã© or other chars. Let's do a more robust match if possible, but exact match should work for many.
import unicodedata
def norm(s):
    return s.encode('ascii','ignore').decode().lower()

normalized_categories = {norm(k): k for k in categories}

for root in search_roots:
    for file_path in root.rglob("*.pdf"):
        # Ignore already processed files to avoid duplication
        n_name = norm(file_path.name)
        if n_name in normalized_categories:
            orig_key = normalized_categories[n_name]
            if orig_key not in moved_files:
                cat = categories[orig_key]
                dest_dir = dest_base / cat
                # In case category folder needs to be created
                dest_dir.mkdir(parents=True, exist_ok=True)
                dest_path = dest_dir / file_path.name
                
                try:
                    shutil.move(str(file_path), str(dest_path))
                    moved_files.add(orig_key)
                    moved_counts[cat] += 1
                except Exception as e:
                    print(f"Error moving {file_path.name}: {e}")

print("FINAL_REPORT")
for cat, count in moved_counts.items():
    print(f"- {cat}: {count} papers")

