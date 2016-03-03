import configparser
class Currency:
    '''A class to calculate currencies'''
    #constructor
    def __init__(self):#sets initial values in the class
        self._config = configparser.ConfigParser()
        self._config.read('currencyconverter.config')#reads config file
        if self._config.sections() == []:#checks if the file is empty or doesn't exists
            #creates values in class using default values
            self._euro = 1.21
            self._usd = 1.67
            self._yen = 170.71
        else:
            #loads values from the file
            self._euro = self._config['Currencies']['Euro']
            self._usd = self._config['Currencies']['USD']
            self._yen = self._config['Currencies']['YEN']
    def convertToPounds(self,amount,currency):#converts any currency to GBP
        if currency == 'Euro':
            return (float(amount)/float(self._euro))#converts Euro to GBP
        elif currency == 'USD':
            return (float(amount)/float(self._usd))#converts USD to GBP
        elif currency == 'YEN':
            return (float(amount)/float(self._yen))#converts YEN to GBP
        else:
            return amount#converts GBP to GBP
    def convertFromPounds(self,amount,currency):#converts GBP to any currency
        if currency == 'Euro':
            return (float(amount)*float(self._euro))#converts GBP to Euro
        elif currency == 'USD':
            return (float(amount)*float(self._usd))#converts GBP to USD
        elif currency == 'YEN':
            return (float(amount)*float(self._yen))#converts GBP to YEN
        else:
            return amount#converts GBP toGBP
    def get(self):#returns the current values
        return {'Euro':self._euro,'USD':self._usd,'YEN':self._yen}#dictionary for the all the values
    def edit(self,euro,usd,yen):#edit the stored values with the ones that the user has input 
        self._euro = euro
        self._usd = usd
        self._yen = yen
    #run when class is about to be destroyed
    def __del__(self):#run when the class is deleted
        print('Saving Currencies')
        self._config = configparser.ConfigParser()
        self._config['Currencies'] = {'Euro': self._euro,
                               'USD': self._usd,
                               'Yen': self._yen}#create dictionary with all the values to be written to the file
        with open('currencyconverter.config','w') as f:#opens the file
            self._config.write(f)#saves values to the config file
