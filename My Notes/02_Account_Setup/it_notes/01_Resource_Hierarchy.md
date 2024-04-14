# Gerarchia delle risorse

Nel contesto di Google Cloud, una **Risorsa** può riferirsi a:

- le risorse a livello di servizio utilizzate per elaborare i carichi di lavoro, come:

  - Compute Instances VMs
  - Cloud Storage Buckets
  - Cloud SQL Databases

- le risorse a livello di account che si trovano sopra il servizio, come:

  - Organizzazioni
  - Cartelle
  - Progetti

La **Gerarchia delle risorse** è il modo di Google Cloud per configurare e concedere l'accesso alle varie risorse cloud per la tua organizzazione, sia a livello di servizio che di account. Può veramente definire le autorizzazioni granulari necessarie per gestire le tue risorse.

Le risorse sono organizzate in modo gerarchico, in una relazione padre-figlio, in cui la risorsa padre può concedere l'accesso alle risorse figlio. È progettato per mappare la struttura organizzativa su Google Cloud e per gestire il controllo degli accessi e le autorizzazioni per gruppi di risorse correlate.

Le politiche sono controllate da **IAM** (Identity and Access Management), quindi quando le politiche IAM vengono impostate a un livello superiore nella gerarchia, vengono **ereditate** dai livelli inferiori.

**NOTA**: Ogni oggetto figlio ha esattamente un genitore e ogni genitore può avere più figli.

![Gerarchia delle risorse](../images/01_Resource_Hierarchy_01.png)


## Domain

Il **Dominio** è il livello superiore della gerarchia ed è il nodo radice della gerarchia. È il livello più alto della gerarchia ed è il genitore di tutte le altre risorse nella gerarchia.

Qui gestiamo gli utenti nella nostra organizzazione e sono collegati a account G-Suite o Cloud Identity.

## Organization

L'**Organizzazione** è il secondo livello della gerarchia e rappresenta l'organizzazione ed è il nodo radice della gerarchia delle risorse di GCP.

È associata esattamente a un dominio e tutte le politiche impostate a livello di organizzazione vengono ereditate da tutte le risorse al di sotto di essa.

## Folders

Le **Cartelle** sono un meccanismo di raggruppamento aggiuntivo e un confine di isolamento tra ogni progetto, in sostanza, è un raggruppamento di cartelle, progetti e risorse.

Quindi, se ci sono diversi dipartimenti e team nell'organizzazione, possono essere raggruppati in cartelle e le cartelle possono essere nidificate per creare una gerarchia.

Per utilizzare una cartella è necessario avere un nodo di organizzazione e mentre una cartella può contenere più cartelle o risorse, una cartella o risorsa può avere solo un genitore.

## Projects

I **Progetti** sono il livello più basso della gerarchia e vengono utilizzati per organizzare le risorse e gestire la fatturazione.

Qualsiasi risorsa può appartenere solo a un progetto e tutte le risorse devono appartenere a un progetto.

## Risorse

Le **Risorse** sono le risorse a livello di servizio utilizzate per elaborare i carichi di lavoro.

## Labels

Le **Labels** sono coppie chiave-valore che possono essere associate alle risorse e possono essere utilizzate per organizzare le risorse e filtrare e raggruppare le risorse.

Infine, possiamo fare una distinzione tra **Risorse a livello di account** e **Risorse a livello di servizio**:

- **Risorse a livello di account** sono le risorse che si trovano sopra le risorse a livello di servizio, come Organizzazioni, Cartelle e Progetti.

- **Risorse a livello di servizio** sono le risorse utilizzate per elaborare i carichi di lavoro, come Compute Instances VMs, Cloud Storage Buckets e Cloud SQL Databases.