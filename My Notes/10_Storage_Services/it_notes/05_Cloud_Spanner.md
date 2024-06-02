# Cloud Spanner

Cloud Spanner è un database relazionale globale di Google Cloud, che è simile in alcuni modi a Cloud SQL, per quanto riguarda le transazioni ACID, le query SQL e la consistenza forte, ma differisce nel modo in cui i dati vengono gestiti internamente rispetto a Cloud SQL.

- **Cloud Spanner** è un *servizio di database relazionale completamente gestito* che è sia *consistentemente forte* che *scalabile in modo orizzontale*.

- Cloud Spanner è un altro offerta di Database as a Service (*DBaaS*) di Google, quindi elimina tutti i problemi di configurazione e manutenzione dell'infrastruttura e del software necessari per eseguire il database nel cloud.

- Supporta schemi, transazioni ACID, query SQL.
  - Essere consistentemente forti in questo contesto significa che i dati vengono passati a tutte le repliche non appena una richiesta di scrittura arriva a una delle repliche del database.
  - Cloud Spanner utilizza *truetime*, un sistema di orologio atomico distribuito altamente disponibile fornito alle applicazioni su tutti i server di Google.
  - Applica un timestamp a ogni transazione al momento del commit, quindi le transazioni in altre regioni vengono sempre eseguite in sequenza.

- *Distribuzione globale*
  - Cloud Spanner può distribuire e gestire dati su scala globale e supportare letture globalmente coerenti insieme a transazioni distribuite consistentemente forti.

- Gestisce *repliche* e *sharding*
  - Cloud Spanner gestisce tutte le repliche necessarie per la disponibilità dei dati e ottimizza le prestazioni suddividendo automaticamente i dati in base al carico delle richieste e alla dimensione dei dati.

- Replica sincrona dei dati
  - Parte della disponibilità elevata di Cloud Spanner è dovuta alla sua replica sincrona automatica dei dati tra tutte le repliche e le zone indipendenti.

- *Scaling automatico* e *ridondanza dei nodi*
  - Cloud Spanner si scala automaticamente in modo orizzontale all'interno delle regioni, ma può anche scalare tra le regioni per carichi di lavoro con requisiti di disponibilità più elevati, rendendo i dati disponibili più velocemente agli utenti e su scala globale, insieme a una ridondanza nota, aggiunta silenziosamente per ogni nodo distribuito nell'istanza.

- Fino a *5 nove di disponibilità*
  - è possibile raggiungere una disponibilità di 5 nove su un'istanza multi-regionale e una disponibilità di 4 nove su un'istanza regionale.

- Crittografia del livello dei dati, registrazione delle attività e integrazione IAM
  - Cloud Spanner è altamente sicuro e offre crittografia del livello dei dati, registrazione delle attività e integrazione IAM.

- Cloud Spanner è stato progettato per soddisfare le esigenze di settori specifici come servizi finanziari, ad tech, vendita al dettaglio e catena di approvvigionamento globale, insieme al gaming.

- *Prezzo* per Cloud Spanner, è di $0,90 per nodo all'ora con il costo dello storage di $0,30 per gigabyte al mese.
  - Sicuramente non economico, ma le funzionalità sono abbondanti.

## Istanza (Nota richiesta per l'esame)

Per utilizzare Cloud Spanner, è necessario prima creare un'**istanza di Cloud Spanner**.

Questa istanza è un'allocazione di risorse utilizzata dai database di Cloud Spanner creati in quell'istanza.

La creazione dell'istanza include due scelte importanti:

- La **configurazione dell'istanza**
  - Queste scelte determinano la posizione e la quantità di CPU e memoria dell'istanza insieme alle risorse di archiviazione.
  - La scelta della configurazione è permanente per un'istanza e solo il numero di nodi può essere modificato successivamente, se necessario.
  - Una configurazione dell'istanza definisce il posizionamento geografico e la replica del database in quell'istanza, sia regionale che multi-regionale.
  - **NOTA:** Quando si sceglie una configurazione multi-zona, consente di replicare i dati del database non solo in più zone, ma anche in più zone in diverse regioni.

- Il **numero di nodi**
  - Questo determina il numero di nodi da allocare a quell'istanza.
  - Questi nodi allocano la quantità di CPU, memoria e archiviazione necessaria per l'istanza per aumentare la capacità di throughput o di archiviazione.

Non ci sono tipi di istanze tra cui scegliere come in Cloud SQL, quindi quando hai bisogno di più potenza, aggiungi semplicemente un altro nodo.

Per qualsiasi configurazione regionale, Cloud Spanner mantiene esattamente tre repliche di lettura/scrittura, ognuna in una diversa zona di quella regione.

Ogni replica di lettura/scrittura contiene una copia completa del tuo database operativo in grado di gestire richieste di lettura/scrittura e di sola lettura.

Cloud Spanner utilizza repliche in diverse zone, quindi se si verifica un guasto in una singola zona, il tuo database rimane disponibile.

In una configurazione di istanza multi-regionale, all'istanza vengono assegnate una combinazione di quattro repliche di lettura/scrittura e di sola lettura.

**NOTA:** Google raccomanda un minimo di 3 nodi di configurazione per la produzione.

![Cloud Spanner](../images/05_Cloud_Spanner_01.png)
Come Cloud Spanner viene popolato con i dati, avviene lo sharding, noto anche come **split**, Cloud Spanner crea repliche di ogni split del database per migliorare le prestazioni e la disponibilità.

Tutti i dati in uno split vengono fisicamente memorizzati insieme in una replica.

Cloud Spanner serve ogni replica da una zona di guasto indipendente e all'interno di ogni set di repliche, una replica viene eletta a **leader**.

Le repliche leader sono responsabili della gestione delle scritture, mentre qualsiasi replica di sola lettura o lettura/scrittura conserva le richieste di lettura senza comunicare con il leader.

![Cloud Spanner](../images/05_Cloud_Spanner_02.png)

## Performance

- Ogni nodo Cloud Spanner può fornire fino a 10.000 query al secondo, o QPS di letture, o 2000 QPS di scritture.
- Ogni nodo fornisce fino a due terabyte di storage.
  - Se hai bisogno di aumentare le risorse di servizio e storage nella tua istanza, *aggiungi più nodi a quell'istanza*
- Aggiungere un nodo non aumenta il numero di repliche, ma aumenta le risorse che ogni replica ha nell'istanza
  - Aggiungere nodi fornisce a ogni replica CPU e RAM, che *aumenta il throughput delle repliche*
- Se stai cercando di *scalare automaticamente*, puoi scalare il numero di nodi nella tua istanza in base alle metriche di monitoraggio del cloud su CPU o utilizzo dello storage in combinazione con l'uso di Cloud Functions per attivare.
  - Quindi, quando devi decidere su un database relazionale che fornisce distribuzione globale e scalabilità orizzontale che gestisce carichi di lavoro transazionali in Google Cloud, Cloud Spanner sarà sempre la scelta ovvia rispetto a Cloud SQL.