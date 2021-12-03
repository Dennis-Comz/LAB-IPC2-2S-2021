import os

class Reporte:
    def __init__(self):
        pass

    def genReporte(self, lista):
        html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.0/dist/css/bootstrap.min.css" integrity="sha384-B0vP5xmATw1+K9KRQjQERJvTumQW0nPEzvF6L/Z6nronJ3oUOFUFpCjEUQouq2+l" crossorigin="anonymous">
    <link rel="stylesheet" href="style.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,900;1,900&display=swap" rel="stylesheet">
    <title>Reporte Tokens</title>
</head>
<body>
    <nav>
        <h1>Elaboracion Optima</h1>
    </nav>
    <div>\n'''
        temp = lista.first
        while temp:
            if temp != None:
                html += '\t<h2>' + temp.nombre + '</h2>\n'
                html += '''
        <table class="table table-bordered">
            <thead class="thead-dark">
                <tr>
                    <th scope="col">Segundo</th>\n'''
                tt = temp.listaPasos.getTiempoTotal()
                for i in range(1,temp.listaPasos.getMayor()+1):
                    html += '\t\t    <th scope=\"col\">Linea' + str(temp.listaPasos.getMayor()) + '</th>\n'
                html += '\t</tr>\n</thead>\n<tbody>\n'
                
                i = 1
                pasos = temp.listaPasos.first
                while i <= tt:
                    if pasos == None:
                        break
                    html += '\t\t\t<tr>\n'
                    html += '\t\t\t\t<th scope=\"row\">' + str(i) + '</th>\n'
                    while pasos:
                        if pasos != None:
                            if pasos.segundo == i:
                                if pasos.mover == True and pasos.ensamblar == False:
                                    html += '\t\t\t<td>Mover brazo - componente ' + str(pasos.componente) + '</td>\n'
                                elif pasos.mover == False and pasos.ensamblar == True:
                                    html += '\t\t\t<td>Ensamblar - componente ' + str(pasos.componente) + '</td>\n'
                                elif pasos.mover == False and pasos.ensamblar == False:
                                    html += '\t\t\t<td>No hacer nada</td>\n' 
                            elif pasos.next == None:
                                html += '\t\t\t</tr>\n'
                                i += 1
                                break
                            else:
                                html += '\t\t\t</tr>\n'
                                i += 1
                                break
                        pasos = pasos.next
                html += '\t\t</tbody>\n\t</table>\n</div>\n</body>\n</html>'

            temp = temp.next

            file = open("Reporte.html", "w")
            file.write(html)
            file.close
            os.startfile("Reporte.html")

        print(html)