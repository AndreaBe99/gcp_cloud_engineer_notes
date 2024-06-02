# Cloud Shell e Editor

## Cloud Shell

**Cloud Shell** è una macchina virtuale che è caricata con strumenti di sviluppo. Offre una directory home persistente da 5GB e funziona su Google Cloud.

È accessibile dalla Console di Google Cloud, ed è disponibile gratuitamente.

Fornisce un'interfaccia a riga di comando per gestire le risorse e sviluppare nel cloud.

Include anche un editor di codice integrato, che è un **editor basato su web** che ti permette di modificare i file direttamente nel Cloud Shell.

### Demo

Una demo video del Cloud Shell può essere trovata [qui](https://youtu.be/jpno8FSqpc8?si=F7wWa9aTn5l9UKRJ&t=14015).

Per attivare il Cloud Shell, clicca sull'icona `Attiva Cloud Shell` nell'angolo in alto a destra della Console di Google Cloud.

![Attiva Cloud Shell](../images/09_Cloud_Shell_and_Editor_01.png)

Provvista una istanza E2 small di Google Compute Engine, che esegue un sistema operativo Linux basato su debian.

È una VM effimera e preconfigurata, e l'ambiente con cui lavori è un contenitore Docker in esecuzione sulla VM.

Le istanze di Cloud Shell sono provviste su base per utente, per sessione.

L'istanza persiste mentre la sessione è attiva, e dopo un'ora di inattività, la sessione viene terminata e l'istanza viene eliminata.

**INFO:** Per controllare lo spazio su disco disponibile, puoi eseguire il comando:

```bash
df -h

## Example of Output
Filesystem                                  Size  Used Avail Use% Mounted on
overlay                                      49G  2.3G   44G   5% /
tmpfs                                        64M     0   64M   0% /dev
tmpfs                                       3.2G     0  3.2G   0% /sys/fs/cgroup
shm                                          64M     0   64M   0% /dev/shm
tmpfs                                       3.2G   12K  3.2G   1% /run
tmpfs                                       3.2G     0  3.2G   0% /media
/dev/disk/by-id/google-persistent-disk-0    4.8G   11M  4.6G   1% /home
```

Per cambiare le proprietà utilizzando lo strumento a riga di comando `gcloud`, puoi eseguire il seguente comando:

```bash
gcloud config set project [PROJECT_ID]
```

**INFO:** Per controllare dove l'attuale istanza di Cloud Shell è in esecuzione, puoi eseguire il comando:

```bash
curl "metadata/computeMetadata/v1/instance/zone"
```

## Cloud Code Editor

Per utilizzare Code Editor abbiamo bisogno di abilitare i cookie di terze parti nel browser.
