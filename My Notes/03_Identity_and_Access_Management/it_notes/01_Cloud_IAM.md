# Cloud IAM

## Principi del privilegio minimo

**Un utente, un programma o un processo dovrebbe avere solo i privilegi minimi necessari per svolgere la propria funzione.**

Ad esempio, se un utente esegue una funzione di creazione su un bucket di archiviazione cloud, l'utente dovrebbe essere limitato a creare oggetti solo su un bucket di archiviazione.

![Principio del privilegio minimo](../images/01_Cloud_IAM_01.png)

## Identity and Access Management

**Identity and Access Management (IAM)** consente di gestire il controllo degli accessi definendo **chi** (identità) ha **quali** accessi (ruolo) per **quali** risorse. IAM è un componente fondamentale di Google Cloud ed è essenziale comprendere come funziona per proteggere le risorse.

![Principio del privilegio minimo](../images/01_Cloud_IAM_02.png)

Include anche organizzazione, cartella e progetto.

Nelle autorizzazioni IAM, l'accesso alle risorse non viene concesso direttamente agli utenti, ma **le autorizzazioni vengono raggruppate in ruoli** e i ruoli vengono concessi ai membri autenticati.

Le politiche IAM definiscono e applicano i ruoli concessi ai membri e queste politiche sono collegate a una risorsa.

Quindi, quando un membro autenticato cerca di accedere a una risorsa, IAM controlla le politiche collegate alla risorsa per determinare se il membro ha le autorizzazioni necessarie.

## Architettura delle politiche

![Architettura delle politiche](../images/01_Cloud_IAM_03.png)

Una **politica** è una collezione di **binding**, **configurazione di audit** e altri **metadati** che descrivono quali **ruoli** vengono concessi a quali membri.

- I **binding** specificano come deve essere concesso l'accesso alle risorse e collegano uno o più membri a un singolo ruolo e a eventuali condizioni specifiche del contatto che modificano come e quando viene concesso il ruolo.
- I **metadati** includono informazioni aggiuntive sulla politica, come ad esempio un etag, che è un identificatore univoco per la politica, e un numero di versione, per facilitare la gestione delle politiche.
- La **configurazione di audit** specifica i dati di configurazione su come devono essere registrati i tentativi di accesso.

### Membri

Un **membro** è un'**identità** che può accedere a una risorsa. Quindi, l'identità di un membro è un indirizzo email associato a un utente, a un account di servizio o a un gruppo di Google, o addirittura a un nome di dominio associato a un dominio di G Suite o di identità cloud.

- **Account Google**: Rappresenta qualsiasi persona che interagisce con Google Cloud, ovvero qualsiasi indirizzo email associato a un account Google può essere un'identità, inclusi `gmail.com` o altri domini.

- **Account di servizio**: È un account che appartiene alla tua applicazione anziché a un singolo utente finale. Quindi, quando esegui il tuo codice ospitato su GCP, questa è l'identità che specifici per eseguire il tuo codice.

- **Gruppo di Google**: È una raccolta nominata di account Google e account di servizio. Il vantaggio dei gruppi di Google è che puoi concedere e modificare le autorizzazioni per più utenti contemporaneamente.

- **Dominio G Suite**: Rappresenta il dominio Internet dell'organizzazione (ad esempio `example.com`) e quando aggiungi un utente al tuo dominio G Suite, ottiene un account Google con lo stesso nome. Rappresenta un gruppo virtuale di tutti gli account Google che sono stati creati. Come i gruppi di Google, i domini G Suite non possono essere utilizzati per stabilire l'identità, ma consentono semplicemente la gestione delle autorizzazioni.

- **Dominio di identità cloud**: È simile a un dominio G Suite, ma la differenza è che gli utenti non hanno accesso alle applicazioni e alle funzionalità di G Suite.

**NOTA:**

- **Tutti gli utenti autenticati**: È un identificatore speciale che rappresenta qualsiasi utente autenticato con un account Google.

- **Tutti gli utenti**: È un identificatore speciale che rappresenta qualsiasi utente, inclusi gli utenti non autenticati.

### Ruoli

I **ruoli** sono una **raccolta nominata di autorizzazioni** che concedono l'accesso per eseguire determinate azioni sulle risorse.

**Autorizzazioni**:

- Determinano quali operazioni sono consentite su una risorsa.
- Di solito (ma non sempre) corrispondono **uno a uno con i metodi delle API REST**.
- Non vengono concesse direttamente agli utenti.
  - Concedi un ruolo a un utente e tutte le autorizzazioni contenute nel ruolo.
- Concedi ruoli che contengono una o più autorizzazioni.
- È possibile creare ruoli personalizzati, combinando una o più delle autorizzazioni AIM disponibili.

Le autorizzazioni sono definite nella forma `servizio.risorsa.azione`, ad esempio `compute.instance.list`.

Ci sono tre tipi di ruoli in IAM:

1. **Ruoli primitivi**:
   - Questi ruoli sono i ruoli di base che esistevano quando IAM è stato introdotto per la prima volta.
   - Sono:
     - `Owner`, include le autorizzazioni dei ruoli `Editor` e `Viewer`.
     - `Editor`, include le autorizzazioni del ruolo `Viewer`.
     - `Viewer`
   - Questi ruoli **non sono consigliati** per l'uso in produzione perché concedono un ampio accesso a tutte le risorse in un progetto.

2. **Ruoli predefiniti**:
   - Questi ruoli sono mantenuti da Google Cloud e concedono l'accesso a risorse specifiche e a un insieme predefinito di autorizzazioni.
   - Sono:
     - `roles/owner`
     - `roles/editor`
     - `roles/viewer`.
   - Vengono aggiunti nuovi ruoli man mano che vengono aggiunti nuovi servizi a Google Cloud.

3. **Ruoli personalizzati**:
   - Questi ruoli sono definiti dall'utente e concedono l'accesso a risorse specifiche e a un insieme personalizzato di autorizzazioni.
   - A differenza dei ruoli predefiniti, non sono mantenuti da Google Cloud.
   - Quando crei un ruolo personalizzato, devi scegliere un'organizzazione o un progetto in cui crearlo, quindi puoi concedere il ruolo personalizzato all'organizzazione o al progetto e a tutte le risorse all'interno dell'organizzazione o del progetto.
     - *Non puoi creare ruoli personalizzati a livello di cartella*. Se devi definire un ruolo personalizzato per una cartella, devi definirlo sul genitore di quella cartella.
   - Solo i proprietari del progetto possono creare ruoli personalizzati.
   - Una caratteristica dei ruoli personalizzati è la **fase di lancio**, che indica il livello di supporto per il ruolo.
     - **Alpha**: Il ruolo è ancora in fase di test.
     - **Beta**: Il ruolo è stato testato ed è in attesa di approvazione.
     - **GA**: Il ruolo è disponibile e completamente supportato.

### Condizione

Una **condizione** è un'**espressione logica** utilizzata per definire e applicare un controllo degli accessi *condizionale* e *basato su attributi* per le risorse di Google Cloud.

Le condizioni consentono di concedere l'accesso alle risorse solo alle identità (membri) se vengono soddisfatte le condizioni configurate.

Ad esempio, ciò potrebbe essere fatto per configurare l'accesso temporaneo per gli utenti che sono appaltatori e hanno ricevuto un accesso specifico per un periodo di tempo specifico. Una condizione potrebbe essere messa in atto per rimuovere l'accesso di cui hanno bisogno una volta terminato il contratto.

Le condizioni vengono specificate nel binding del ruolo di una politica IAM di una risorsa.

Quando esiste una condizione, la richiesta di accesso viene concessa solo **se l'espressione della condizione viene valutata come vera**.

### Metadati

Questo componente contiene sia l'**etag** che la **versione** della politica.

- **etag**: È un identificatore univoco per la politica.
  - *Per evitare una condizione di gara durante l'aggiornamento della politica, IAM supporta il controllo della concorrenza tramite l'uso di un campo etag nella politica.*
    - Quando più sistemi cercano di scrivere contemporaneamente la stessa politica IAM, c'è il rischio di sovrascrivere le modifiche reciproche. L'etag viene utilizzato per evitare che ciò accada.
- **versione**: È un numero che viene incrementato ogni volta che la politica viene aggiornata.
  - Per evitare di interrompere le integrazioni esistenti nelle nuove versioni delle funzionalità che si basano sulla coerenza nella struttura della politica, vengono introdotte nuove versioni dello schema delle politiche.

### Configurazione di audit

Il componente di configurazione di audit viene utilizzato per configurare la registrazione degli audit per la politica.

Determina quali tipi di autorizzazioni vengono registrati e quali identità, se presenti, sono esentate dalla registrazione.

## Ereditarietà delle politiche

È possibile impostare una politica IAM in qualsiasi livello della gerarchia delle risorse e le risorse ereditano le politiche dalle risorse genitore.

La politica effettiva per una risorsa **è l'unione** della politica impostata sulla risorsa e delle politiche ereditate dalle risorse genitore.

**NOTA:** Le politiche a livello di organizzazione si applicano anche a livello di risorsa.

Ad esempio, se si applica una politica a `Progetto X`, tutte le risorse all'interno di quel progetto erediteranno la politica.

![Ereditarietà delle politiche](../images/01_Cloud_IAM_04.png)

## Demo

È possibile trovare una demo video dei concetti IAM [qui](https://youtu.be/jpno8FSqpc8?si=GwX8rTLDLGgdN3Z4&t=17252).

1. Vai alla pagina `IAM e amministrazione` utilizzando il menu laterale sinistro.

Ora spieghiamo ogni voce di menu nel menu laterale sinistro:

- La pagina `IAM` è dove è possibile aggiungere o modificare le autorizzazioni relative ai membri e ai ruoli per la politica aggiunta al proprio progetto.
  - Per aggiungere un membro, fare clic su `Aggiungi` e quindi inserire l'indirizzo email del membro che si desidera aggiungere.
  - Per aggiungere un'autorizzazione al nuovo membro, è possibile utilizzare la riga di comando, eseguire il seguente comando:

    ```bash
    gcloud projects add-iam-policy-binding [PROJECT_ID] --member=[MEMBER] --role=[ROLE]
    ```

    Questo comando aggiungerà il ruolo al membro.

  ![Console IAM](../images/01_Cloud_IAM_05.png)

- La pagina `Identità e organizzazione` è dove è possibile gestire Cloud Identity, ovvero una soluzione di identità come servizio di Google Cloud che consente di creare e gestire utenti e gruppi all'interno di Google Cloud.

- La pagina `Politiche dell'organizzazione` è dove è possibile impostare politiche a livello di organizzazione che si applicano a tutti i progetti dell'organizzazione.

- La pagina `Quote` è dove è possibile visualizzare e gestire le quote per il proprio progetto (vedi [Limiti e quote](../02_Account_Setup/10_Limits_and_Quotas.md)).

- La pagina `Account di servizio` è dove è possibile creare e gestire gli account di servizio.

- La pagina `Etichette` è dove è possibile creare e gestire le etichette per le proprie risorse. Sono coppie chiave-valore che è possibile associare alle risorse per aiutare a organizzarle e identificarle.

- La pagina `Impostazioni` è dove è possibile gestire le impostazioni per il proprio progetto, ad esempio cambiare il nome del progetto, vedere il numero del progetto e l'ID del progetto, migrare o chiudere il progetto.

- La pagina `Privacy e sicurezza` è dove Google fornisce a tutti i clienti di Google Cloud la conformità necessaria per soddisfare le normative in tutto il mondo e gli standard del settore, come ad esempio il settore sanitario e l'istruzione.

- La pagina `Identity Aware Proxy` è dove è possibile gestire l'accesso alle applicazioni e alle VM cloud senza una VPN.

- La pagina `Ruoli` è dove è possibile visualizzare e gestire i ruoli per il proprio progetto. Ad esempio, è possibile creare ruoli, ruoli personalizzati e si ha accesso a tutte le autorizzazioni.

- La pagina `Log di audit` è dove è possibile abilitare i log automatici senza dover utilizzare una politica specifica, semplicemente facendo clic su `Configurazione predefinita automatica` e quindi selezionando o deselezionando le caselle di controllo per i log che si desidera abilitare o disabilitare.
  - **NOTA:** Evitare di abilitare tutti i log perché può generare una grande quantità di dati e può superare rapidamente la quota.

  - Per scrivere la configurazione dei log di audit utilizzando la riga di comando, è possibile utilizzare il seguente comando:

    ```bash
    gcloud projects get-iam-policy [PROJECT_ID] > policy.yaml
    ```

    Questo comando scriverà la politica in un file chiamato `policy.yaml` nella directory corrente, quindi è possibile incollare la sezione di configurazione dei log di audit (`auditConfigs`) nel file.

    Per scrivere la politica nuovamente nel progetto, è possibile utilizzare il seguente comando:

    ```bash
    gcloud projects set-iam-policy [PROJECT_ID] policy.yaml
    ```

    Questo comando scriverà nuovamente la politica nel progetto.

- La pagina `Gruppi` è dove è possibile creare e gestire i gruppi.