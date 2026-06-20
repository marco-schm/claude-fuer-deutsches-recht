# 05 — Due-Diligence-Kurzbericht (Sell-Side / DD-Memo)

> Auftrag: Sachverhaltsklärung für die Beschlussvorlage des Gläubigerausschusses (Az. 06_…) sowie zur Vorbereitung des Asset-Purchase-Agreements (Az. 09_…). Erstellt durch RAin Beate Lottberg (Corporate) und WP Edzard Quintbeck, Datum 12.06.2026.

## 1. Gesellschaftsrechtliche Lage der Schuldnerin

| Punkt | Inhalt |
|---|---|
| Rechtsform | GmbH, HRB 234567 B AG Charlottenburg |
| Stammkapital | 25.000 EUR (voll eingezahlt) |
| Gesellschafter | Hatchprism Holdings B.V. (NL, 64 %), Vitalis Capital Partners GmbH (DE, 26 %), Gründer-Mitarbeiter-ESOP (10 %, verwässert nach Anti-Dilution) |
| Geschäftsführung | Jasper Knoebel-Brandeis (seit 2019, Eigenantragsteller) |
| Beirat | Pro-forma; tagte zuletzt am 14.06.2025 |
| Konzernzugehörigkeit | nein — keine T-Beziehung; reine Stand-alone-GmbH |

## 2. Asset-Inventur (immaterielle Vermögensgegenstände)

### 2.1 Software (eigenentwickelt)

| Asset | Beschreibung | Repository (privat) | Lizenzstatus |
|---|---|---|---|
| ChainCortex Compliance Engine (CCE) | Hauptprodukt: KI-gestützte AML-Analyse-Pipeline für Krypto-Transaktionen (MiCAR-Compliance) | github.com/chaincortex/cce-core (private repo) | Allein-Inhaberin: Schuldnerin (Mitarbeiterurheber: § 69b UrhG, ausschließliche Nutzungsrechte) |
| BlockSight Sentinel | On-chain-Forensik-Tool (modulares Add-on zu CCE) | github.com/chaincortex/blocksight-sentinel | wie oben |
| InsightLLM Adapter | Mini-LLM-Wrapper (mit Anthropic/OpenAI-API; nicht weiterverkaufbar als LLM, nur Adapter-Code) | github.com/chaincortex/insightllm-adapter | wie oben |
| Schulungs-Datensätze | anonymisierte/synthetische On-chain-Daten für Modell-Fine-Tuning | im Repo `chaincortex/training-data` (privat; DSGVO-konform, da synthetisch) | Allein-Inhaberin |

**Open-Source-Audit:** Nikolas Reuckershoff (Tech-Lead Schuldnerin) hat eine OSS-Compliance-Untersuchung erstellt (`docx/oss-bom-2025-q4.docx` — nicht beigefügt, im Datenraum): 47 OSS-Komponenten verwendet, davon 38 unter MIT/Apache-2.0 (unbedenklich), 7 unter LGPL-3.0 (dynamisches Linking — unbedenklich für ein SaaS-Produkt ohne Distribution), 2 unter GPL-3.0 (geprüft: nur Build-Tools, nicht im distributierten Produkt — unbedenklich). **Keine GPL-Kontamination** der Hauptcodebase.

### 2.2 Markenrechte (DPMA-Eintragungen)

| Marke | Form | Reg.-Nr. | Klassen | Status |
|---|---|---|---|---|
| ChainCortex | Wortmarke | DE 30 2023 045 678 | 9, 42 | eingetragen, Verlängerung 2033 |
| BlockSight | Wortmarke | DE 30 2024 098 765 | 9, 42 | eingetragen, Verlängerung 2034 |
| ChainCortex (Logo) | Bildmarke | DE 30 2023 045 679 | 9, 42 | eingetragen, Verlängerung 2033 |

Eintragungen frei von Belastungen Dritter; keine Widerspruchsverfahren; keine Pfändungen.

### 2.3 Domains

- chaincortex.ai (Registrar: united-domains GmbH; KK frei)
- chaincortex.io (Registrar: GoDaddy)
- blocksight-sentinel.io (Registrar: GoDaddy)
- blocksight.de (Registrar: united-domains GmbH)

### 2.4 Know-how / Geschäftsgeheimnisse (GeschGehG § 2)

- Anlernpipelines für CCE-Modell (dokumentiert in `docs/training-pipeline.md` Repo `cce-core`)
- AML-Heuristik-Bibliothek (proprietär; nicht in öffentlich publizierten Whitepapers offengelegt)
- Modellgewichte: aktuelles Checkpoint (Q4/2025) im Repo `chaincortex/cce-checkpoints` (privat, ~3.2 GB)

Schutzmaßnahmen (für § 2 Nr. 1b GeschGehG): Verträge AN mit Verschwiegenheits- und Werkschöpfungsklauseln (siehe AN-Verträge im Datenraum); MFA + Branch-Protection + Need-to-Know-Prinzip.

## 3. Vertragslage (Auswahl)

| Typ | Vertragspartner | Status | Hinweise |
|---|---|---|---|
| SaaS-Kundenvertrag (B2B) | 12 aktive Kunden — siehe `xlsx/kundendaten-business.xlsx` | sämtlich gekündigt zum 31.07.2026 von Schuldnerseite (§ 103 InsO Wahlrechts-Verzicht des Verwalters); Voracis verhandelt Neuabschluss |
| SaaS-Kundenvertrag (B2C) | 8 aktive Privatkunden — siehe `xlsx/kundendaten-privat.xlsx` | analog gekündigt; Voracis bietet Neuabschluss + Datentransfer-Information |
| Miete Büroräume Linienstraße | Pebbo Immo GmbH | Kündigung Verwalter § 109 InsO; geräumt 30.06.2026 |
| Cloud-Hosting AWS (Frankfurt-Region) | AWS Inc. | wird vertraglich abgelöst; Voracis übernimmt neue Account-Hülle |
| Wartungsvertrag Hardware (Lenovo Workstations) | DataMid GmbH | bis 31.07.2026, Voracis übernimmt 7 Geräte separat (außerhalb dieses Asset Deals — Verkauf gegen Buchwert 4.200 EUR) |

## 4. Arbeitnehmer

12 Arbeitnehmer (Stand 01.04.2026). Übersicht in `xlsx/arbeitnehmer-uebernahmestatus.xlsx`. Davon:

- 10 Übernahmen geplant (§ 613a BGB Bereitschaft des Käufers)
- 2 Nicht-Übernahmen (Position Vertriebsleitung dual besetzt — Voracis-eigene Vertriebsleitung; sowie eine Stelle „Office Manager", in Voracis nicht vorgesehen).

Sozialplan-Bedarf für die 2 Nicht-Übernommenen: prüfen, ob Schwellenwerte des § 17 KSchG (Massenentlassungsanzeige) erreicht sind — bei 12 AN-Gesamtbelegschaft Schwelle gemäß § 17 I 1 Nr. 1 KSchG nicht erreicht (mehr als 5 AN bei weniger als 20 AN). **Anzeige nicht erforderlich**, aber individuelle Abfindungsverhandlungen über Sozialplan-Komponente vorbereitet (siehe `08_…`).

## 5. Kundendaten — DSGVO-Risikobewertung

Dies ist der **rechtlich heikelste Workstream**. Detailanalyse in `07_…`. Zusammenfassung:

- B2B-Kundendaten (12 juristische Personen): unproblematisch (keine personenbezogenen Daten i. S. d. Art. 4 Nr. 1 DSGVO, soweit nur Firmendaten; Ansprechpartner-Klardaten gelten nach EDSA-Stellungnahme als personenbezogen, aber unter Art. 6 I lit. f DSGVO durch berechtigtes Interesse gedeckt).
- B2C-Kundendaten (8 natürliche Personen): personenbezogene Daten i. S. d. Art. 4 Nr. 1 DSGVO. Rechtsgrundlage für **Übermittlung** an Voracis: Art. 6 I lit. f DSGVO + EuGH **C-732/22** (Bonprix, 26.09.2024) — Asset-Deal-Privileg streng auszulegen; Information nach Art. 14 DSGVO ist zwingend (im Anhang `eml/dsgvo-information-b2c-privatkunden-entwurf.eml`).

## 6. Steuerliche Würdigung (Geschäftsveräußerung im Ganzen — § 1 Ia UStG)

Da die übernommenen Assets einen lebensfähigen Betriebsteil ergeben (Software + Marken + AN + Kunden) — und der Käufer die Geschäftstätigkeit fortführen will (vgl. EuGH **C-497/01 Zita Modes** und **C-444/10 Schriever**, Übernommen in **BFH V R 11/13** v. 18.01.2017) — wird die Veräußerung als **Geschäftsveräußerung im Ganzen** behandelt. Folge: **kein Umsatzsteuerausweis** (§ 1 Ia UStG; § 15a UStG-Vorsteuerkorrektur greift, ist aber durch Übernahme der Berichtigungspflicht durch den Käufer gedeckt).

Steuerliche Stellungnahme: Steuerberater Walther Inkermann (WP Quintbeck, Berlin) — siehe `docx/giug-stellungnahme.docx` (nicht beigefügt; im Datenraum).

## 7. Risiken / Red Flags

| Risiko | Wahrscheinlichkeit | Wirkung | Maßnahme |
|---|---|---|---|
| DSGVO-Übertragung B2C-Daten greift nicht | mittel | EuGH-Bonprix-Standard verlangt Information; Bußgeldrisiko | siehe `07_…` — strikte Anwendung Art. 14 DSGVO, Widerspruchsmöglichkeit |
| Mitarbeiterwiderspruch § 613a VI BGB | gering | Verlust einzelner Schlüsselkräfte | Vorabklärung mit AN; siehe `08_…` |
| Markenrecht-Streit Wettbewerber „ChainSight Forensics" Hamburg | gering | Verwechslungsfähigkeit Frage | DPMA-Auskunft eingeholt 02.06.2026: keine Identitäts- oder Verwechslungsfälle anhängig |
| GoDaddy/Cloud-Account-Transfer Bottleneck | mittel | technischer Übergabeengpass | Closing-Checkliste 10_… |
| Rest-Gläubiger versuchen Anfechtung Vertrags-Beendigung Asset-Deal-konstruktion (§ 132 InsO) | sehr gering | Mass-anrechnung Rückabwicklung | § 132 InsO greift nicht (Verfahrenseröffnung 01.04.2026, Vertragsabschluss nach Eröffnung — keine vorinsolvenzliche Rechtshandlung) |
| Käufer-Finanzierung fällt aus | gering | Closing platzt | Equity-Letter 4.5 Mio. EUR Genmar Holding GmbH; Eskrow vereinbart |

## 8. Empfehlung Verwalter

Der Asset Deal mit Voracis Ventures GmbH zu einem Kaufpreis von [400.000,00 EUR] ist gegenüber den Alternativen (Stilllegung, Einzelverwertung, Verkauf an Pebbo Code Holding ohne AN-Übernahme) wirtschaftlich überlegen und entspricht dem höchstmöglichen Verwertungsergebnis im Sinne von § 159 InsO. Der Verwalter empfiehlt dem Gläubigerausschuss, der Veräußerung gemäß § 160 II Nr. 1 InsO zuzustimmen.
