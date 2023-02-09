# Light Curve Fermi-LAT Analisys
Analisi di 5 sorgenti di tipo variabile estrapolate dal seguente link: https://fermi.gsfc.nasa.gov/ssc/data/access/lat/LightCurveRepository/.<br/>
In particolare si analizzano per ogni sorgente tre campionamenti disponibili, differenziati per intrevalli di campionamento: giornaliero (3gg), settimanale e mensile.<br/>
Le sorgenti selezionate sono disponbili nella cartella `Dati` ed all'interno di ogni sorgente sono presenti tre file di tipo `.csv` (campionamenti).<br/>
Tramite lo script `FermiLATLightCurveAnalysis.py` e' possibile leggere dati ed analizzarli.

# Istruzioni all'uso

Un volta fatto il `clone` della repository e' sufficienti lanciare da terminale lo script `FermiLATLightCurveAnalysis.py` seguito dalla directory della sorgente/file da voler analizzare (per eseguire molteplici sorgenti/file basta aggiungere uno spazio tra le directory). Inoltre e' possibile, inserendo `--file` preceduto da uno spazio dopo la directory che si vuole eseguire, salvare su sorgente file e png relativi al folder/file analizzato invece che visualizzarli a schermo.</br>
(Per la parte opzionale, in quanto le alte attività sono caratterischi della singola sorgente e non dei vari campionamenti, basta lanciare il programma con il folder relativo alla sorgente da analizzare per ottenere lo studio delle alta attività)

### Esempio:<br/>
<ul>
    <li>py FermiLATLightCurveAnalysis.py Dati/4FGL J1224.9+2122 LCR (Analisi della sorgente, visualizzazione a schermo)</li>
    <li>py FermiLATLightCurveAnalysis.py Dati/4FGL J1224.9+2122 LCR/4FGL_J1224.9+2122_daily.csv --file (Analsi del file, scrittura su sorgente dei file)</li>
</ul>

# Moduli

<table>
    <thead>
        <tr>
            <th>Modulo</th>
            <th><center>Funzioni</center><th>
            <th></th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>read.py</td>
            <td><ul>
                <li>read</li>
            </ul></td>
            </ul></td>
            <td>Legge ed elabora il csv per scrivere i dati in funzione del tempo</td>
        </tr>
        <tr>
            <td>plot.py</td>
            <td><ul>
                <li>plot</li>
            </ul></td>
            <td>Crea un grafico del flusso di fotoni in funzione del tempo</td>
        </tr>
        <tr>
            <td>fourier.py</td>
            <td><ul>
                <li>fourier</li>
            </ul></td>
            <td>Crea molteplici grafici relativi allo spettro di potenza dei file analizzati (in funzione delle frequenze e del periodo)</td>
        </tr>
        <tr>
            <td>noise.py</td>
            <td><ul>
                <li>noise</li>
            </ul></td>
            <td>Studia il tipo di rumore del file da analizzare tramite un fit. Restituisce un grafico con il fit che meglio apporossima il rumore della variabile</td>
        </tr>
        <tr>
            <td>filtro.py</td>
            <td><ul>
                <li>filter</li>
            </ul></td>
            <td>Applica vari filtri in frequenza per visualizzare solo il comportamento di lungo periodo e ne grafica il comportamento</td>
        </tr>
        <tr>
            <td>highactivity.py</td>
            <td><ul>
                <li>soglia</li>
                <li>alta_attivita</li>
                <li>line_high_activity</li>
                <li>highact</li>
            </ul></td>
            <td><ul>
                <li>Restituisce la soglia minima di fotoni in base alla sorgente analizzata</li>
                <li>Resituisce il numero di stati si alata attivita e la loro durata in base alla sorgnet eanalizzata</li>
                <li>Resituisce gli indici da cui tracciare i limiti dei vari stati di alta attivita</li>
                <li>Richiama tutte le funzioni precedenti e grafica la sorgente analizzata applicando la soglia per distiguere stati di quiescenza da stati di alta attivita</li>
            </ul></td>
        </tr>
    </tbody>
</table>

