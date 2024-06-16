# Policy e Condizioni

Ricorda:

![Architettura delle politiche](../images/01_Cloud_IAM_03.png)

- Le **Policy** sono una raccolta di dichiarazioni che definiscono chi ha quale tipo di accesso alle tue risorse.
  - Una politica è collegata a una risorsa e viene utilizzata per far rispettare il controllo degli accessi ogni volta che quella risorsa viene acceduta.
- I **Bindings** legano uno o più membri con un singolo ruolo e qualsiasi condizione specifica del contesto.

Quindi un binding è una tupla di (membri, ruolo, condizione), e aggiungendo metadati e configurazione di audit otteniamo una politica.

## Dichiarazioni di Policy

Un esempio di una **Dichiarazione di Policy**:

```json
{
    "bindings": [
        {
            "role": "roles/storage.admin",
            "members": [
                "user:tonybowtieace@gmail.com"
            ]
        },
        {
            "role": "roles/storage.objectViewer",
            "members": [
                "user:larkfederkenge@gmail.com"
            ],
            "condition": {
                "title": "Scade_il_1_Gennaio_2021",
                "description": "Non concedere l'accesso dopo il 1 gennaio 2021",
                "expression": "request.time < timestamp('2021-01-01T00:00:00Z')"
            }
        }
    ],
    "etag": "BwW9z3Q8f3Y=",
    "version": 3
}
```

Possiamo scrivere la stessa politica in formato YAML:

```yaml
bindings:
- members:
  - user: tonybowtieace@gmail.com
    role: roles/storage.admin
- members:
    - user: larkfederkenge@gmail.com
    role: roles/storage.objectViewer
    condition:
        title: Scade_il_1_Gennaio_2021
        description: Non concedere l'accesso dopo il 1 gennaio 2021
        expression: request.time < timestamp('2021-01-01T00:00:00Z')
etag: BwW9z3Q8f3Y=
version: 3
```

Per interrogare la politica, possiamo utilizzare il seguente comando:

```bash
# Ottieni la politica IAM per un progetto
gcloud projects get-iam-policy [PROJECT_ID]

# Ottieni la politica IAM per una cartella
gcloud resource-manager folders get-iam-policy [FOLDER_ID]

# Ottieni la politica IAM per un'organizzazione
gcloud organizations get-iam-policy [ORG_ID]
```

### Versioni delle Politiche

Ci sono tre versioni dello schema di politica IAM:

- `1`: della sintassi IAM per la politica supporta il binding di un ruolo a uno o più membri.
  - **Non supporta i binding di ruoli condizionali**. Quindi, con la versione 1 non vedrai il campo `condition`.
- `2`: è utilizzato per **l'uso interno di Google** e quindi le query non restituiranno politiche di versione 2.
- `3`: introduce il campo `condition` per supportare i binding di ruoli condizionali.

### Limitazioni delle Politiche

Le seguenti sono alcune limitazioni delle politiche IAM:

- Ogni risorsa può avere solo una politica e questo include organizzazione, cartella e progetto.
- Ogni politica IAM ha un massimo di 1500 membri o 250 gruppi Google.
- Le modifiche alle politiche impiegheranno fino a 7 minuti per propagarsi completamente attraverso GCP.
- C'è un limite di 100 binding di ruoli condizionali per politica.

## Condizioni

Le **Condizioni** sono attributi che si basano su risorse o su dettagli sulla richiesta (timestamp, indirizzo IP di origine/destinazione, ecc).

Il *Binding di Ruolo Condizionale* è un altro nome per una politica che include una condizione, possono essere aggiunte a una politica nuova o esistente.

### Esempi

Esempio basato sul tempo:

```yaml
bindings:
- members:
  - user: tonybowtieace@gmail.com
    role: roles/storage.admin
- members:
    - user: larkfederlagen@gmail.com
    role: roles/storage.objectViewer
    condition:
        title: Accesso_durante_orario_lavorativo
        description: accesso durante l'orario lavorativo da lunedì a venerdì
        expression: request.time.getHours("America/Toronto") >= 9 &&
                    request.time.getHours("America/Toronto") <= 17 &&
                    // Il giorno della settimana varia da 0 a 6, dove 0 è domenica e 6 è sabato
                    request.time.getDayOfWeek("America/Toronto") >= 1 &&
                    request.time.getDayOfWeek("America/Toronto") <= 5
etag: BwW9z3Q8f3Y=
version: 3
```

Esempio basato su risorse:

```yaml
bindings:
- members:
  - user: larkfederlagen@gmail.com
    role: roles/owner
- members:
    - group: developer@bowtieinc.com
    role: roles/compute.instanceAdmin
    condition:
        title: Accesso_solo_per_sviluppo
        description: Solo accesso a VM di sviluppo
        expression: (resource.type == "compute.googleapis.com/Disk" &&
                    resource.name.startsWith("project-cat-bowties/region/us-central1/disk/development")) ||
                    (resource.type == "compute.googleapis.com/Instance" &&
                    resource.name.startsWith("project-cat-bowties/region/us-central1/instance/development")) ||
                    (resource.type != "compute.googleapis.com/Instance" &&
                    resource.type != "compute.googleapis.com/Disk")
version: 3
```

### Limitazioni delle Condizioni

Alcune limitazioni delle condizioni includono:

- Le condizioni sono limitate a servizi e risorse specifici.
- I ruoli primitivi non sono supportati.
- I membri non possono essere allUsers o allAuthenticatedUsers.
- Limite di 100 binding di ruoli condizionali per politica.
- 20 binding di ruoli per lo stesso ruolo e membro.

## Log AuditConfig

I log **AuditConfig** sono utilizzati per registrare tutte le modifiche apportate alla politica IAM. Questo è utile per tracciare le modifiche e per scopi di conformità.

Specifica l'auto-configurazione per un servizio, che definisce quali tipi di permessi vengono registrati e quali identità (se presenti) sono esentate dalla registrazione.

Esempio:

```yaml
auditConfigs:
- auditLogConfigs:
  - logType: DATA_READ
  - logType: ADMIN_READ
  - logType: DATA_WRITE
  service: allServices
- auditLogConfigs:
  - exemptedMembers:
    - tonybowtieace@gmail.com
    - logType: ADMIN_READ
  service: storage.googleapis.com
```