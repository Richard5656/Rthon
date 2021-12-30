town_map ="""
-----------------------------------------------|
            ||ooo ||                           |
            ||    ||                           |
            ||    ||                     |---- |
            ||    ||                     |S    |
                                         |h    |
                                         |o    |
                                         |p    |
                                         |---- |
                                               |
                                               |
                                               |
-----------------------------------------------|"""
#48 accross ^^^
#13 down ^^^


anoter = """
----------------------------|
      |        |            |
      |        |            |
      |        |a4          |
      |        |            |
      |        |            |
      |        |            |
---------------------------||
      Welcome!              |
                            |
----------------------------|"""
#29 accross ^^^
#11 down ^^^


buffer = []
town_map = town_map.replace("\n","")
for i in range(len(town_map)):
    buffer.append(town_map[i])

town_map = buffer




#anoter = anoter.replace("\n","") 
