# Cloud DNS

**NOTA:** Questo viene visualizzato solo nell'esame a un livello elevato.

**Cloud DNS** è un servizio completamente gestito che gestisce i server DNS per le tue zone specifiche.

Funziona come un **server DNS autoritativo** per le zone pubbliche, che sono visibili su Internet, e le zone private, che sono visibili solo alle tue reti VPC. Viene anche chiamato **DNS come servizio**.

Cloud DNS dispone di server che si estendono in tutto il mondo, rendendolo un servizio **globalmente resiliente**, ed è anche altamente disponibile, con un SLA di uptime del 100%.

Per utilizzare Cloud DNS con un dominio pubblicamente disponibile specifico, è necessario acquistare un nome di dominio tramite un registrar di domini, e è possibile registrare un dominio tramite Google Domains o qualsiasi altro registrar di domini. Quindi, non è possibile registrare un dominio tramite Cloud DNS, ma è possibile utilizzare Cloud DNS per gestire i record DNS per quel dominio.

Offre la flessibilità di ospitare:

- **Zona pubblica**: visibile su Internet.
- **Zona privata**: visibile solo alle tue reti VPC.

**NOTA:** La rete VPC che autorizzi a utilizzare la zona privata deve trovarsi nello stesso progetto della zona privata.

Ogni zona gestita che crei è associata a un progetto di Google Cloud, e una volta creata questa zona è ospitata dai server di nomi gestiti da Google. Queste zone sono sempre ospitate sui server di nomi gestiti da Google, all'interno di Google Cloud, quindi creeresti record e insiemi di record, e questi server diventerebbero quindi allocati a quella specifica zona che ospita i tuoi record e insiemi di record.

**Osservazione:** Un **insieme di record** è una collezione di record DNS in una zona che hanno lo stesso nome e tipo.

## Demo

A video demo is available [here](https://youtu.be/jpno8FSqpc8?si=V_4Nc0V9y0RXIOEE&t=35004).

1. Go to **Newotk Services** > **Cloud DNS**.
2. Click on **Create Zone**, and fill in the details.
   - Zone type: `Private`.
     - Zone name: `tonybowtie`.
     - DNS name: `tonybowtie.private`.
     - Description: `Tony's private zone`.
     - Optional: `Default (private)`.
     - Network: `default`.
3. Click on **Create**.

The same process can be done with command line:

```bash
gcloud beta dns 
    --project=tonybowtieinc 
    managed-zones create tonybowtie 
        --description="Tony's private zone"
        --dns-name=tonybowtie.private
        --visibility=private
        --networks=default 
```

In the following image, you can see the newly created zone, with some DNS records.

In the **IN USE BY** tab, you can see the VPC networks that are using this private zone.

![Cloud DNS GCP Console](images/14_Cloud_DNS_01.png)

**NOTE for the exame:** When creating a zone these records are always created by default:

- **SOA**: Start of Authority.
- **NS**: Name Server.

