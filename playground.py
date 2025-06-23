Merci pour ce long exposé très riche, tu touches ici à **l'ensemble des tests de revue KYC/KYS, questionnaires sanctions, processus de screening et d'échantillonnage** dans le cadre d’une mission d’audit sur les entités bancaires. Voici un **résumé structuré**, utile soit pour reformuler à l’écrit dans un livrable, soit pour t’aider à formaliser les cas d’automatisation ou de standardisation des contrôles.

---

### 🔎 1. **Tests KYC – SNE Customer Diligence**

* **Test 1** : vérifier que les clients filtrés (screening sanctions) ne sont pas sanctionnés → test manuel actuellement.
* **Test 2** : même logique mais dans un autre périmètre (toujours dans SNE Customer Diligence).
* Objectif : automatiser partiellement ces tests grâce à des extractions structurées (ex : extractions clients / revues KYC).
* Outils mentionnés : non précisés, mais outils internes de gestion KYC sont censés permettre ce suivi.

### 🔁 2. **Revue Périodique KYC**

* Périodicité dépend du **niveau de risque du client** :

  * **Vert (low risk)** → revue tous les **3-4 ans**.
  * **Orange (medium risk)** → tous les **2 ans**.
  * **Rouge (high risk)** → chaque **année**.
* Ce process est **à la charge de l'entité locale**, avec un département dédié à la revue KYC.
* **L’audit** vérifie que ce suivi est respecté, mais ne le réalise pas lui-même.

### 📄 3. **Questionnaire Sanctions**

* Analyse manuelle nécessaire à 100% aujourd’hui, car :

  * Contenu souvent non structuré (scan PDF, nommage peu standardisé).
  * Détection automatique possible (OCR/LLM), mais pas trivial à mettre en place.
  * Il existe une **double vérification** :

    * Niveau **client** : questionnaire existe, est rempli, version correcte utilisée.
    * Niveau **entité/processus** : questionnaire prévu dans le process, bonne version en place.

### 📋 4. **Échantillonnage Clients**

* En moyenne : **20 à 30 clients** par mission.
* **Approche par les risques** (pas forcément déterministe) :

  * Ex : on cible plutôt des clients de pays à risque (Russie, Biélorussie).
  * Pas de règle fixe sauf le volume (lié à la taille/risque de la mission).
* Aide au diagnostic : les entités doivent fournir les documents KYC et questionnaires.

### 🏢 5. **Lien entre revue KYC client et plan d’audit entité**

* **Processus indépendants** :

  * Le **plan d’audit** détermine la fréquence d’audit d’une entité selon sa criticité.
  * La **revue KYC** est gérée **par l’entité** selon le niveau de risque des clients.
  * L’audit vérifie juste que le process de revue KYC fonctionne correctement.

### 🤖 6. **Automatisation – Obstacles et Opportunités**

| Tâche                                        | Automatisable ? | Freins identifiés                                            |
| -------------------------------------------- | --------------- | ------------------------------------------------------------ |
| Vérif revues KYC faites (statut OK)          | ✅ oui           | Extraction possible si outil structuré                       |
| Vérif existence questionnaire sanction       | ✅ partiellement | OCR + logique de détection à affiner                         |
| Analyse contenu du questionnaire             | ❌ difficile     | Lecture + interprétation des réponses → fort jugement humain |
| Échantillonnage client                       | ✅ partiellement | Peut suivre des règles semi-déterministes                    |
| Comparaison sourcing hub vs base fournisseur | ✅ oui           | Test simple de jointure + analyse manuelle si écart          |

### 🧾 7. **Fournisseurs (KYS)**

* Vérification dans **Sourcing Hub** (outil de référence groupe).
* On regarde :

  * Si tous les fournisseurs de l’entité sont dans Sourcing Hub.
  * Si ceux qui n’y sont pas ont une **justification**.
  * Si les fournisseurs éligibles ont bien été **filtrés sanctions**, bénéficiaires identifiés.
* Estimation charge : **\~5 jours/homme**, moins critique que le KYC.
* Outils : fichiers Excel + analyse manuelle.

---

### 📌 Conclusion

Tu as bien saisi les enjeux :

* Forte charge manuelle, surtout sur la partie non structurée.
* Automatisations possibles mais limitées par :

  * la **qualité du nommage** des fichiers,
  * la **présence de scans PDF** non structurés,
  * le besoin de **jugement humain** (ex : interprétation des questionnaires).

---
Tu veux probablement une synthèse claire de cette grosse partie sur le **filtrage sanctions/embargos**, le rôle du **SLA** et du **SNR mapping**, et surtout ce qu'on regarde concrètement en audit. Voici un résumé structuré et pédagogique pour que tu puisses t'y retrouver facilement ou réexploiter ça dans un document ou outil :

---

## 🔎 Partie filtrage – Scanning (Sanctions / Embargos)

### 1. **SLA – Service Level Agreement**

* **Définition** : Contrat entre une entité et le groupe (ou parfois un tiers) définissant les prestations de services, notamment ici sur le **filtrage sanctions**.
* **Ce qu’on vérifie** :

  * Y a-t-il un contrat en place ?
  * Qui réalise le filtrage : l’entité, le groupe, ou un tiers ?
* **Méthodologie** :

  * Récupération des contrats (souvent par mail).
  * Vérification basique, sans analyse poussée.
* **Temps / Priorité** :

  * ≈ 1 jour homme.
  * Faible priorité, **peu intéressant à automatiser**, jugé peu critique.

---

### 2. **SNR – Système de Référentiel Cartographie**

* **Objectif** : Recenser ce que chaque entité filtre :

  * **Référentiels** : clients, employés, fournisseurs, etc.
  * **Transactions** : flux intra/inter-pays, types de flux (virement, carte, etc.)
* **Format** :

  * Un **fichier Excel** massif accessible via **l’outil MySNRMAP** ou fourni par la conformité.
  * Chaque ligne = une entité du groupe, avec des colonnes comme :

    * Type de référentiel / flux.
    * Filtré ou non (oui / non).
    * Fréquence (manuel, auto).
    * Finalité (sanction, embargo...).

#### 🔍 Ce qu’on vérifie :

* Que les déclarations sont **cohérentes avec la politique du groupe**.
* Exemple :

  * Si une entité dit qu’elle **ne filtre pas ses clients** ⇒ **alerte**, c’est contraire à la politique.
  * Si une entité ne filtre pas ses employés mais c’est justifié par une contrainte légale (ex. : Monaco) ⇒ ok.

#### 🧠 Analyse :

* **Fort jugement humain** : ≈ 90%.
* Lecture manuelle de la ligne correspondant à l’entité auditée.
* Pas de challenge du fichier dans son ensemble, mais **vérification locale** de cohérence.

#### 💡 Piste d’automatisation :

* Charger le fichier Excel dans un LLM (type ChatGPT) et lui demander :

  * **Synthèse** des flux et référentiels filtrés par une entité.
  * Mise en évidence des **points de non-conformité** par rapport à la politique du groupe.

---

### 3. **Filtrage – Définition technique**

* **Filtrage sanctions** = comparaison de données (référentiels ou flux) avec des **listes de personnes / entités sanctionnées** fournies par des régulateurs.
* **Outil utilisé** : *Fircosoft* (moteur externe).

  * Utilise des techniques de **fuzzy matching**, matching par score (prénom, nom, date de naissance, etc.).
  * Génère des **alertes** analysées manuellement.
* **Que filtre-t-on ?**

  * Les **clients** (obligatoire).
  * Les **fournisseurs, bénéficiaires effectifs** selon les cas.
  * Les **transactions** selon leur nature (intra-pays, transfrontalières…).
  * **Pas toujours les employés** (soumis à loi locale).

---

## ✅ Synthèse – Ce qu’on fait en audit

| Étape                     | Action de l’auditeur                            | Type d’analyse     | Automatisable ?              |
| ------------------------- | ----------------------------------------------- | ------------------ | ---------------------------- |
| Vérification des SLA      | Demande des contrats, vérifie leur existence    | Faible jugement    | Peu prioritaire              |
| Analyse SNR               | Lire la ligne de l’entité et vérifier cohérence | Fort jugement      | Possible en partie via GPT   |
| Compréhension du filtrage | S’assurer que les bons objets sont filtrés      | Normatif / logique | Possible (analyse de config) |

---

Voici une **analyse détaillée de la partie "filtrage"** dans le cadre d’un audit sanctions-embargos, telle que décrite dans l’échange :

---

## 🔍 **1. Introduction à la phase de filtrage**

La phase de **filtrage** est décrite comme **la plus importante** et **la plus intéressante intellectuellement** du processus de revue sanctions-embargos. C’est là que l’équipe d’audit va passer **en revue les dispositifs de filtrage** des entités, afin de s’assurer de leur **conformité réglementaire** et du bon fonctionnement opérationnel des outils.

Le filtrage ici s'entend exclusivement dans le **cadre des sanctions internationales**, et consiste à **comparer des flux ou des référentiels** avec des **listes de personnes ou d'entités sanctionnées** (listes OFAC, UE, ONU, etc.).

---

## 🧾 **2. Vérification des SLA (Service Level Agreements)**

### Objectif :

Vérifier si un contrat existe entre l’entité et :

* Le **groupe** (filtrage réalisé par le groupe pour l’entité),
* Ou un **prestataire tiers** (rare),
  pour la **réalisation du filtrage**.

### Points-clés :

* **SLA = contrat de prestation de service**, précisant la responsabilité du filtrage.
* Se fait **souvent dès la phase diagnostic** via **demande de contrat à l’entité**.
* L’analyse est **simple et peu chronophage** : une **vérification binaire** (contrat présent / absent, cohérent ou non).
* Importance **modérée** en termes de risques ; **pas prioritaire** pour automatisation.

---

## 📊 **3. Le SNR Mapping (Système de Référentiel - Cartographie)**

### Objectif :

Analyser le fichier Excel de mapping du filtrage, appelé **SNR MAP**, pour vérifier :

* **Quelles typologies de référentiels** (clients, employés, fournisseurs, etc.) et de **flux de transactions** sont soumises au filtrage.
* Si les pratiques déclarées sont **conformes aux exigences du groupe** et aux **réglementations locales**.

### Outil :

* Fichier disponible dans l’outil **MySNRMAP**, consultable pour tout le groupe.
* Contient :

  * Code et nom de l'entité
  * Typologie des données : **référentiels** (RH, clients, prospects, fournisseurs...) et **flux** (paiements, virements, cartes...)
  * **Indication si filtré ou non**, à quelle **fréquence**, et si le traitement est **manuel ou automatique**.
  * **Motif d’exclusion éventuelle** (ex. : loi locale interdisant le filtrage RH à Monaco).

### Analyse :

* **Manuelle à 90 %**, jugée très fastidieuse mais incontournable.
* On **ne vérifie pas la véracité du contenu**, mais **la cohérence** avec les politiques du groupe.
* Exemple : si une entité déclare **"ne pas filtrer ses clients"**, cela soulève immédiatement un **signal d’alerte**.
* Objectif : détecter les **incohérences manifestes**.

### Difficultés :

* **Fichier Excel très volumineux** (toutes les entités du groupe y sont listées).
* Analyse repose sur **des règles implicites** (ex. : les employés peuvent être exclus à cause de la réglementation locale, mais pas les clients).

---

## ⚙️ **4. Le moteur de filtrage (Fircosoft)**

### Description :

* Outil externe utilisé pour **faire tourner le filtrage automatiquement**.
* Intègre :

  * Les **listes de sanctions**
  * Les **référentiels clients** et les **flux**
  * Des **paramètres internes**
* Utilise des **algorithmes de fuzzy matching** pour détecter les correspondances partielles (ex. différentes orthographes de Mohamed).

### Fonctionnement :

* Compare les **données entité** avec les **listes sanctions**.
* Génère des **alertes** si correspondances (selon un **score de matching**).
* Les alertes sont ensuite **analysées manuellement** par l’entité ou le groupe.

---

## 📌 **5. Points clés à analyser dans l’audit**

| Élément                           | Que fait-on ?                                                         | Risques associés                                                 |
| --------------------------------- | --------------------------------------------------------------------- | ---------------------------------------------------------------- |
| **Présence d’un SLA**             | Vérifie existence de contrat entre entité et groupe/tier              | Flou de responsabilité si filtrage mal fait                      |
| **SNR Mapping**                   | Vérifie la **cohérence** des déclarations avec la politique du groupe | Déclaration erronée → non-conformité réglementaire               |
| **Typologies filtrées**           | Vérifie si les clients, fournisseurs, flux sont bien filtrés          | Manquement à l’obligation réglementaire                          |
| **Cas d’exclusion**               | Vérifie si les raisons sont **documentées** (lois locales, etc.)      | Filtrage partiel injustifié                                      |
| **Mise à jour SNR**               | Vérifie si l’entité met à jour son mapping régulièrement              | Données obsolètes, erreurs de conformité                         |
| **Outil de filtrage (Fircosoft)** | Comprendre fonctionnement général                                     | Permet de détecter les failles techniques ou limites du matching |

---

## 🤖 **6. Automatisation possible ?**

| Tâche                           | Automatisation envisageable ? | Commentaire                                                                  |
| ------------------------------- | ----------------------------- | ---------------------------------------------------------------------------- |
| Analyse SLA                     | ❌ Non prioritaire             | Requiert lecture de contrats PDF peu nombreux                                |
| Vérification SNR Mapping        | ✅ Potentiellement oui         | Extraction automatique des lignes entité + comparaison avec règles du groupe |
| Matching noms (Fircosoft)       | ❌ Difficile                   | C’est un outil propriétaire, peu d’accès aux règles internes                 |
| Extraction des données filtrées | ✅ Oui                         | Peut se faire via parsing Excel + règles métier définies à l’avance          |

---

## ✅ **Conclusion**

La partie **filtrage** est **centrale** dans l'audit sanctions-embargos :

* Elle implique **beaucoup de vérification manuelle** (surtout SNR Mapping),
* Mais elle **porte sur des points à très fort enjeu réglementaire** : la détection des personnes ou entités sanctionnées.
* Si l’automatisation complète est difficile, une **aide à l’analyse du fichier SNR** (via GPT ou scripts de parsing) pourrait **réduire drastiquement le temps passé**, en isolant les entités non conformes ou douteuses.

Voici une **analyse détaillée de la partie "filtrage"** dans le traitement des opérations SWIFT, à partir de ce que tu m’as fourni :

---

## 🔎 **1. Objectif du filtrage**

Le filtrage a pour objectif principal de détecter en amont des opérations financières à risque, notamment celles qui pourraient enfreindre des sanctions internationales (terrorisme, blanchiment, embargos, etc.).
C’est une **exigence réglementaire majeure**, liée à la LCB-FT (Lutte Contre le Blanchiment et le Financement du Terrorisme) et à la conformité aux sanctions internationales (OFAC, UE, ONU, etc.).

---

## 🧭 **2. Positionnement du filtrage dans le processus SWIFT**

Le processus se déroule en plusieurs étapes :

1. **Le conseiller saisit l’ordre de paiement dans l’outil EG.**
2. **Avant d’être envoyé via le réseau SWIFT**, le message passe par un **moteur de filtrage**, typiquement **Fircosoft**, pour vérifier :

   * La correspondance des données (bénéficiaire, émetteur, banque correspondante…) avec des **listes de sanctions**.
   * L’absence de transactions avec des personnes, entités ou pays sanctionnés.
3. Une fois filtré, le message est envoyé via SWIFT.
4. À la **réception**, les messages SWIFT entrants sont également soumis à un **filtrage de conformité** avant d’être crédités au compte du client.

Ce double filtrage (émission + réception) garantit une traçabilité et une conformité complète.

---

## 🛠️ **3. Mécanisme du moteur de filtrage (ex: Fircosoft)**

* **Données en entrée :**

  * Données clients (nom, adresse, pays…)
  * Détails transactionnels (montants, bénéficiaires, banques intermédiaires…)

* **Comparaison avec les listes de sanctions** :

  * **Listes Groupe** (ex : OFAC, UE, ONU, listes françaises obligatoires pour toutes les entités)
  * **Listes locales** (propres à un pays ou à un régulateur local – ex : liste du régulateur mozambicain)

* **Mode de fonctionnement :**

  * Algorithmes de matching : fuzzy matching, phonétique, traitement de variantes linguistiques…
  * Résultats générés : alertes s’il y a un match potentiel.
  * Les alertes sont ensuite traitées manuellement par les équipes conformité.

---

## 🧾 **4. Contrôles et vérifications effectuées**

Lors d’une revue du dispositif de filtrage, plusieurs éléments sont analysés :

### 🔹 **Sur le process de traitement SWIFT** :

* Est-ce que le traitement des messages SWIFT est **automatisé** ou **manuel** ?

  * Si manuel, il existe un **risque de modification non tracée** des données ➝ audit de la séparation des tâches (saisie ≠ validation).
  * Revue des procédures internes documentées.
  * Présence de contrôles de type "4-eyes check".

### 🔹 **Sur le moteur de filtrage lui-même** :

* Vérification des **paramètres de configuration** du moteur.
* Analyse des **listes de sanctions utilisées** : sont-elles à jour ? Correspondent-elles bien à celles imposées par les régulateurs ?
* Pour les **listes locales**, il faut :

  * Télécharger la dernière version depuis le site du régulateur local.
  * Comparer (souvent manuellement ou via des scripts type KNIME ou Excel) avec la version effectivement injectée dans le moteur de filtrage.
  * Cette **comparaison peut être automatisée** (retraitement de fichiers Excel / CSV, jointures, détection de différences).

---

## 🧪 **5. Pré-filtrage : zone de risque élevée**

Certaines entités ajoutent un **outil de pré-filtrage maison** en amont de Fircosoft.

Problèmes potentiels :

* **Décision de filtrage prise en amont** (exclusion d’alertes) avec **peu ou pas de contrôle du groupe**.
* Risque que des transactions "à risque" ne soient **jamais escaladées**.
* Ce type d’outil est **rare** et souvent **non validé par le groupe**.

Analyse requise :

* Existe-t-il un outil de pré-filtrage ?
* Qui l’a validé ?
* Comment est-il paramétré ?
* Peut-on injecter des données "test" (ex : noms très connus sous sanctions) et voir si l’alerte est levée ?

---

## 🤖 **6. Automatisabilité vs Jugement Humain**

| Étape / Test                                        | Automatisable ?     | Degré de jugement humain |
| --------------------------------------------------- | ------------------- | ------------------------ |
| Vérification de l’existence d’un moteur de filtrage | Oui                 | Faible                   |
| Revue des procédures de traitement                  | Non                 | Fort                     |
| Analyse de la configuration Fircosoft               | Partiellement       | Moyen à fort             |
| Comparaison des listes locales vs injectées         | Oui (scriptable)    | Moyen                    |
| Audit de l’outil de pré-filtrage                    | Non (en l’état)     | Très fort                |
| Injection de faux noms pour test (pré-filtrage)     | Partiellement (POC) | Fort                     |

---

## ⏱️ **7. Estimation de charge**

* **Traitement SWIFT + filtrage** : 2 à 3 jours par entité
* **Revue des listes locales** : 1 à 2 jours supplémentaires si liste locale existante
* **Test sur pré-filtrage** : dépendant de l’existence d’un tel outil (rare)

---

## 📌 **Conclusion**

Le **filtrage SWIFT** est un **processus critique de conformité** impliquant :

* Une grande variabilité selon les entités (process, outils, régulateurs locaux)
* Une combinaison de tâches manuelles et de tâches automatisables
* Des enjeux de conformité très élevés

La **partie automatisable** (notamment la comparaison de listes) peut faire gagner du temps et fiabiliser l’analyse, mais **l’essentiel repose sur l’audit du process et la compréhension fine des risques humains**.
________________________
prise en charge de l’"ongoing monitoring". Ils ont compris rapidement les enjeux en voyant la table issue de la cartographie. Cela signifie que l’équipe est bien alignée sur les objectifs, et prête à investir du temps et des ressources pour concrétiser cette démarche.

Approche de priorisation par valeur/coût
Une démarche structurée de priorisation va être menée, visant à classer les actions selon leur valeur ajoutée et leur coût. Cela inclura notamment les contrôles, les sources de données, et leur lien. Tu seras impliquée dans ce processus, notamment pour structurer l’ordre dans lequel attaquer les sujets.

Lien entre données et contrôles
Tu travailles activement à établir une cartographie fine entre les contrôles et les données qu’ils mobilisent. C’est une pièce maîtresse pour évaluer la faisabilité technique et l’automatisation. Cela permet aussi d’identifier les points de blocage (ex. : données manuelles vs. accessibles via data lake).

Accès aux ressources techniques (ingestion, traitements)
moyens techniques(équipe à Bangalore, ingestion de données, retraitements) peuvent être mis à disposition. Cela ouvre la voie à un prototypage plus ambitieux, sans te surcharger des aspects les plus fastidieux.

Structuration et scoring des contrôles
Tu souhaites structurer les informations collectées (notamment via les entretiens avec Éric) pour dégager des scores (valeur, faisabilité, fréquence, etc.) permettant de prioriser les contrôles. Cela facilitera les arbitrages collectifs lors des échanges avec Julien, Alban et Xavier.

Gouvernance : faible priorité métier mais forte valeur en monitoring
Les contrôles de gouvernance sont perçus comme peu prioritaires par les opérationnels car peu fréquents et demandant une analyse humaine. Néanmoins, ils ont une forte valeur en matière de risk assessment et d’automatisation via le monitoring, ce qui en fait des candidats intéressants à moyen terme.

Partie "alertes et filtrage" : cœur du métier, priorité forte
Le filtrage des transactions et la gestion des alertes est le cœur opérationnel du métier. C’est là que se concentre la demande des parties prenantes (Éric, Fleur). Cela représente un challenge analytique intéressant et un terrain pour proposer des approches innovantes (classification, scoring de gravité…).

Explicabilité : enjeu central
Il faut impérativement éviter les modèles opaques. L’objectif est de construire des approches analytiques transparentes (ex. : règles, classification simple) pour que les utilisateurs comprennent les alertes générées. Le clustering actuel est critiqué pour son manque d’interprétabilité.

Redéfinir la notion d’anomalie
Tu soulèves un point crucial : avant même d’implémenter des modèles, il faut définir ce qu’est une anomalie dans ce contexte. Cela implique une analyse profonde des comportements normaux/attendus (par client, par moment, par contexte) pour construire des features pertinentes.

Objectif final : fournir des bornes décisionnelles claires
Quel que soit le modèle ou la méthode, le résultat final doit permettre d’assortir les décisions d’alertes de seuils clairs, justifiables, pour que l’auditeur ou l’analyste sache pourquoi une transaction est suspecte, et ait des moyens d’action concrets.


