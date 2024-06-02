# Sottoreti di rete VPC

Una **sottorete** è una *sottorete* di una rete VPC.

- Ogni rete VPC è composta da una o più **sottoreti** (partizioni utili di intervalli IP), conosciute anche in Google Cloud come **sottoreti**.
- Ogni sottorete è associata a una regione e tutte le istanze nella sottorete si trovano nella stessa regione.
- Il nome o la regione di una sottorete **non possono essere modificati** dopo la creazione.
  - È necessario eliminare la sottorete e crearne una nuova con il nome o la regione desiderati.
- Le gamme primarie e secondarie delle **sottoreti non possono sovrapporsi** con alcuna gamma allocata.
  - Qualsiasi gamma primaria o secondaria di un'altra sottorete nella stessa rete o qualsiasi gamma IP di sottoreti in reti collegate.
  - ***Devono essere blocchi cidr validi e unici.***

## Aumentare lo spazio IP della sottorete

Google Cloud VPC ha una funzionalità per aumentare lo spazio IP di una sottorete senza interruzioni o tempi di inattività, ma ci sono alcune limitazioni:

- Le nuove sottoreti **non devono sovrapporsi** con le altre sottoreti nella stessa rete VPC in nessuna regione.
- Le nuove sottoreti **devono rimanere all'interno** dello spazio degli indirizzi RFC 1918.
- La nuova gamma di rete deve essere **più grande dell'originale**, ovvero la lunghezza del prefisso deve essere più piccola.
- Una volta che una sottorete è stata espansa, **non è possibile annullarla**.

Le reti VPC in modalità automatica iniziano con una sottorete `/20` e è possibile espanderla a `/16`.

## Indirizzi IP riservati

Ci sono alcuni indirizzi IP riservati per i servizi di Google Cloud e non possono essere utilizzati nella rete VPC:

- Il primo indirizzo IP in ogni sottorete è riservato per l'**indirizzo di rete**.
- Il secondo indirizzo IP in ogni sottorete è riservato per il **gateway predefinito**, che consente l'accesso a Internet.
- Il penultimo indirizzo IP nell'intervallo IP primario per la sottorete è riservato per **l'uso futuro di Google Cloud**.
- L'ultimo indirizzo nell'intervallo IP per la sottorete è riservato per l'**indirizzo di broadcast**.

**NOTA:** Gli indirizzi IP non sono riservati nelle gamme IP secondarie, ma solo nella gamma IP primaria.