from escribir import Escribir
class Autorizacion:
    def __init__(self, fecha, total_facturas, errores, correctas, emisores, receptores, aprobaciones):
        self.fecha = fecha
        self.total_facturas = total_facturas
        self.errores = errores
        self.correctas = correctas
        self.emisores = emisores
        self.receptores = receptores
        self.aprobaciones = aprobaciones

    def to_dict(self):
        return {"autorizacion": {"fecha": self.fecha, "total_facturas": self.total_facturas, 
        "errores": {"emisores": self.errores.emisor, "receptores": self.errores.receptor, "iva": self.errores.iva, "total": self.errores.total, "duplicado": self.errores.duplicada},
        "facturas_correctas": self.correctas, "cant_emisores": self.emisores, "cant_receptores": self.receptores, 
        "aprobaciones": self.get_apr()}}

    def get_apr(self):
        apr = [obj.to_dict() for obj in self.aprobaciones]
        return apr
class Error:
    def __init__(self, emisor, receptor, iva, total, duplicada):
        self.emisor = emisor
        self.receptor = receptor
        self.iva = iva
        self.total = total
        self.duplicada = duplicada

class Aprobacion:
    def __init__(self, referencia, emisor, codigo):
        self.referencia = referencia
        self.emisor = emisor
        self.codigo = codigo

    def to_dict(self):
        return {"aprobacion": {"referencia": self.referencia, "emisor": self.emisor, "codigo": self.codigo}}
class Analizador:
    def __init__(self):
        self.crear_archivo = Escribir()

    def analizar(self, lista):
        fechas = []
        self.lista_autorizaciones = list()
        for factura in lista:
            if len(fechas) == 0:
                fechas.append(factura.tiempo)
            else:
                if factura.tiempo not in fechas:
                    fechas.append(factura.tiempo)

        i = 0
        while i < len(fechas):
            error_emisor = 0
            error_receptor = 0
            error_iva = 0
            error_total = 0
            aprobaciones = 0
            emisores = []
            receptores = []
            facturas = 0
            self.error_duplicada = 0
            lista_aprobaciones = []
            
            for factura in lista:
                if factura.tiempo == fechas[i]:
                    facturas += 1
                    error_finded = False
                    if self.analisis_nit(factura.nit_emisor) == False:
                        error_emisor += 1
                        error_finded = True
                    if self.analisis_nit(factura.nit_receptor) == False:
                        error_receptor += 1
                        error_finded = True
                    if self.verificar_iva(factura.iva, factura.valor) == False:
                        error_iva += 1
                        error_finded = True
                    if self.verificar_total(factura.total, factura.iva, factura.valor) == False:
                        error_total += 1
                        error_finded = True
                    if self.verificar_referencia(factura.tiempo, factura.referencia, lista) == True:
                        error_finded = True
                    if error_finded == False:
                        aprobaciones += 1
                        
                        for fct in lista:
                            if fct.tiempo == fechas[i]:
                                if len(emisores) == 0:
                                    emisores.append(fct.nit_emisor)
                                else:
                                    if fct.nit_emisor not in emisores:
                                        emisores.append(fct.nit_emisor)
                                if len(receptores) == 0:
                                    receptores.append(fct.nit_receptor)
                                else:
                                    if fct.nit_receptor not in receptores:
                                        receptores.append(fct.nit_receptor)
                        codigo = self.get_codigo(fechas[i], aprobaciones)
                        lista_aprobaciones.append(Aprobacion(factura.referencia, factura.nit_emisor, codigo))

            fecha = fechas[i]
            error = Error(error_emisor, error_receptor, error_iva, error_total, self.error_duplicada)
            self.lista_autorizaciones.append(Autorizacion(fecha, facturas, error, aprobaciones, len(emisores), len(receptores), lista_aprobaciones))
            i += 1
            error_emisor = 0
            error_receptor = 0
            error_iva = 0
            error_total = 0
            aprobaciones = 0
            emisores = []
            receptores = []
            facturas = 0
            self.error_duplicada = 0
            lista_aprobaciones = []
        self.crear_archivo.escribir_salida(self.lista_autorizaciones)
        

    def analisis_nit(self, nit):
        tamano = len(nit) - 1
        validador = nit[tamano]
        suma = 0
        contador = 0
        for i in range(tamano, 0, -1):
            suma += i * int(nit[contador])
            contador += 1

        preliminar = suma % 11
        preliminar = 11 - preliminar
        final = preliminar % 11
        if final == 10:
            final = 'K'

        if str(final) == validador:
            return True
        else:
            return False

    def verificar_total(self, total, iva, valor):
        preliminar = iva + valor
        if total == preliminar:
            return True
        else:
            return False

    def verificar_iva(self, iva, valor):
        preliminar = round(0.12*valor, 2)
        if preliminar == iva:
            return True
        else:
            return False

    def verificar_referencia(self, fecha, referencia, lista):
        contador = 0
        for factura in lista:
            if factura.tiempo == fecha and factura.referencia == referencia:
                contador += 1
        
        if contador > 1:
            self.error_duplicada = contador
            return True
        else:
            return False

    def get_codigo(self, fecha, no_aprobacion):
        anio = ''
        dia = ''
        mes = ''
        contador = 0
        for num in fecha:
            if num != '/' and contador >= 0 and contador <= 1:
                dia += num
                contador += 1
            elif num != '/' and contador >= 2 and contador <= 3:
                mes += num
                contador += 1
            elif num != '/' and contador > 3:
                anio += num
                contador += 1

        ceros = '000000' + str(no_aprobacion)
        final = anio + mes + dia + ceros
        return final

    def get_lista(self):
        return self.lista_autorizaciones