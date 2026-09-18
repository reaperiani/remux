# Remux

[![Latest release](https://img.shields.io/github/v/release/reaperiani/remux?include_prereleases&label=release)](https://github.com/reaperiani/remux/releases/latest)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

Una piccola interfaccia grafica per sostituire la traccia audio di un video con
un file WAV o AIFF, senza ricodificare il video.

Remux usa FFmpeg per copiare i flussi originali in un nuovo contenitore MKV.
Può essere utile quando vuoi consegnare a YouTube, Vimeo o ad altre piattaforme
una traccia audio non compressa, evitando un passaggio intermedio con un codec
lossy.

> [!WARNING]
> Il progetto e le release disponibili sono sperimentali. Conserva sempre una
> copia dei file originali e controlla il risultato prima di pubblicarlo.

## Cosa fa

- rimuove la traccia audio dal video selezionato;
- inserisce la traccia del file WAV/AIFF selezionato;
- copia i flussi senza ricodificarli;
- salva il risultato accanto al video originale come `nome_output.mkv`;
- non modifica il file video originale.

Il remux non migliora la qualità di materiale già compresso: serve a evitare
un'ulteriore compressione quando l'audio di partenza è disponibile in formato
lossless.

## Download

Gli eseguibili sperimentali sono disponibili nella pagina
[Releases](https://github.com/reaperiani/remux/releases/latest).

La release più recente contiene gli archivi `remuxMAC.zip` e `remuxPyQt.zip`.
La compatibilità con le versioni attuali di Windows e macOS non è ancora stata
verificata: se li provi, puoi raccontare com'è andata aprendo una
[issue](https://github.com/reaperiani/remux/issues).

## Utilizzo

1. Avvia Remux.
2. Premi **Scegli** e seleziona il video.
3. Seleziona il file audio WAV o AIFF.
4. Premi **Metti il WAV nel video**.
5. Controlla il file `nome_output.mkv` creato nella cartella del video.

Durante l'operazione viene creato anche un file temporaneo
`nome_noaudio.mkv`, che normalmente viene eliminato al termine.

Video supportati dal selettore: AVI, MP4, MKV, MOV, WMV, FLV, WebM, MPEG e MPG.
La compatibilità effettiva dei flussi dipende da FFmpeg e dal contenitore MKV.

## Avvio dal sorgente

### Requisiti

- Python 3;
- [PyQt5](https://pypi.org/project/PyQt5/);
- [FFmpeg](https://ffmpeg.org/download.html).

Installa PyQt5 con:

```bash
python -m pip install PyQt5
```

Gli script cercano l'eseguibile di FFmpeg nella directory da cui vengono
avviati: `ffmpeg` per gli script macOS e `ffmpeg.exe` per lo script PyQt
destinato a Windows.

Avvia uno degli script con:

```bash
python remuxMAC_v2.py
```

oppure:

```bash
python remuxPyQt.py
```

### Script disponibili

| File | Descrizione |
| --- | --- |
| `remuxMAC_v2.py` | Versione più recente che richiama l'eseguibile `ffmpeg`. |
| `remuxPyQt.py` | Interfaccia con nomi accessibili per gli screen reader e `ffmpeg.exe`. |
| `remuxMAC.py` | Prima versione, mantenuta come riferimento. |

Il supporto agli screen reader non è ancora stato verificato in modo completo.

## Limitazioni note

- video e audio devono essere già sincronizzati; la loro durata va verificata;
- il programma non offre opzioni per offset, taglio o regolazione del volume;
- la gestione degli errori di FFmpeg è ancora essenziale;
- un file di output già esistente può impedire il completamento del processo;
- le release sono alpha e potrebbero non funzionare sulle versioni recenti dei
  sistemi operativi.

## FFmpeg e licenze

Il codice di Remux è distribuito con licenza [MIT](LICENSE).

FFmpeg è un progetto indipendente e viene distribuito secondo le proprie
licenze. Gli eventuali binari di FFmpeg inclusi nelle release non sono coperti
dalla licenza MIT di Remux. Consulta la pagina ufficiale
[FFmpeg Legal](https://ffmpeg.org/legal.html) per i dettagli.

## Segnalazioni

Hai trovato un problema o vuoi proporre un miglioramento? Apri una
[issue](https://github.com/reaperiani/remux/issues) indicando sistema operativo,
versione utilizzata e messaggio di errore.
