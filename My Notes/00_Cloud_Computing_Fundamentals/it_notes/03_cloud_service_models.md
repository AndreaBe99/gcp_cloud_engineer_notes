# Cloud Service Models

## XaaS

**Everything as a Service (XaaS)** è un termine di cloud computing che indica una varietà di servizi e applicazioni a cui gli utenti possono accedere tramite internet, anziché fare affidamento esclusivamente su server locali o dispositivi personali per gestire le applicazioni.

Quando si tratta di distribuire un'applicazione, questa viene distribuita in uno stack di infrastruttura composto da diversi livelli.

![Modelli di servizio cloud](../images/03_cloud_service_models_01.png)

Uno **stack** è una collezione di infrastrutture necessarie per far funzionare l'applicazione. È stratificato e ogni livello si basa sul precedente.

Questo stack può essere diviso in due parti:

- una gestita dal fornitore di cloud
- una gestita dal cliente

**Prezzato per unità di consumo**: come il fornitore di servizi stabilisce il prezzo del servizio che offre ai propri clienti.

## Data Center Hosted

In questo modello il data center è gestito dal fornitore, mentre il cliente è responsabile del resto dello stack.

In questo modello, il fornitore di cloud è responsabile di tutto ciò che riguarda il data center, come i rack, l'alimentazione dei rack, il raffreddamento, i cavi di rete fuori dal data center, la sicurezza fisica, ecc.

Quindi, in questo caso, l'**unità di consumo** è lo spazio del rack nel data center.

## IaaS

Nel modello **Infrastructure as a Service (IaaS)**, tutti i livelli dal data center fino al livello di virtualizzazione sono gestiti dal fornitore di cloud. Il cliente è responsabile del resto dello stack.

Questo è il modello più basilare, che essenzialmente consiste in una macchina virtuale in esecuzione nel cloud. In Google Cloud Platform, questo viene chiamato **Compute Engine**.

In questo caso, l'**unità di consumo** è il sistema operativo in esecuzione sulla macchina virtuale.

## PaaS

Nel modello **Platform as a Service (PaaS)**, il fornitore di cloud è responsabile di tutto fino al livello di runtime. Il cliente è responsabile del resto dello stack.

In questo modello, il fornitore fornisce una piattaforma di calcolo che include un sistema operativo, un ambiente di esecuzione per linguaggi di programmazione, un database e un server web. Il cliente non deve preoccuparsi degli aggiornamenti del sistema operativo o della gestione del runtime o del middleware. In Google Cloud Platform, questo viene chiamato **App Engine**.

In questo caso, l'**unità di consumo** è il runtime.

## SaaS

Nel modello **Software as a Service (SaaS)**, il fornitore di cloud è responsabile di tutto fino al livello dell'applicazione.

In questo modello, il fornitore fornisce l'applicazione software che il cliente utilizza. Il cliente non deve preoccuparsi degli aggiornamenti del sistema operativo, del runtime, del middleware o dell'applicazione stessa. In Google Cloud Platform, questo viene chiamato **G Suite**.