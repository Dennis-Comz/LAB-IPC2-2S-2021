import xml.etree.ElementTree as ET
import re

class Factura:
    def __init__(self, tiempo, referencia, nit_emisor, nit_receptor, valor, iva, total):
        self.tiempo = tiempo
        self.referencia = referencia
        self.nit_emisor = nit_emisor
        self.nit_receptor = nit_receptor
        self.valor = valor
        self.iva = iva
        self.total = total

    def to_dict(self):
        return {"tiempo": self.tiempo, "referencia": self.referencia, "nit_emisor": self.nit_emisor,
        "nit_receptor": self.nit_receptor, "valor": self.valor, "iva": self.iva, "total": self.total}
        
class Reader:
    def __init__(self):
        self.lista_facturas = list()

    def read_file(self, file):
        root = ET.fromstring(file)
        for tag in root.findall('DTE'):
            tiempo = self.get_tiempo(tag[0].text)
            referencia = self.get_numeros(tag[1].text)
            nit_emisor = self.get_numeros(tag[2].text)
            nit_receptor = self.get_numeros(tag[3].text)
            valor = float(self.get_numeros(tag[4].text))
            iva = float(self.get_numeros(tag[5].text))
            total = float(self.get_numeros(tag[6].text))

            self.lista_facturas.append(Factura(tiempo, referencia, nit_emisor, nit_receptor, valor, iva, total))

    def get_numeros(self, numeros):
        nums = ''
        for num in numeros:
            if num != ' ':
                nums += num
        return nums

    def get_tiempo(self, tiempo):
        final = "#"
        tiempo += final
        estado = 0
        tfinal = ''
        i = 0
        while i < len(tiempo):
            actual = tiempo[i]
            if estado == 0:
                if actual == ' ':
                    i += 1
                elif actual == '\n':
                    i += 1
                elif actual == '\t':
                    i += 1
                elif re.search('\d', actual):
                    estado = 1
                    tfinal += actual
                    i += 1
                else:
                    i += 1
            elif estado == 1:
                if re.search('\d', actual):
                    tfinal += actual
                    i += 1
                elif re.search('/', actual):
                    tfinal += actual
                    i += 1
                elif actual == ' ':
                    break
        return tfinal

    def get_lista(self):
        return self.lista_facturas