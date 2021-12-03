from xml.etree.ElementTree import indent
import xml.etree.cElementTree as ET

class Escribir:
    def __init__(self) -> None:
        pass

    def escribir_salida(self, lista):
        root = ET.Element('LISTAAUTORIZACIONES')
        for autorizacion in lista:
            auto = ET.SubElement(root, 'AUTORIZACION')
            ET.SubElement(auto, 'FECHA').text = autorizacion.fecha
            ET.SubElement(auto, 'FACTURAS_RECIBIDAS').text = str(autorizacion.total_facturas)

            errores = ET.SubElement(auto, 'ERRORES')
            ET.SubElement(errores, 'NIT_EMISOR').text = str(autorizacion.errores.emisor)
            ET.SubElement(errores, 'NIT_RECEPTOR').text = str(autorizacion.errores.receptor)
            ET.SubElement(errores, 'IVA').text = str(autorizacion.errores.iva)
            ET.SubElement(errores, 'TOTAL').text = str(autorizacion.errores.total)
            ET.SubElement(errores, 'REFERENCIA_DUPLICADA').text = str(autorizacion.errores.duplicada)

            ET.SubElement(auto, 'FACTURAS_CORRECTAS').text = str(autorizacion.correctas)
            ET.SubElement(auto, 'CANTIDAD_EMISORES').text = str(autorizacion.emisores)
            ET.SubElement(auto, 'CANTIDAD_RECEPTORES').text = str(autorizacion.receptores)

            autorizaciones = ET.SubElement(auto, 'LISTADO_AUTORIZACIONES')
            for aprobacion in autorizacion.aprobaciones:
                apro = ET.SubElement(autorizaciones, 'APROBACION')
                ET.SubElement(apro, 'NIT_EMISOR', ref=aprobacion.referencia).text = str(aprobacion.emisor)
                ET.SubElement(apro, 'CODIGO').text = str(aprobacion.codigo)
            
            ET.SubElement(autorizaciones, 'TOTAL_APROBACIONES').text = str(len(autorizacion.aprobaciones))

        tree = ET.ElementTree(root)
        self.indent(root)
        tree.write('autorizaciones.xml')

    def indent(self, elem, level=0):
        i = "\n" + level*"  "
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = i + "  "
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
            for elem in elem:
                self.indent(elem, level+1)
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = i