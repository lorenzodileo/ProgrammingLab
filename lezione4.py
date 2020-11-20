# Creare un oggetto CSVFile che rappresenti un file CSV, e che:
# venga inizializzato sul nome del file CSV, e
# abbia un attributo "name" che ne contenga il nome
# abbia un metodo "get_data" che torni i dati dal file CSV come numeri
# di una lista (come abbiamo già visto)


# oggetto CSVFile
#   - init (filename)
#   - name
#   - get_data()
#   - return dati


class CSVFile:
    pass
    def __init__(self, name):
        self.name = name

    def get_data(self):
        
        values = []

        my_file = open(self.name, 'r')

        for line in my_file:
        
            elements = line.split(',')

            if elements[0] != 'Date':

                date = elements[0]
                value = elements[1]

                values.append(float(value))

        return(values)


mio_file = CSVFile(name='shampoo_sales.csv')

print(mio_file.name)
print(mio_file.get_data())
