# Storage and Database Options

## Opzioni di archiviazione

Principalmente, ci sono tre tipi di opzioni di archiviazione in Google Cloud, ognuna con i propri casi d'uso:

- **Cloud Storage**: per dati **non strutturati** (oggetti, blob, file, ecc.)
- **Filestore**: per **archiviazione di file** (NFS)
- **Persistent Disk**: per **archiviazione a blocchi** (come un hard disk)

![Opzioni di archiviazione](../images/03_Storage_and_Database_Options_01.png)

**NOTA**:

- **Object storage** è un'architettura di archiviazione dati che non è collegata alla tua istanza e archivia il tuo sistema operativo e le applicazioni, invece, viene utilizzata per gestire i dati come oggetti, come documenti, foto, video e altri file.
- Non va confusa con **Block storage**, una capacità di archiviazione grezza, che viene utilizzata nei dispositivi collegati a un sistema operativo.

### Cloud Storage

**Cloud Storage** è un'archiviazione di oggetti coerente, scalabile, di grande capacità e altamente durevole.

Ha una **durabilità di 11 9** (99,999999999%), il che significa che se archivi 1 milione di oggetti, statisticamente puoi aspettarti di perdere un file ogni 659.000 anni.

Una delle grandi caratteristiche di Cloud Storage è l'**archiviazione illimitata** senza dimensione minima degli oggetti. Quindi, è un'ottima opzione per **consegna di contenuti, data lake e backup**.

Infine, è disponibile in diverse **classi di archiviazione** e **disponibilità**.

Per quanto riguarda le **classi di archiviazione**, ci sono quattro tipi:

- **Standard**: È ottimo per archiviare dati a cui si accede frequentemente.
  - Massima disponibilità e prestazioni
- **Nearline**: È ottimo per archiviare dati a cui si accede meno di una volta al mese.
  - Archiviazione di archiviazione a basso costo
- **Coldline**: È ottimo per archiviare dati a cui si accede meno di una volta al trimestre.
  - Archiviazione di archiviazione a costo ancora più basso
- **Archive**: È ottimo per archiviare dati a cui si accede meno di una volta all'anno.
  - Archiviazione di archiviazione a costo più basso

Per quanto riguarda la **disponibilità**, ci sono tre tipi:

- **Region** (Single-region): I dati vengono archiviati in una singola regione.
- **Dual-region**: I dati vengono archiviati in due regioni.
- **Multi-region**: I dati vengono archiviati in più regioni.

### Filestore

**Filestore** è un server di file **NFS (Network File System)** completamente gestito, compatibile con NFS v3.

Puoi archiviare dati da applicazioni in esecuzione, istanze VM multiple e cluster Kubernetes, accedendo ai dati contemporaneamente.

È una buona opzione quando è necessario accedere ai dati da un gruppo di istanze e sono necessarie più istanze per accedere agli stessi dati.

### Persistent Disk

**Persistent Disk** è un'archiviazione a blocchi durevole per le istanze. Offre due opzioni diverse:

- **Standard Persistent Disk**: È un **HDD** (Hard Disk Drive) che è buono per la lettura/scrittura sequenziale.
- **SSD Persistent Disk**: È un **SSD** (Solid State Drive) che è buono per la lettura/scrittura casuale.

Entrambe le opzioni sono disponibili in opzioni zonali e regionali.

## Opzioni di database

Google Cloud offre una varietà di opzioni di database, che possono essere suddivise in due categorie principali:

- **Database relazionali**: come MySQL, PostgreSQL e SQL Server.
- **Database NoSQL**: come Cloud Bigtable, Firestore e Cloud Spanner.

![Opzioni di database](../images/03_Storage_and_Database_Options_02.png)

### Database relazionali

- **Cloud SQL** è un servizio di database relazionale completamente gestito che supporta MySQL, PostgreSQL e SQL Server. Ha alta disponibilità tra le zone.
- **Cloud Spanner** è un servizio di database relazionale scalabile che supporta transazioni, consistenza forte e replica sincrona ed è ad alta disponibilità tra le regioni e globalmente.

### Database NoSQL

- **Cloud Bigtable** è un servizio di database NoSQL completamente gestito e scalabile, con un'elevata velocità di trasferimento e bassa latenza. Offre la flessibilità di ridimensionare il cluster senza tempi di inattività.
- **Cloud Datastore** è un servizio di database documentale NoSQL veloce, completamente gestito e serverless. È progettato per applicazioni mobili, web, IoT e ha la capacità di replicazione multi-regione e transazioni *ACID*.
- **Cloud Firestore** è un servizio di database NoSQL in tempo reale ottimizzato per l'uso offline. Offre il ridimensionamento del cluster senza tempi di inattività.
- **Cloud Memorystore** è un servizio altamente disponibile in memoria per Redis e Memcached ed è un servizio completamente gestito, in cui Google gestisce il servizio per te.