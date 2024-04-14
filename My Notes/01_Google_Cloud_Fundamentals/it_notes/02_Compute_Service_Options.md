# Opzioni di servizio di calcolo

![Opzioni di servizio di calcolo](../images/02_Compute_Service_Options_01.png)

## Compute Engine

**Compute Engine** è una **macchina virtuale** che viene eseguita sull'infrastruttura di Google. È un servizio **IaaS** che consente di creare ed eseguire **macchine virtuali** sull'infrastruttura di Google chiamate **istanze**.

È possibile creare **macchine virtuali** con diverse configurazioni ed eseguire su di esse diversi sistemi operativi, nonché distribuirle in diverse regioni e zone.

È possibile utilizzare immagini **pubbliche** o **private** per creare **macchine virtuali**, e sono disponibili anche immagini preconfigurate e pacchetti software nel **Google Cloud Marketplace**.

Nel Compute Engine è possibile:

- gestire più istanze utilizzando **gruppi di istanze**.
- aggiungere/rimuovere capacità utilizzando **autoscaling** con **gruppi di istanze**.
- collegare/scollegare **dischi** alle istanze.
  - Google Cloud Storage può essere utilizzato in combinazione con Compute Engine per archiviare i dati.

Per connettersi alla **macchina virtuale**, è possibile utilizzare **SSH**.


## Kubernetes Engine

**Kubernetes Engine** è un sistema di orchestrazione dei contenitori per automatizzare il rilascio, la scalabilità e la gestione dei contenitori.

È basato su **Kubernetes**, un sistema di orchestrazione dei contenitori open source.
Quindi, può essere descritto come un **servizio Kubernetes gestito** che consente di eseguire **cluster Kubernetes** sull'infrastruttura di Google.

Sotto il cofano, GKE utilizza istanze di **Compute Engine** come **nodi** nel **cluster Kubernetes** (gruppo di nodi).

È un servizio **CaaS**, ovvero **Containers as a Service**.

## App Engine

**App Engine** è una piattaforma serverless completamente gestita (**PaaS**, Platform as a Service) per lo sviluppo e l'hosting di applicazioni web su larga scala.

Con App Engine, Google si occupa della maggior parte della gestione delle risorse per te, ad esempio:

- se la tua applicazione richiede più risorse di calcolo perché il traffico al tuo sito web aumenta, Google scala automaticamente il sistema per fornire più risorse.
- se il software di sistema deve essere aggiornato, Google lo aggiorna automaticamente.

Quindi lo sviluppatore può concentrarsi sulla scrittura del codice e sul rilascio delle applicazioni, utilizzando diversi linguaggi di programmazione.

Infine, è collegato ad altri servizi di Google (o servizi di terze parti) **in modo trasparente**, e si **integra** con Web Security Scanner per identificare le minacce.

## Cloud Functions

**Cloud Functions** è un servizio **FaaS** (Function as a Service), ovvero un ambiente di esecuzione serverless per la creazione e la connessione di servizi cloud.

Con Cloud Function è possibile scrivere **funzioni a scopo specifico** che sono **collegate a eventi** emessi dalla tua infrastruttura e dai tuoi servizi cloud. Infatti, una funzione viene attivata quando viene generato un evento in ascolto, e il codice viene eseguito in un ambiente completamente gestito, quindi non è necessario fornire alcuna infrastruttura.

L'utente può scrivere il codice in diversi linguaggi di programmazione, come **JavaScript**, **Python**, **Go** o **Java**.

Le Cloud Functions sono utili nei seguenti **casi d'uso**:

- Elaborazione dati o operazioni ETL (trascodifica video, analisi immagini, ecc.)
- Webhook per rispondere a trigger HTTP
- API che compongono logica debolmente accoppiata
- Funzioni di backend mobile

## Cloud Run

**Cloud Run** è una piattaforma di calcolo completamente gestita per il rilascio e la scalabilità rapida e sicura di applicazioni containerizzate.

È costruito su uno standard aperto chiamato **Knative**, che è una piattaforma basata su Kubernetes per la creazione, il rilascio e la gestione di carichi di lavoro serverless moderni. Quindi **astrae** completamente la gestione dell'infrastruttura, scalando automaticamente le istanze per soddisfare la domanda.

È un servizio **FaaS**, ovvero **Function as a Service**, perché è serverless per i container.