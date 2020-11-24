# Modificate l’oggetto CSVFile della lezione precedente in modo che 
# dia un messaggio d’errore se si cerca di aprire un file non esistente.

# Poi, aggiungete questi due campi al file “shampoo_sales.csv”:

# 01-01-2015,
# 01-02-2015,ciao
# e gestite gli errori che verranno generati in modo che le linee 
# vengano saltate ma che venga stampato a schermo l’errore.

#======================
# Classe per file CSV
#======================

class CSVFile:

    def __init__(self, name):
        
        # Setto il nome del file
        self.name = name


    def get_data(self):

        # Inizializzo una lista vuota per salvare i valori
        values = []

        # Provo ad aprire il file per estrarci i dati. Se non ci riesco, prima avverto dell'errore, poi devo abortire. Questo è un errore "un-recoverable", ovvero non posso proseguire con la lettura dei dati se non riesco ad aprire il file!

        try:
            my_file = open(self.name, 'r')
        except Exception as e:
            
            # Stampo l'errore
            print('Errore nella lettura del file: "{}"'.format(e))
            
            # Esco dalla funzione tornando "niente".
            return None
        
        # Ora inizio a leggere il file linea per linea
        for line in my_file:
            
            # Faccio lo split di ogni linea sulla virgola
            elements = line.split(',')

            # Se NON sto processando l'intestazione...
            if elements[0] != 'Date':
                    
                # Setto la data ed il valore
                date  = elements[0]
                value = elements[1]
                
                # La variabile "value" al momento e' ancora una stringa, poiche' ho letto da file di testo, quindi converto a valore floating point, e se nel farlo ho un errore avverto. Questo è un errore "recoverable", posso proseguire (semplicemente salto la linea).
                
                try:
                    value = float(value)
                except Exception as e:
                    
                    # Stampo l'errore
                    print('Errore nela conversione a float: "{}"'.format(e))
                    
                    # Vado al prossimo "giro" del ciclo, quindi NON eseguo quanto viene dopo (ovvero l'append)
                    continue
                
                # Infine aggiungo alla lista dei valori questo valore
                values.append(value)
        
        # Chiudo il file
        my_file.close()
        
        # Quando ho processato tutte le righe, ritorno i valori
        return values
    
        
#======================
# Corpo del programma
#======================

mio_file = CSVFile(name='shampoo_sales.csv')

print('Nome del file: "{}"'.format(mio_file.name))
print('Dati contenuti nel file: "{}"'.format(mio_file.get_data()))