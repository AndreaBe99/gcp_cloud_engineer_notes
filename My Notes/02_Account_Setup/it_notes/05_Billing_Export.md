# Esportazione della fatturazione

L'esportazione della fatturazione consente di esportare automaticamente dati dettagliati sulla fatturazione (come l'utilizzo, i dettagli dei costi e i dati sui prezzi) in BigQuery per analisi e reportistica dettagliata.

L'esportazione della fatturazione non è retroattiva.

Ci sono due tipi di dati di fatturazione che possono essere esportati (possono essere selezionati nella console a seconda del caso d'uso):

- Dati dettagliati sui costi giornalieri
- Dati sui prezzi

![Esportazione della fatturazione](../images/05_Billing_Export_01.png)

## Demo: Esportazione della fatturazione

Demo al seguente link: [Segui l'esportazione della fatturazione](https://youtu.be/jpno8FSqpc8?si=Ze40OpOie3td3_AD&t=10489).

1. Vai alla pagina `Fatturazione`, utilizzando il **menu di navigazione** a sinistra.

2. Vai alla sezione `Esportazione della fatturazione` e scegli tra `Dati dettagliati sui costi giornalieri` e `Dati sui prezzi`.

    ![Esportazione della fatturazione GCP](../images/05_Billing_Export_02.png)

    1. Prima di tutto, è necessario creare un **dataset** in BigQuery, se non ne hai già uno. Se è la prima volta, ti verrà chiesto di creare un dataset, fai clic su `Vai a BigQuery`.

    2. Nella console di BigQuery, fai clic su `Crea dataset` e compila i dettagli.

3. Fai clic su `Modifica impostazioni` per configurare le impostazioni di esportazione.

4. Ora è necessario abilitare l'API di trasferimento dati di BigQuery. Per farlo, vai alla pagina `API e servizi`, utilizzando il **menu di navigazione** a sinistra.

     1. Fai clic su `Dashboard` e cerca nella barra di ricerca `BigQuery Data Transfer API`, quindi fai clic su di essa e successivamente su `Abilita`.