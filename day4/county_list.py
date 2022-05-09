county_list = ["Stockholm", "Västerbotten", "Norrbotten", "Uppsala", "Södermanland", "Östergötland", "Jönköping", "Kronoberg", "Kalmar", "Gotland", " Blekinge", "Skåne", "Halland", " Västra Götaland", " Värmland", "Örebro", "Västmanland", "Dalarna", "Gävleborg", "Västernorrland", "Jämtland"] 
print(county_list)
print(county_list.count("Stockholm"))

copy_list = county_list.copy()
print(copy_list)
copy_list.reverse()
print(copy_list)
copy_list.sort( key=None, reverse=False)
print(copy_list)
copy_list.append("Nykvarn")
print(copy_list)