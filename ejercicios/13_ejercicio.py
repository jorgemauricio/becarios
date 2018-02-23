#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
#######################################
# Author: Jorge Mauricio
# Email: jorge.ernesto.mauricio@gmail.com
# Date: 2018-02-01
# Version: 1.0
#######################################

Objetivo:
Dado un texto, contabilizar el número de veces que cada una de las palabras se
repiten.


texto = "Muy buenas tardes a todas y a todos ustedes.
Quiero saludar, con respeto, al Presidente de la Cámara de Diputados y al
Presidente de la Cámara de Senadores.
A los señores Dirigentes de los partidos políticos en nuestro país. A sus
principales fuerzas.
De igual forma, saludo con respeto a los señores Gobernadores. A
Gobernadores electos. Al Jefe de Gobierno electo del Distrito Federal. Todos
ellos con origen en distintas expresiones políticas.
Saludo a los señores Coordinadores Parlamentarios de distintas fuerzas
políticas que están, hoy, aquí presentes.
Con respeto, también, saludo a la representación, en actores políticos
distinguidos, de las distintas fuerzas políticas de nuestro país.
A todos, les saludo con afecto y reconocimiento por este encuentro, sin duda,
inédito, pero que representa un gran paso para impulsar la trasformación de
nuestro país. Es el punto de encuentro y de coincidencia que, realmente,
aplaudo, celebro, y que sea para el bien de México.
México comienza una nueva etapa de su vida democrática. Ha llegado el
momento del encuentro y del acuerdo. Ha llegado el momento de dar el
siguiente paso en el perfeccionamiento democrático: Transitar del sufragio
efectivo al gobierno eficaz.
En este propósito, los actores políticos deben, o debemos, caminar juntos.
Debemos dialogar para construir consensos. En esta hora decisiva de la vida
de la República se requiere que los políticos hagamos de las coincidencias la
base para alcanzar los acuerdos esenciales.
Se necesita que la pluralidad y la diferencia de visiones, en lugar de ser
obstáculo, permitan el ascenso de México, enriquezcan el proyecto de Nación
que todos queremos para el Siglo XXI.
Como Presidente de la República, estoy plenamente convencido que
gobernar en democracia significa estar atento y escuchar a las diversas
voces que expresan el sentir de los mexicanos.
He señalado, con plena convicción, que seré un Presidente democrático.
Esto significa voluntad absoluta para conciliar posiciones. Voluntad para
anteponer, invariablemente, el interés superior de la Nación."

Resultado:

***** Numero de palabras: 321
Palabra MUY se repite 1
Palabra BUENAS se repite 1
Palabra TARDES se repite 1
Palabra A se repite 10
Palabra TODAS se repite 1
Palabra Y se repite 8
Palabra TODOS se repite 4
Palabra USTEDES se repite 1
Palabra QUIERO se repite 1
Palabra SALUDAR se repite 1
Palabra CON se repite 6
Palabra RESPETO se repite 3
Palabra AL se repite 4
Palabra PRESIDENTE se repite 4
Palabra DE se repite 26
Palabra LA se repite 11
Palabra CÁMARA se repite 2
Palabra DIPUTADOS se repite 1
Palabra SENADORES se repite 1
Palabra LOS se repite 8
Palabra SEÑORES se repite 3
Palabra DIRIGENTES se repite 1
Palabra PARTIDOS se repite 1
Palabra POLÍTICOS se repite 4
Palabra EN se repite 8
Palabra NUESTRO se repite 3
Palabra PAÍS se repite 3
Palabra SUS se repite 1
Palabra PRINCIPALES se repite 1
Palabra FUERZAS se repite 3
Palabra IGUAL se repite 1
Palabra FORMA se repite 1
Palabra SALUDO se repite 4
Palabra GOBERNADORES se repite 2
Palabra ELECTOS se repite 1
Palabra JEFE se repite 1
Palabra GOBIERNO se repite 2
Palabra ELECTO se repite 1
Palabra DEL se repite 4
Palabra DISTRITO se repite 1
Palabra FEDERAL se repite 1
Palabra ELLOS se repite 1
Palabra ORIGEN se repite 1
Palabra DISTINTAS se repite 3
Palabra EXPRESIONES se repite 1
Palabra POLÍTICAS se repite 3
Palabra COORDINADORES se repite 1
Palabra PARLAMENTARIOS se repite 1
Palabra QUE se repite 10
Palabra ESTÁN se repite 1
Palabra HOY se repite 1
Palabra AQUÍ se repite 1
Palabra PRESENTES se repite 1
Palabra TAMBIÉN se repite 1
Palabra REPRESENTACIÓN se repite 1
Palabra ACTORES se repite 2
Palabra DISTINGUIDOS se repite 1
Palabra LAS se repite 3
Palabra LES se repite 1
Palabra AFECTO se repite 1
Palabra RECONOCIMIENTO se repite 1
Palabra POR se repite 1
Palabra ESTE se repite 2
Palabra ENCUENTRO se repite 3
Palabra SIN se repite 1
Palabra DUDA se repite 1
Palabra INÉDITO se repite 1
Palabra PERO se repite 1
Palabra REPRESENTA se repite 1
Palabra UN se repite 2
Palabra GRAN se repite 1
Palabra PASO se repite 2
Palabra PARA se repite 7
Palabra IMPULSAR se repite 1
Palabra TRASFORMACIÓN se repite 1
Palabra ES se repite 1
Palabra EL se repite 11
Palabra PUNTO se repite 1
Palabra COINCIDENCIA se repite 1
Palabra REALMENTE se repite 1
Palabra APLAUDO se repite 1
Palabra CELEBRO se repite 1
Palabra SEA se repite 1
Palabra BIEN se repite 1
Palabra MÉXICO se repite 3
Palabra COMIENZA se repite 1
Palabra UNA se repite 1
Palabra NUEVA se repite 1
Palabra ETAPA se repite 1
Palabra SU se repite 1
Palabra VIDA se repite 2
Palabra DEMOCRÁTICA se repite 1
Palabra HA se repite 2
Palabra LLEGADO se repite 2
Palabra MOMENTO se repite 2
Palabra ACUERDO se repite 1
Palabra DAR se repite 1
Palabra SIGUIENTE se repite 1
Palabra PERFECCIONAMIENTO se repite 1
Palabra DEMOCRÁTICO: se repite 1
Palabra TRANSITAR se repite 1
Palabra SUFRAGIO se repite 1
Palabra EFECTIVO se repite 1
Palabra EFICAZ se repite 1
Palabra PROPÓSITO se repite 1
Palabra DEBEN se repite 1
Palabra O se repite 1
Palabra DEBEMOS se repite 2
Palabra CAMINAR se repite 1
Palabra JUNTOS se repite 1
Palabra DIALOGAR se repite 1
Palabra CONSTRUIR se repite 1
Palabra CONSENSOS se repite 1
Palabra ESTA se repite 1
Palabra HORA se repite 1
Palabra DECISIVA se repite 1
Palabra REPÚBLICA se repite 2
Palabra SE se repite 2
Palabra REQUIERE se repite 1
Palabra HAGAMOS se repite 1
Palabra COINCIDENCIAS se repite 1
Palabra BASE se repite 1
Palabra ALCANZAR se repite 1
Palabra ACUERDOS se repite 1
Palabra ESENCIALES se repite 1
Palabra NECESITA se repite 1
Palabra PLURALIDAD se repite 1
Palabra DIFERENCIA se repite 1
Palabra VISIONES se repite 1
Palabra LUGAR se repite 1
Palabra SER se repite 1
Palabra OBSTÁCULO se repite 1
Palabra PERMITAN se repite 1
Palabra ASCENSO se repite 1
Palabra ENRIQUEZCAN se repite 1
Palabra PROYECTO se repite 1
Palabra NACIÓN se repite 2
Palabra QUEREMOS se repite 1
Palabra SIGLO se repite 1
Palabra XXI se repite 1
Palabra COMO se repite 1
Palabra ESTOY se repite 1
Palabra PLENAMENTE se repite 1
Palabra CONVENCIDO se repite 1
Palabra GOBERNAR se repite 1
Palabra DEMOCRACIA se repite 1
Palabra SIGNIFICA se repite 2
Palabra ESTAR se repite 1
Palabra ATENTO se repite 1
Palabra ESCUCHAR se repite 1
Palabra DIVERSAS se repite 1
Palabra VOCES se repite 1
Palabra EXPRESAN se repite 1
Palabra SENTIR se repite 1
Palabra MEXICANOS se repite 1
Palabra HE se repite 1
Palabra SEÑALADO se repite 1
Palabra PLENA se repite 1
Palabra CONVICCIÓN se repite 1
Palabra SERÉ se repite 1
Palabra DEMOCRÁTICO se repite 1
Palabra ESTO se repite 1
Palabra VOLUNTAD se repite 2
Palabra ABSOLUTA se repite 1
Palabra CONCILIAR se repite 1
Palabra POSICIONES se repite 1
Palabra ANTEPONER se repite 1
Palabra INVARIABLEMENTE se repite 1
Palabra INTERÉS se repite 1
Palabra SUPERIOR se repite 1

caracteres = ("?", "¿", "¡", "!", ",", ".", ";", ":")
t = t.upper()
texto = "" 
for i in t:
    if not i in caracteres:
        texto += i
texto = texto.split(" ")
}
"""
t = "Muy buenas tardes a todas y a todos ustedes. "
t=t+"Quiero saludar, con respeto, al Presidente de la Cámara de Diputados y al "
t=t+"Presidente de la Cámara de Senadores. "
t=t+"A los señores Dirigentes de los partidos políticos en nuestro país. A sus "
t=t+"principales fuerzas. "
t=t+"De igual forma, saludo con respeto a los señores Gobernadores. A "
t=t+"Gobernadores electos. Al Jefe de Gobierno electo del Distrito Federal. Todos "
t=t+"ellos con origen en distintas expresiones políticas. "
t=t+"Saludo a los señores Coordinadores Parlamentarios de distintas fuerzas "
t=t+"políticas que están, hoy, aquí presentes. "
t=t+"Con respeto, también, saludo a la representación, en actores políticos "
t=t+"distinguidos, de las distintas fuerzas políticas de nuestro país. "
t=t+"A todos, les saludo con afecto y reconocimiento por este encuentro, sin duda, "
t=t+"inédito, pero que representa un gran paso para impulsar la trasformación de "
t=t+"nuestro país. Es el punto de encuentro y de coincidencia que, realmente, "
t=t+"aplaudo, celebro, y que sea para el bien de México. "
t=t+"México comienza una nueva etapa de su vida democrática. Ha llegado el "
t=t+"momento del encuentro y del acuerdo. Ha llegado el momento de dar el "
t=t+"siguiente paso en el perfeccionamiento democrático: Transitar del sufragio "
t=t+"efectivo al gobierno eficaz. "
t=t+"En este propósito, los actores políticos deben, o debemos, caminar juntos. "
t=t+"Debemos dialogar para construir consensos. En esta hora decisiva de la vida "
t=t+"de la República se requiere que los políticos hagamos de las coincidencias la "
t=t+"base para alcanzar los acuerdos esenciales. "
t=t+"Se necesita que la pluralidad y la diferencia de visiones, en lugar de ser "
t=t+"obstáculo, permitan el ascenso de México, enriquezcan el proyecto de Nación "
t=t+"que todos queremos para el Siglo XXI. "
t=t+"Como Presidente de la República, estoy plenamente convencido que "
t=t+"gobernar en democracia significa estar atento y escuchar a las diversas "
t=t+"voces que expresan el sentir de los mexicanos. "
t=t+"He señalado, con plena convicción, que seré un Presidente democrático. "
t=t+"Esto significa voluntad absoluta para conciliar posiciones. Voluntad para "
t=t+"anteponer, invariablemente, el interés superior de la Nación."
texto = t
caracteres = (",", ".", ";", ":")
for i in caracteres:
	texto = texto.replace(i,'')
texto = texto.upper()
texto = texto.split(' ')
print ("TOTAL DE PALABRAS: {}\n".format(len(texto)))
while texto != []:
	cont1 = texto[0]
	cont2 = 0
	for j in texto:
		if j == cont1:
			cont2 +=1
			texto.remove(j)
	print('Palabra {} se repite {}'.format(cont1,cont2))
