# Best Practice per Cloud IAM

## Principio del privilegio minimo

***Applicare solo il livello di accesso minimo richiesto per svolgere il lavoro necessario.***

- Ciò può essere fatto utilizzando **Ruoli predefiniti** anziché **Ruoli primitivi**.
- Concedere i ruoli al **livello di ambito più piccolo possibile**.
- Le risorse figlie non possono limitare l'accesso concesso sulle risorse genitore.
- **Limitare** chi può creare e gestire gli account di servizio.
- **Fare attenzione** al ruolo di `Owner`, poiché ha il controllo completo sul progetto.

## Gerarchia delle risorse

- **Riflettere** la struttura gerarchica delle risorse di Google Cloud nella struttura dell'organizzazione.
- Utilizzare i progetti per raggruppare le risorse che condividono **le stesse frontiere di fiducia**.
- Impostare le politiche a livello di **organizzazione e di progetto**, anziché a livello di risorsa.
- Utilizzare i principi di sicurezza del **privilegio minimo** per concedere ruoli IAM.
- Concedere ruoli per utenti o gruppi a livello di **cartella** anziché impostarli a livello di progetto, se **si estendono su più progetti**.

## Account di servizio

- Quando si utilizzano gli Account di servizio, **trattare ogni app come una frontiera di fiducia separata**.
- **Non eliminare gli Account di servizio** utilizzati da servizi in esecuzione.
- **Ruotare regolarmente le chiavi degli Account di servizio gestiti dall'utente**.
- **Denominare le chiavi degli Account di servizio** in base all'uso e alle autorizzazioni.
- **Limitare** l'accesso agli Account di servizio.
- **Non** caricare le chiavi degli Account di servizio nei repository di codice sorgente.

## Audit

- Utilizzare i **Log di audit di Cloud** per **verificare regolarmente le modifiche alle politiche IAM**.
- **Verificare** chi può modificare le politiche IAM sui progetti.
- **Esportare** i log di audit in Cloud Storage per la conservazione a lungo termine.
- Verificare regolarmente l'accesso alle **chiavi degli Account di servizio**.
- **Limitare l'accesso ai log** con ruoli di registrazione.

## Gestione delle politiche

- Per concedere accesso a **tutti i progetti** dell'organizzazione, utilizzare una **politica a livello di organizzazione**.
- Concedere ruoli a un **gruppo di Google** anziché a singoli utenti, quando possibile.
- Quando si concedono **più ruoli per un compito specifico**, creare un **gruppo di Google**.